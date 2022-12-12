from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from payments.models import *
from payments.serializers import *
from django.db.models import Q
from drf_spectacular.utils import extend_schema

@extend_schema(
    request=PurchaseSerializer(many=True)
)
@api_view(["post"])
def purchase(request):
    # 결제 가능한지 확인
    user = request.user
    amount = 0
    serializer = PurchaseSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    queryset = Q()
    for item in serializer.validated_data:
        queryset = queryset | Q(id=item["product_id"], stock__gte=item["quantity"])

    products = Product.objects.filter(queryset).order_by("id")
    if len(serializer.validated_data) != len(products): #len을 쓸 때 products를 불러오는데 count로 하면 count 쿼리만 돌림(비효율적)
        raise ValidationError("including sold out item")

    # 스톡 정보 업데이트
    sorted_data = list(sorted(serializer.validated_data, key=lambda x : x['product_id']))
    payment_items = []
    for item, product in zip(sorted_data, products):
        product.stock -= item["quantity"]
        product.sales_count += item["quantity"]
        amount += product.price * item["quantity"]
        product.save(update_fields=["stock", "sales_count"])
        payment_items.append(PaymentItem(product=product,quantity=item["quantity"]))

    # 결제 생성
    payment = Payment.objects.create(buyer=user, amount=amount)
    for item in payment_items:
        item.payment = payment
    PaymentItem.objects.bulk_create(payment_items)

    return Response({"status":"success", "payment_id":payment.id})
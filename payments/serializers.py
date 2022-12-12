from rest_framework import serializers
from payments.models import *

# class PurchaseSerializer(serializers.Serializer):
#     product_id = serializers.IntegerField()
#     quantity = serializers.IntegerField()

class PurchaseSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model=PaymentItem
        fields=("product", "product_id", "quantity", "payment")
        read_only_fields=("payment", "product")
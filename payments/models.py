from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from products.models import Product

class Payment(models.Model):
    buyer = models.ForeignKey(User, null=True, blank=True, verbose_name=_("buyer of payment"), on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1) # 총액

class PaymentItem(models.Model): #유저가 구매한 아이템
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) # 수량

from django.db import models
from accounts.models import User

class Product(models.Model): # 상품
    stock = models.PositiveIntegerField(default = 0)
    category = models.IntegerField(default=0)
    price = models.PositiveBigIntegerField(default=0)
    name = models.CharField(default="", max_length=30)
    description = models.TextField(default="")
    sales_count = models.PositiveBigIntegerField(default=0)

# class Cart(models.Model): # 장바구니
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product,blank=True, through="ProductCart")

# class ProductCart(models.Model): # 장바구니 속 아이템(m2m)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField(default=1)

from django.contrib import admin

from products.models import Product

# Register your models here.
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass
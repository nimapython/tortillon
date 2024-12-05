from django.contrib import admin

# Register your models here.

from .models import Product,Cart,Order,CartItem
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartItem)


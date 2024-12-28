from django.contrib import admin

# Register your models here.
from .models import Product 
admin.site.register(Product)

from .models import  CartItem
admin.site.register(CartItem)
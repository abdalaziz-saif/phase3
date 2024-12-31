
from django.contrib import admin 


# Register your models here.
from .models import  User , Category
admin.site.register(User)
admin.site.register(Category)

from .models import Product 
admin.site.register(Product)

from .models import  CartItem
admin.site.register(CartItem)
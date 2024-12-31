from django.urls import path
from . import views
# login,
# product_list,
# add_to_cart,
# cart_details,
# remove_from_cart,
from .views import check_user_exists



urlpatterns = [
    path('' ,views.index, name='index'),
    path('home/' ,views.home, name='home'),
    path('login/',views.login, name='login'),
    path('check-user/', check_user_exists, name='check_user_exists'),
    path("category/<str:cat>",views.category, name='category'),

#     path('', product_list, name='product_list'),
#     path('add-to-cart/', add_to_cart, name='add_to_cart'),
#     path('cart/', cart_details , name='cart_details'),
#     path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
]


   
       





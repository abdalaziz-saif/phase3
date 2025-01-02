from django.urls import path
from . import views
from django.conf import settings
from .views import check_user_exists
from django.conf .urls.static import static
from django.shortcuts import redirect 
from .views import update_cart_quantity, checkout, history_view



def redirect_to_search(request): 
    return redirect('search') 
path('home/search.html', redirect_to_search),

def redirect_to_cart(request): 
    return redirect('search') 
path('home/cart.html', redirect_to_cart),


urlpatterns = [
    path('' ,views.index, name='index'),
    path('home/' ,views.home, name='home'),
    path('login/',views.login, name='login'),
    path('check-user/', check_user_exists, name='check_user_exists'),
    path("category/<str:cat>",views.category, name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('home/cart/', views.cart, name='cart'),
    path('update-cart/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart_view/',views.cart_view,name='cart_view'),
    path('update_cart_item/<int:cart_item_id>/',views. update_cart_item, name='update_cart_item'),
  


    path('update-cart-quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('history/', history_view, name='history_view'),
    # Add other URL patterns here
]




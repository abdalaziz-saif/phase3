from django.urls import path
from . import views
from django.conf import settings
from .views import check_user_exists
from django.conf.urls.static import static


def redirect_to_search(request): 
    return redirect('search') 
path('home/search.html', redirect_to_search),


urlpatterns = [
    path('' ,views.index, name='index'),
    path('home/' ,views.home, name='home'),
    path('login/',views.login, name='login'),
    path('check-user/', check_user_exists, name='check_user_exists'),
    path("category/<str:cat>",views.category, name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
#path('history/', views.history, name='history'),

#path('product/<int:product_id>/', views.product_detail, name='product_detail'),


#     path('', product_list, name='product_list'),
#     path('add-to-cart/', add_to_cart, name='add_to_cart'),
#     path('cart/', cart_details , name='cart_details'),
#     path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, CartItem
 
def login(request):
    return render(request,'pages/login.html',{'name':'ahmed'})
 
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(id=product_id)
        
        cart_item, created = CartItem.objects.get_or_create(product=product)
        cart_item.quantity += quantity
        cart_item.save()

#         return JsonResponse({'message': 'Product added to cart!', 'cart_item_count': cart_item.quantity})
#     return JsonResponse({'error': 'Invalid request'})

# def cart_details(request):
#     cart_items = CartItem.objects.all()
#     total_price = sum(item.get_total_price() for item in cart_items)
#     return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# def remove_from_cart(request):
#     if request.method == "POST":
#         cart_item_id = request.POST.get('cart_item_id')
#         CartItem.objects.get(id=cart_item_id).delete()
#         return JsonResponse({'message': 'Item removed from cart!'})
#     return JsonResponse({'error': 'Invalid request'})

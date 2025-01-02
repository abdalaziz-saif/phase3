from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, CartItem 
from django.shortcuts import get_object_or_404
from .models import Category 
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import User
from .models import CartItem, HistoryItem



def category(request,cat):
    try:
        category=get_object_or_404(Category, name=cat)

        products=Product.objects.filter(category=category)
        
        return render(request,'pages/category.html',{'products':products , 'category':category })
    except:
           messages.success(request , ("This category deos Note exist"))
           return redirect('home')

def update_cart_item(request, cart_item_id): 
    if request.method == 'POST':
         cart_item = get_object_or_404(CartItem, id=cart_item_id) 
         quantity = int(request.POST.get('quantity', 1))
         cart_item.quantity = quantity 
         cart_item.save() 
         return redirect('cart')

def cart_details(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})

        
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404

def update_cart_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity', 1))
        
        # Fetch the cart item or return a 404 error
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        
        if quantity > 0:
            # Update the quantity
            cart_item.quantity = quantity
            
            # Calculate the new total price
            cart_item.total_price = cart_item.unit_price * quantity
            
            # Save the changes
            cart_item.save()
        else:
            # Optionally, handle invalid quantity values
            pass
        
        return redirect('cart_view')


    

def remove_from_cart(request, cart_item_id): 
    cart_item = get_object_or_404(CartItem, id=cart_item_id) 
    cart_item.delete() 
    return redirect('cart')


def check_user_exists(request):
    username = request.GET.get('username')
    password = request.GET.get('password') 

    if not username or not password: 
        return JsonResponse({'exists': False, 'message': 'Username and password are required!'}) 
    user = User.objects.filter(username=username, password=password).first() 
    
    if user and password: 
     return JsonResponse({'exists': True, 'message': 'User exists!'}) 
    else: 
     return JsonResponse({'exists': False, 'message': 'User does not exist, you can proceed!'})

def cart(request): 
    cart_items = CartItem.objects.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'pages/cart.html', {'cart_items': cart_items,'total_price': total_price})

def home(request):
   return render(request,'pages/home.html')

def index(request):
   return render(request,'pages/index.html')


def login(request):
    return render(request,'pages/login.html',{'name':'ahmed'})
 
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
def add_to_cart(request, product_id): 
    if request.method == 'POST': 
      
         product = get_object_or_404(Product, id=product_id) 
         quantity = int(request.POST.get('quantity', 1)) 
       
         cart_item, created = CartItem.objects.get_or_create( 
             product=product,
               defaults={'quantity': quantity} )
         if not created: 
            cart_item.quantity += 1
            cart_item.save() 
            return redirect('cart')
         else:
             return redirect('cart')
def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price}  ) 


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/single_product.html', {'product': product})

def history(request):
    return render(request, 'pages/history.html')

def search(request): 
    query = request.GET.get('query', '') 
    category = request.GET.get('category', 'all') 
    brand = request.GET.get('brand', 'all') 
    products = Product.objects.all() 
 
    if query: 
        products = products.filter(name__icontains=query)   
 
    if category != 'all': 
        products = products.filter(category_name_iexact=category) 
 
    if brand != 'all': 
        products = products.filter(brand_name_iexact=brand)   
 
    return render(request, 'pages/search.html', {'results':products})

def checkout(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.all()
        for item in cart_items:
            total_price = item.product.price * item.quantity
            HistoryItem.objects.create(
                product=item.product,
                quantity=item.quantity,
                total_price=total_price
            )
        cart_items.delete()
        return redirect('history_view')


 

def history_view(request):
    history_items = HistoryItem.objects.all()
    return render(request, 'history.html', {'history_items': history_items})


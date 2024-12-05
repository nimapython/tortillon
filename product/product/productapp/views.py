from django.shortcuts import redirect, render
from .models import CartItem, Order, Product,Cart
from django.contrib.auth.models import User
from django.contrib import messages,auth
from decimal import Decimal 

# Create your views here.

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def register(request):
    if request.method=='POST':
        name=request.POST['name']
        uname=request.POST['username']
        password=request.POST['password']
      

    
        if User.objects.filter(username=uname).exists():
                messages.info(request,"username already taken")
       
        else:
            user=User.objects.create_user(first_name=name,username=uname,password=password)
            user.save()
            return render(request,'login.html')
   
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
            
        else:
            messages.info(request,"invalid entry")
    return render(request,'login.html')


def detail(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,'detail.html',{'product':product})


def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    
    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1  
    cart_item.save()

    return redirect('detail', product_id=product.id)


def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    print(cart_items)
    grand_total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'grand_total': grand_total})



def delete(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart')


def place_order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    if cart_items.exists():
        total_price = Decimal(0)
        for item in cart_items:
            total_price += item.get_total_price()

        order = Order.objects.create(
            user=user,
            cart=cart,
            total_price=total_price,
        )

        cart_items.delete()

        messages.success(request, 'Your order has been placed successfully.')

        return redirect('cart')
    else:
        messages.error(request, 'Your cart is empty. Please add items to your cart before placing an order.')
        return redirect('cart')
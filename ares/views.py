from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from ares.forms import AddToCartForm
from cart.cart import Cart
from order.models import Order, OrderItem

from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
import random
from django.db.models import Q

# Create your views here.
def add_product(request):
    if request.method=="POST":
        name = request.POST.get('product_name')
        spec = request.POST.get('specification')
        imagedata = request.POST.get('image_data')
        rentprice = request.POST.get('rent_price')
        buyprice = request.POST.get('buy_price')
        product = Product(product_name = name, spec = spec, image_data = imagedata, rent_price=rentprice, buy_price= buyprice)
        product.save()
        return HttpResponse("<h1>Product details saved</h1>")
    return render(request, 'seller/add_product.html')
 

def profile(request):
    products = Product.objects.all()
    return render(request, 'seller/index.html', {'products' : products})

def homepage(request):
    products = Product.objects.all()
    return render(request, 'seller/home.html', {'products' : products})   
   

def productView(request, slug):
    # Fetch the product using the id
    product = Product.objects.filter(slug=slug).first()
    context={'product':product}
    return render(request, 'single_product/single_product.html', context)
    
def cart(request):
    return render(request, "checkout/checkout.html")    




def product_sell(request, slug):
    # Create instance of Cart class
    cart = Cart(request)

    product = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.create(item=product)
    order = Order.objects.all()

    # Check whether the AddToCart button is clicked or not
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.product_id, quantity=quantity, update_quantity=False)

            messages.success(request, "The product was added to the cart.")

            return redirect('product:product', slug=slug)            
    
    else:
        form = AddToCartForm()

    # similar_products = list(product.category.products.exclude(id=product.id))

    # # If more than 4 similar products, then get 4 random products 
    # if len(similar_products) >= 4:
    #     similar_products = random.sample(similar_products, 4)
    
    context = {
        'product': product,
        #'similar_products': similar_products,
        'form': form,
    }

    return render(request, 'product/product.html', context)

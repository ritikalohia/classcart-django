from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

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



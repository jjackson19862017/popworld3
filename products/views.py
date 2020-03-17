from django.shortcuts import render, redirect, reverse
from .models import Product
from .forms import ProductsForm
from django.contrib import messages

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})

def addproducts(request):
    print("Loaded view")
     
    if request.method == 'POST':
       
        APF = ProductsForm(request.POST, request.FILES)
        
        if APF.is_valid():
            APF.save()
            messages.error(request, "Product Added!")
            return render(request, "addproducts.html", {'APF': APF})
        else:
            messages.error(request, "Unable to ADD this product.")
                    
    else:
        APF = ProductsForm()

    return render(request, "addproducts.html", {'APF': APF})

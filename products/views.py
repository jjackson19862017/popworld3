from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import ProductsForm
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})

def SAO_products(request):
    products = Product.objects.filter(series__exact='Sword Art Online')
    return render(request, "products.html", {"products":products})

def addproducts(request):
    if request.method == 'POST':
       
        APF = ProductsForm(request.POST, request.FILES)
        
        if APF.is_valid():
            APF.save()
            messages.error(request, "Product Added!")
            APF = ProductsForm()
            return render(request, "addproducts.html", {'APF': APF})
        else:
            messages.error(request, "Unable to ADD this product.")
                    
    else:
        APF = ProductsForm()

    return render(request, "addproducts.html", {'APF': APF})

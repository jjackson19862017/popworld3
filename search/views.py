from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})

def SAO_search(request):
    products = Product.objects.filter(series__iexact='Sword Art Online')
    return render(request, "products.html", {"products":products})

def Bleach_search(request):
    products = Product.objects.filter(series__iexact='Bleach')
    return render(request, "products.html", {"products":products})

def DBZ_search(request):
    products = Product.objects.filter(series__iexact='Dragonballz')
    return render(request, "products.html", {"products":products})
from django.conf.urls import url, include
from .views import all_products, addproducts, SAO_products


urlpatterns = [
    url(r"^$", all_products, name="products"),
    url(r"^SAO/$", SAO_products, name="SAO_products"),
    url(r"^add/$", addproducts, name="addproducts"),
]

from django.conf.urls import url, include
from .views import all_products, addproducts


urlpatterns = [
    url(r"^$", all_products, name="products"),
    url(r"^add/$", addproducts, name="addproducts"),
]

from django.conf.urls import url
from .views import all_bids

urlpatterns = [
    url(r'', all_bids, name="bid"),
    
    ]
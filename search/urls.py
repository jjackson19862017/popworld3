from django.conf.urls import url
from .views import do_search, SAO_search, Bleach_search,dbz_search

urlpatterns = [
    url(r'^/Bleach$', Bleach_search, name='Bleach_search'),
    url(r'^/Dbz$', dbz_search, name='dbz_search'),
    url(r'^/SAO$', SAO_search, name='SAO_search'),
    url(r'^$', do_search, name='search'),
]

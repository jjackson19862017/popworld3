from django.db import models
from products.models import Product
from django.utils import timezone

# Create your models here.

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_number = models.IntegerField(default=1)
    start_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    auction_open = models.CharField(max_length=10, blank=False, null=False, default="Open")
    
    def __str__(self):
        return  "product_id:" + str(self.product_id)
        
        
    
    
    
   
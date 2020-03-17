from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default= '')
    description = models.TextField()
    original_item_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    instant_buy_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    reserved_buy_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/',
                             width_field="width_field",
                             height_field="height_field",
                             blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    series = models.CharField(max_length=200, default= '')
    character = models.CharField(max_length=200, default= '')
    current_auction_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.name

from django import forms
from .models import Auction


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('product_id', 'bid_number', 'start_date','end_time','auction_open')
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from .forms import AuctionForm
from products.models import Product
from bids.models import Bid

def all_auctions(request):
    """ Creates a view so only registered users can see the auctions """
    if request.user.is_authenticated:
        auctions = Auction.objects.all()
        return render(request, "auction.html", {"auctions": auctions})
    else:
        messages.error(request, "Im sorry but you need to be logged in")
        return redirect(reverse('index'))
        
    return render(request, "index.html")

def open_auctions(request):
    """ Creates a view so only registered users can see the auctions that are currently open """
    if request.user.is_authenticated:
        auctions = Auction.objects.filter(auction_open__iexact='Open')
        return render(request, "auction.html", {"auctions": auctions})
    else:
        messages.error(request, "Im sorry but you need to be logged in")
        return redirect(reverse('index'))
        
    return render(request, "index.html")    

def open_auction(request):
    
    """ Allows a registered user to bid on open auctions """
    
    if request.method == "POST":
            product_id = request.POST['product_id']
            auction = Auction.objects.get(product_id=product_id)
            """ Make sure Auction is still Open """
            if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
                product = Product.objects.get(id=product_id)
                product.current_auction_price += int(request.POST['UpBid'])
                product.save()
                current_bid = Bid.objects.filter(product_id=product_id)
                if current_bid:
                    bid = current_bid[0]
                    bid.user_id = request.user
                    bid.bid_time = timezone.now()
                    bid.bid_views += 1
                    bid.save()
                else:
                    new_bid = Bid()
                    new_bid.product_id = product
                    new_bid.auction_id = auction
                    new_bid.user_id = request.user
                    new_bid.bid_time = timezone.now()
                    new_bid.bid_views += 1
                    new_bid.save()
                messages.error(request, "Well done you have placed a bid.")
            else:
                auction.auction_open = "Closed"
                auction.save()
                messages.error(request, "This Auction is closed.")
            
    return redirect(reverse('auctions'))
        
def buy_now(request):

    """ Allows a user to buy an Item Straight away, closing the Auction """
    if request.method == "POST":
        product_id = request.POST['product_id']
        auction = Auction.objects.get(product_id=product_id)
        """ Make sure Auction is still Open """
        if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
            product = Product.objects.get(id=product_id)
            return render(request, "bid.html")
        else:
            messages.error(request, "This Auction is closed")
    return redirect(reverse('auctions'))

def add_auctions(request):
    """ Allows Owner to Open Auctions """
    if request.method == 'POST':
        AF = AuctionForm(request.POST)
        if AF.is_valid():
            AF.save()
            messages.error(request, "Auction Started!")
            return render(request, "addauctions.html", {'AF': AF})
        else:
            messages.error(request, "Auction Failed!")
    else:
        AF = AuctionForm()
    
    return render(request, "addauctions.html", {'AF': AF})

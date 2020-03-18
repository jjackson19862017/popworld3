from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages


def all_bids(request):
    """ Shows logged in users all the bids """
    if request.user.is_authenticated:
        bid = Bid.objects.all()
        end_time_list = []
        for i in bid:
            end_time_list.append(str(i.auction_id.end_time))
        return render(request, "bid.html", {"bid": bid, 'end_time':end_time_list})
    else:
        messages.error(request, "You must be Logged in")
        return redirect(reverse('login'))
    return render(request, "bid.html", {"bid": bid})

def bid_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {bid.id})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('all_bids'))



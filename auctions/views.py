from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, AuctionListings, Bid, Comments





def create_listing(request):
    return render(request, "auctions/create_listing.html")

def save_listing(request):
    if request.method == "POST":
        name_of_item = request.POST['name_of_item']
        user = request.user 
        description = request.POST['description']
        category = request.POST['category']
        image_url = request.POST['image_url']
        bid = Bid(bid=int(request.POST["bid"]), user=user)
        bid.save()
        listing = AuctionListings(name_of_item=name_of_item, description=description, owner=user, bid = bid, is_closed = False, url = image_url, category = category)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
        
    return render(request, "auctions/create_listing.html")

def display_listing(request, active_listings_id):
    listing = AuctionListings.objects.get(pk=active_listings_id)
    comments = listing.comments.all()
    if request.user == listing.owner:
        is_owner = True
    
    else: 
        is_owner = False
    is_listing_in_watchlist = request.user in listing.watchlist.all()

    return render(request,"auctions/display_listing.html",{
        "listing": listing,
        "comments": comments,
        "is_owner": is_owner,
        "is_listing_in_watchlist": is_listing_in_watchlist
        })

def add_watchlist(request,listing_id):
    user = request.user
    listing = AuctionListings.objects.get(pk=listing_id)
    listing.watchlist.add(user)
    return HttpResponseRedirect(reverse("display_listing",args=(listing_id,)))

def remove_watchlist(request,listing_id):
    listing = AuctionListings.objects.get(pk=listing_id)
    user = request.user
    listing.watchlist.remove(user)
    return HttpResponseRedirect(reverse("display_listing",args=(listing_id,)))


def close_auction(request, listing_id):
    listing = AuctionListings.objects.get(pk=listing_id)
    listing.is_closed = True
    listing.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))

def add_comment(request, listing_id):
    if request.method == "POST":
        user = request.user
        text = request.POST["comment"]
        listing = AuctionListings.objects.get(pk=listing_id)
        new_comment = Comments(text=text, writer=user, listing=listing)
        new_comment.save()
        return HttpResponseRedirect(reverse("display_listing",args=(listing_id,)))

def watchlist(request):
    user = request.user
    users_watchlist_of_items = user.watch_listings.all()
    return render(request, "auctions/watchlist.html",{
        "users_watchlist_of_items" : users_watchlist_of_items
        })
     
    
def category(request):
    if request.method == "POST":
        chosen_category = request.POST["category"]
        active_listings = AuctionListings.objects.filter(is_closed=False,category=chosen_category)
        return render(request, "auctions/index.html",{
            "active_listings": active_listings
        })   

def new_bid(request, listing_id):
    listing = AuctionListings.objects.get(pk=listing_id)
    new_bid = bid = int(request.POST["new_bid"])
    current_bid = listing.bid.bid 
   
    if new_bid > current_bid:
        updated_bid = Bid(bid = new_bid, user=request.user)
        updated_bid.save()
        listing.bid = updated_bid
        listing.save()
        return render(request,"auctions/display_listing.html", {
            "listing":listing,
            "message":"Your Bid was added successfully.",
            "updated": True,
            })
    else:
        return render(request,"auctions/display_listing.html",{
            "listing":listing,
            "message":"Sorry, your bid should be bigger than the latest bid.",
            "updated": False,
            })

def index(request):
    active_listings = AuctionListings.objects.filter(is_closed=False)
    return render(request, "auctions/index.html",{
        "active_listings": active_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
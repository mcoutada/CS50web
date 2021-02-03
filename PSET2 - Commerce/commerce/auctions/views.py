from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User
from django import forms
from django.forms import ModelForm
from auctions.models import *


class newListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'startingBid','image', 'category','startingBid']

def index(request):
    category_id = request.GET.get("category", None)
    if category_id is None:
        listings = Listing.objects.filter(is_active=True)
    else:
        listings = Listing.objects.filter(is_active=True, category=category_id)
        selectedCategory = Category.objects.get(id=category_id)
    categories = Category.objects.all()

    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": categories,
        "selectedCategory":selectedCategory if category_id else None,
    })



@login_required
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        if request.POST.get("button") == "Watchlist": 
            if not user.watchlist.filter(listing= listing):
                watchlist = Watchlist()
                watchlist.user = user
                watchlist.listing = listing
                watchlist.save()
                watchlistMsg = "Remove from Watchlist"
            else:
                user.watchlist.filter(listing=listing).delete()
                watchlistMsg = "Add to Watchlist"
        return HttpResponseRedirect(reverse('listing', kwargs={'listing_id':listing_id}))

    else:
        if user.watchlist.filter(listing= listing):
            watchlistMsg = "Remove from Watchlist"
        else:
            watchlistMsg = "Add to Watchlist"       
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "watchlistMsg":watchlistMsg,
            # "listing_pictures": listing.get_pictures.all(),
            # "form": newBidForm(),
            # "comments": listing.get_comments.all(),
            # "comment_form": newCommentForm()        
        })

# @login_required
# def addToWatchlist(request, listing_id):
#     user = request.user
#     listing = Listing.objects.get(pk=listing_id)
#     try:
#         Watchlist.objects.get(user = user) 
#     except:
#         Watchlist.objects.create(user = user)
#     watchlist = Watchlist.objects.get(user = user)
#     watchlist.item.add(listing)
#     watchlist.save()
#     return HttpResponseRedirect(reverse('listing', kwargs={'listing_id':listing_id}))

# @login_required
# def remFromWatchlist(request, listing_id):
#     user = request.user
#     listing = Listing.objects.get(pk=listing_id)
#     watchlist = Watchlist.objects.get(user = user)
#     watchlist.item.remove(listing)
#     watchlist.save()
#     return HttpResponseRedirect(reverse('listing', kwargs={'listing_id':listing_id}))

@login_required
def watchlist(request):
    listing_ids = Watchlist.objects.filter(user_id = request.user).values('listing_id')
    listing = Listing.objects.filter(id__in = listing_ids)
    return render(request, "auctions/watchlist.html", {
        "listings": listing
    })


@login_required
def newListing(request):
   
    if request.method == "POST":        
        form = newListingForm(request.POST, request.FILES)
        
       
        if form.is_valid():
            newListing = form.save(commit=False)
            newListing.seller = request.user
            newListing.save()

            return render(request, "auctions/newListing.html", {
                "form": newListingForm(),
                "message": "Successfully created"
        })
        else:
            return render(request, "auctions/newListing.html", {
                "form": newListingForm(),
                "message": "invalid form"
            })
    else:
        return render(request, "auctions/newListing.html", {
            "form": newListingForm()
        })    
    

# the below is code provided by CS50

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
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
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
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

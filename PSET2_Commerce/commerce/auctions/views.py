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
        fields = [
            "title",
            "description",
            "startingBid",
            "image",
            "category",
            "startingBid",
        ]


class newCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave your comment here",
                }
            )
        }


class newBidForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["currentBid"]
        labels = {
            "currentBid": "New Bid",
        }


def index(request):
    category_id = request.GET.get("category", None)
    if category_id is None:
        listings = Listing.objects.filter(is_active=True)
    else:
        listings = Listing.objects.filter(is_active=True, category=category_id)
        selectedCategory = Category.objects.get(id=category_id)
    categories = Category.objects.all()

    return render(
        request,
        "auctions/index.html",
        {
            "listings": listings,
            "categories": categories,
            "selectedCategory": selectedCategory if category_id else None,
        },
    )


@login_required
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        if request.POST.get("button") == "Watchlist":
            if not user.watchlist.filter(listing=listing):
                watchlist = Watchlist()
                watchlist.user = user
                watchlist.listing = listing
                watchlist.save()
                watchlistMsg = "Remove from Watchlist"
            else:
                user.watchlist.filter(listing=listing).delete()
                watchlistMsg = "Add to Watchlist"
        return HttpResponseRedirect(
            reverse("listing", kwargs={"listing_id": listing_id})
        )

    else:
        if user.watchlist.filter(listing=listing):
            watchlistMsg = "Remove from Watchlist"
        else:
            watchlistMsg = "Add to Watchlist"
        return render(
            request,
            "auctions/listing.html",
            {
                "listing": listing,
                "watchlistMsg": watchlistMsg,
                "form": newBidForm(),
                "comments": listing.get_comments.all(),
                "comment_form": newCommentForm(),
            },
        )


@login_required
def new_bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    # offer = request.POST.get("Bid").value
    offer = float(request.POST["currentBid"])
    user = User.objects.get(username=request.user)

    if user.watchlist.filter(listing=listing):
        watchlistMsg = "Remove from Watchlist"
    else:
        watchlistMsg = "Add to Watchlist"

    if offer > max(listing.currentBid, listing.startingBid):
        bidMessage = "Congrats! Your the current buyer"
        listing.currentBid = offer
        listing.buyer = user
        form = newBidForm(request.POST)
        listing.save()
    else:
        bidMessage = "Your bid is not higher than the current value"

    return render(
        request,
        "auctions/listing.html",
        {
            "listing": listing,
            "form": newBidForm(),
            "message": bidMessage,
            "watchlistMsg": watchlistMsg,
        },
    )


@login_required
def watchlist(request):
    listing_ids = Watchlist.objects.filter(user_id=request.user).values("listing_id")
    listing = Listing.objects.filter(id__in=listing_ids)
    return render(request, "auctions/watchlist.html", {"listings": listing})


@login_required
def newListing(request):

    if request.method == "POST":
        form = newListingForm(request.POST, request.FILES)

        if form.is_valid():
            newListing = form.save(commit=False)
            newListing.seller = request.user
            newListing.save()

            return render(
                request,
                "auctions/newListing.html",
                {"form": newListingForm(), "message": "Successfully created"},
            )
        else:
            return render(
                request,
                "auctions/newListing.html",
                {"form": newListingForm(), "message": "invalid form"},
            )
    else:
        return render(request, "auctions/newListing.html", {"form": newListingForm()})


@login_required
def comment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    form = newCommentForm(request.POST)
    newComment = form.save(commit=False)
    newComment.user = request.user
    newComment.listing = listing
    newComment.save()
    return HttpResponseRedirect(reverse("listing", kwargs={"listing_id": listing_id}))


def close_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user == listing.seller:
        listing.is_active = False
        listing.save()
        return HttpResponseRedirect(
            reverse("listing", kwargs={"listing_id": listing_id})
        )
    else:
        listing.watchers.add(request.user)
    return HttpResponseRedirect(reverse("watchlist"))


###########################################################################################
# the below is code provided by CS50
###########################################################################################


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

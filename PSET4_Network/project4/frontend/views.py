from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from network.models import User, Post, UserFollowing
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)

@csrf_exempt
@login_required
def newpost(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    Post(user=request.user, content=request.POST['content']).save()
    return JsonResponse({"success": "message posted successfully!"})

def posts(request):
    posts = Post.objects.all()
    serialized_posts = [each_post.serialize() for each_post in posts]
    
    return JsonResponse(serialized_posts, safe=False)

def profile(request, owner):
    owner = User.objects.get(id=owner)
    # button = "Follow" if Follow.objects.filter(follower=request.user, following=owner).count() == 0 else "Unfollow"

    # if request.method == "POST":
    #     if request.POST["button"] == "Follow":
    #         button = "Unfollow"
    #         Follow.objects.create(follower=request.user, following=owner)
    #     else:
    #         button = "Follow"
    #         Follow.objects.get(follower=request.user, following=owner).delete()

    # posts = Post.objects.filter(user=owner.id).order_by('-timestamp')
    # for post in posts:
    #     post.likes = Like.objects.filter(post=post.id).count()
    #     post.save()

    # paginator = Paginator(posts, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # return render(request, "network/profile.html", {
    #     "owner": owner,
    #     "followers": Follow.objects.filter(following=owner).count(),
    #     "following": Follow.objects.filter(follower=owner).count(),
    #     "page_obj": page_obj,
    #     "button": button
    # })

    return render(request, "network/profile.html")


############# All the code below is was provided by cs50 #############
def index(request):
    return render(request, "network/index.html")


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
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


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
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

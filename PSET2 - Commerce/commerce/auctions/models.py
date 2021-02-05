from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    seller = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_who_make_the_auction')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='auctions/static/auctions/img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="similar_listings")
    is_active = models.BooleanField(default=True)    
    created = models.DateTimeField(default=timezone.now)
    startingBid = models.FloatField(default=0)
    currentBid = models.FloatField(default=0)
    buyer = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.title} - {self.startingBid}"
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")


    def __str__(self):
        return f"{self.user}: {self.comment}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.user.username} listed {self.listing.id}"
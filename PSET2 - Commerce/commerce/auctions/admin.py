from django.contrib import admin

# Register your models here.
from .models import User, Category, Listing, Comment, Watchlist

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Watchlist)

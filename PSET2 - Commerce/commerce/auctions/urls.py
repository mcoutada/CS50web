from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # the paths above were provided by CS50
    path("newListing", views.newListing, name="newListing"),
    path("auction/listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
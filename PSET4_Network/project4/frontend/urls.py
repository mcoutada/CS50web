
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:owner>", views.profile, name="profile"),
    path("newpost", views.newpost, name='newpost'),
    path("posts", views.posts, name='posts'),
]

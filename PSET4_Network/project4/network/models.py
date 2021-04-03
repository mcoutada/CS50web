from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User,  blank=True, related_name="liked_user")
    likes = models.IntegerField(default=0)
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %#d %Y, %#I:%M %p"),
            "writer_id": self.user.id,
            "writer_name": self.user.username,
            "likes": self.likes,
        }
        
# related_name is needed otherwise:
# network.UserFollowing.following_user_id: (fields.E304) Reverse accessor for 'UserFollowing.following_user_id' clashes with reverse accessor for 'UserFollowing.user_id'.        
#       HINT: Add or change a related_name argument to the definition for 'UserFollowing.following_user_id' or 'UserFollowing.user_id'.
class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "following")
    following_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followers")
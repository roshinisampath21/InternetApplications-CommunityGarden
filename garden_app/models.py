# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class CommunityGarden(models.Model): #rosh
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Post(models.Model): #rosh
    group = models.ForeignKey(GardeningGroup, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.created_at}"
    

class Profile(models.Model):  #yash
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class UserHistory(models.Model): #yash
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    garden = models.ForeignKey(CommunityGarden, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
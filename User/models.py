from django.db import models
from Creator.models import*

# Create your models here.


class FormUser(models.Model):
    name = models.CharField(max_length=50)
    usr_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="UserPictures/Profile",null=True, blank=True)
    bannerimage = models.ImageField(upload_to="UserPictures/Banner",null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True,null=True)

class Playlist(models.Model):
    PlaylistName = models.CharField(max_length=50)
    Playlist_Cover = models.ImageField(upload_to="User/Playlist", null=True, blank=True)
    UsrId = models.ForeignKey(FormUser, on_delete=models.CASCADE)

class PlaylistItem(models.Model):
    Plid = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    MusicId = models.ForeignKey(Music, on_delete=models.CASCADE)

class FollowCr(models.Model):
    follower = models.ForeignKey(FormUser, on_delete=models.CASCADE, related_name='following_User')
    following = models.ForeignKey(Creators, on_delete=models.CASCADE, related_name='followed_Creator')
    date_followed = models.DateTimeField(auto_now_add=True)
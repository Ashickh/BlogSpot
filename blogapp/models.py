from django.db import models
from django.contrib.auth.models import User
import random


class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=120)
    phone=models.CharField(max_length=15)
    dob=models.DateField(null=True)
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )
    gender=models.CharField(max_length=12,choices=options,default="Male")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    following=models.ManyToManyField(User,related_name="followings",blank=True)

    @property
    def fetch_following(self):
        my_followings=[user for user in self.following.all()]
        return my_followings

        # return self.following.all()
    #
    # def fetch_following_count(self):
    #     return self.fetch_following.count()

    @property
    def fetch_following_count(self):
        return len(self.fetch_following)

        # return self.following.all()
    @property
    def get_invitations(self):
        all_users=UserProfile.objects.all().exclude(user=self.user) # fetch all users except current user
        user_list=[userprofile.user for userprofile in all_users]
        myfollowers=[u for u in self.fetch_following]
        invitations=[user for user in user_list if user not in myfollowers]   # exclude my folloings from all users
        return invitations

    def get_followers(self):
        all_user_profile=UserProfile.objects.all()
        my_followers=[]
        for profile in all_user_profile:
            if self.user in profile.fetch_following:
                my_followers.append(profile)
        return my_followers
    def my_follower_count(self):
        return len(self.get_followers)



class Blogs(models.Model):

    description=models.CharField(max_length=260)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    image=models.ImageField(upload_to="blogimages",null=True)
    liked_by=models.ManyToManyField(User)
    posted_date=models.DateTimeField(auto_now_add=True)



    @property
    def get_like_count(self):
        like_count=self.liked_by.all().count()
        return like_count
    @property
    def get_liked_users(self):
        liked_users=self.liked_by.all()
        users=[user.username for user in liked_users]
        return users





    def __str__(self):
        return self.title

class Comments(models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment = models.CharField (max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment






# Create your models here.

# users [ 1. ashiq   2. rinsha   3. zammu ]
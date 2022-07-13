from django.db import models
from django.contrib.auth.models import User


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






class Blogs(models.Model):
    title=models.CharField(max_length=150)
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
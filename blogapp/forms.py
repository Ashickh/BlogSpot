from django.contrib.auth.models import  User
from django.forms import  ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogapp.models import UserProfile,Blogs,Comments


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]
        widgets = {
            "email": forms.EmailInput (attrs={'class': 'form-control' }),
            "username": forms.TextInput (attrs={'class': 'form-control'}),
            "last_name": forms.TextInput (attrs={'class': 'form-control'}),
            "first_name": forms.TextInput (attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded-pill'}))

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)
        widgets={
            "dob":forms.DateInput(attrs={'class':'form-control','type':'date'})
        }

class PasswordResetForm(forms.Form):
    old_pwd=forms.CharField(widget=forms.PasswordInput)
    new_pwd=forms.CharField(widget=forms.PasswordInput)
    confirm_pwd=forms.CharField()

class BlogForm(ModelForm):
    class Meta:
        model=Blogs
        fields=[
            "title",
            "description",
            "image"
        ]
        widgets={
            "title": forms.TextInput (attrs={'class': 'form-contol'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "image":forms.FileInput(attrs={'class':'form-control'})
        }

class ProfilePicUpdateForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=[
            "profile_pic"
        ]
        widgets={
            "profile_pic":forms.FileInput(attrs={'class':'form-control'})
        }

class CommentsForm(ModelForm):
    class Meta:
        model=Comments
        fields=[
            "comment"
        ]
        widgets={
            "comment":forms.TextInput(attrs={'class':'form-control'})
        }





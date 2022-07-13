from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from blogapp.forms import UserRegForm,LoginForm,UserProfileForm,PasswordResetForm,BlogForm,ProfilePicUpdateForm,CommentsForm
from django.contrib.auth import authenticate,login,logout
from blogapp.models import UserProfile,Blogs,Comments
from django.contrib import messages

# Create your views here.

class SignUpView(CreateView):
    form_class=UserRegForm
    template_name="reg.html"
    model=User
    success_url=reverse_lazy("signin")

class LoginView(FormView):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("success")
                login(request,user)
                return redirect("home")
            else:
                return render(request,self.template_name,{'form':form})


class IndexView(CreateView):
    model = Blogs
    form_class = BlogForm
    success_url = reverse_lazy("home")
    template_name="home.html"
    def form_valid(self, form):
        form.instance.author=self.request.user
        self.object = form.save ()
        messages.success(self.request,"Post has been saved")
        return super ().form_valid (form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        blogs=Blogs.objects.all().order_by("-posted_date")
        context["blogs"]=blogs
        comment_form=CommentsForm()
        context["comment_form"]=comment_form
        return context




class UserProfileView(CreateView):
    model = UserProfile
    template_name = "addprofile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success (self.request, "profile has been created")
        self.object = form.save ()
        return super ().form_valid (form)

class UserDetailView(TemplateView):

    template_name = "userdetail.html"

class PasswordResetView(FormView):
    template_name = "pwd-reset.html"
    form_class = PasswordResetForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            oldpwd=form.cleaned_data.get("old_pwd")
            newpwd=form.cleaned_data.get("new_pwd")
            confirmpwd = form.cleaned_data.get ("confirm_pwd")
            user=authenticate(request,username=request.user.username,password=oldpwd)
            if user:
                user.set_password(confirmpwd)
                user.save()
                messages.success(request,"Password changed successfully")
                return redirect("signin")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{'form':form})

class ProfileUpdateView(UpdateView):
    form_class = UserProfileForm
    template_name = "update-user.html"
    model = UserProfile
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"
    def form_valid(self, form):
        messages.success(self.request,"Profile hasbeen Updated")
        self.object = form.save ()
        return super ().form_valid (form)

class ProfilePicUpdateView(UpdateView):
    form_class = ProfilePicUpdateForm
    template_name = "propic-update.html"
    model = UserProfile
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"
    def form_valid(self, form):
        messages.success(self.request,"Profile Pic hasbeen Updated")
        self.object = form.save ()
        return super ().form_valid (form)

def add_comment(request,*args,**kwargs):
    if request.method=='POST':

        blog_id=kwargs.get('post_id')
        blog=Blogs.objects.get(id=blog_id)
        user=request.user
        comment=request.POST.get('comment')
        Comments.objects.create(blog=blog,comment=comment,user=user)
        messages.success(request,"comment has been posted")
        return redirect('home')

def add_like(request,*args,**kwargs):
    blog_id=kwargs.get('post_id')
    blog = Blogs.objects.get (id=blog_id)
    user=request.user
    blog.liked_by.add(request.user)
    blog.save()
    return redirect('home')








def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")






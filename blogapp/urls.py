from django.urls import path
from blogapp import views

urlpatterns=[
path('accounts/signup',views.SignUpView.as_view(),name="signup"),
    path('accounts/login',views.LoginView.as_view(),name="signin"),
    path('home',views.IndexView.as_view(),name="home"),
    path('users/profile/add',views.UserProfileView.as_view(),name='add-profile'),
    path('users/profile/details',views.UserDetailView.as_view(),name='details'),
    path('users/password/change',views.PasswordResetView.as_view(),name='pwd-reset'),
    path('users/profile/change/<int:user_id>',views.ProfileUpdateView.as_view(),name="profile-update"),
    path('users/pic/change<int:user_id>',views.ProfilePicUpdateView.as_view(),name="pic-change"),
    path('post/comment/<int:post_id>',views.add_comment,name='add-comment'),
    path('post/like/add/<int:post_id>',views.add_like,name='add-like'),
    path('accounts/logout',views.sign_out,name="sign-out")
]
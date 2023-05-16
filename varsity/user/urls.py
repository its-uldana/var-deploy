from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView
from user.views import UserProfileView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
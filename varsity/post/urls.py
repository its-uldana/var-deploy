from django.urls import path, include
from post.views import ListCreateCompanyAPIView, CompanyAPIView, ListCreatePostAPIView, PostAPIView
from .view import show_internships

urlpatterns = [
    path('companies/', show_internships),
    path('companies/<int:pk>/', CompanyAPIView.as_view()),
    path('posts/', ListCreatePostAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view()),
]
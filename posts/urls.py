# pages/urls.py
from django.urls import path

from .views import HomePageView, PostDetailView, PostCreateView

urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]

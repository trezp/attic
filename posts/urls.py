# pages/urls.py
from django.urls import path

from .views import HomePageView, PostDetailView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]

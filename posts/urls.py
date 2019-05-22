# pages/urls.py
from django.urls import path

from .views import (
    HomePageView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
)

urlpatterns = [
    path('post/<int:pk>/edit',
         PostUpdateView.as_view(), name='post_edit'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]

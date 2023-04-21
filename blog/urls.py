from django.urls import path
from .views import post

app_name = 'blog'


urlpatterns = [
    path('posts/<slug:slug>', post.DetailView.as_view(), name='post-detail'),
]

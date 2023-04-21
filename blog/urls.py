from django.urls import path
from .views import category, post, tag

app_name = 'blog'


urlpatterns = [
    path('categories/<slug:slug>', category.index, name='category-index'),
    path('posts/<slug:slug>', post.DetailView.as_view(), name='post-detail'),
    path('tags/<slug:slug>', tag.index, name='tag-index'),
]

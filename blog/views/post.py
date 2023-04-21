from django.views import generic


from ..models import Post


# Generic detail view to show single post.
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post/detail.html'

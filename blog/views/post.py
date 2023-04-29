from django.core.paginator import Paginator
from django.views import generic


from ..models import Post


# List posts on homepage.
def posts_for_homepage(request):
    post_list = Post.objects.filter(status=1).order_by('-created_at')
    paginator = Paginator(post_list, 4)  # Show 4 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

# Generic detail view to show single post.
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post/detail.html'

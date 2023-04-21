from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


from ..models import Tag


# List all posts for a tag.
def index(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    post_list = tag.posts.filter(status=1).order_by('-created_at')
    paginator = Paginator(post_list, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'taxonomy': tag, 'page_obj': page_obj}
    return render(request, 'blog/taxonomy/index.html', context)

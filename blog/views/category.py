from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


from ..models import Category


# List all posts for a category.
def index(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = category.posts.filter(status=1).order_by('-created_at')
    paginator = Paginator(post_list, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'taxonomy': category, 'page_obj': page_obj}
    return render(request, 'blog/taxonomy/index.html', context)

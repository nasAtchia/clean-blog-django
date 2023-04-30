from django.shortcuts import render


from blog.views.post import posts_for_homepage


def index(request):
    page_obj = posts_for_homepage(request)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context)

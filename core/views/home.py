from django.shortcuts import render


def index(request):
    # Send variables to template.
    context = {}

    return render(request, 'core/home/index.html', context)

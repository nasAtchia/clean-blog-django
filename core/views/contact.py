from django.shortcuts import render


from ..forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'core/contact.html', context)

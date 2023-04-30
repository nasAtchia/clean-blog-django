from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


from ..forms import ContactForm
from core import signals


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = {
               'email': form.cleaned_data['email'],
               'message': form.cleaned_data['message'],
               'name': form.cleaned_data['name'],
               'phone': form.cleaned_data['phone'],
               'subject': form.cleaned_data['subject'],
            }

            signals.contact_request.send(sender='new_contact_request', contact=contact)

            messages.success(
                request,
                _('Thank you for your contact request. A member of our team will contact you within 24 hours.')
            )

            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'core/contact.html', context)

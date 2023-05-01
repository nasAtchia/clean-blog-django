from django.conf import settings
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


from core import signals


@receiver(signals.contact_request)
def send_contact_request_email_to_admin(sender, contact, **kwargs):
    subject = settings.APP_NAME + ': ' + contact['subject']
    to = [settings.CONTACT_TO_EMAIL]
    from_email = contact['email']
    reply_to = [contact['email']]
    context = {
        'contact': contact,
    }
    message = render_to_string('core/mail/contact_notification.html', context)
    email = EmailMessage(subject, message, from_email=from_email, to=to, reply_to=reply_to)
    email.content_subtype = 'html'
    email.send()


@receiver(signals.contact_request)
def send_thank_you_email_to_sender(sender, contact, **kwargs):
    subject = settings.APP_NAME + ': ' + _('Thank you for contacting us')
    to = [contact['email']]
    from_email = settings.DEFAULT_FROM_EMAIL
    context = {
        'contact': contact,
    }
    message = render_to_string('core/mail/contact_confirmation.html', context)
    email = EmailMessage(subject, message, from_email=from_email, to=to)
    email.content_subtype = 'html'
    email.send()

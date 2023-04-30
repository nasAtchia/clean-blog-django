from django.dispatch import receiver


from core import signals


@receiver(signals.contact_request)
def send_contact_request_email_to_admin(sender, contact, **kwargs):
    # Todo: send email to admin
    print('Email to admin')


@receiver(signals.contact_request)
def send_thank_you_email_to_sender(sender, contact, **kwargs):
    # Todo: send email to sender
    print('Email to sender')

from django.conf import settings


def global_variables(request):
    return {
        'APP_NAME': settings.APP_NAME,
    }

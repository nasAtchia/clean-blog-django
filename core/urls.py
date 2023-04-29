from django.urls import path


from .views.about import AboutView
from .views import contact

app_name = 'core'


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact.index, name='contact'),
]

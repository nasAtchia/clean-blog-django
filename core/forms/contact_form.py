from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Name')}
    ))
    email = forms.EmailField(label=_('Email Address'), label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': _('Email Address')}
    ))
    phone = forms.CharField(label=_('Phone Number'), label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Phone Number'), 'type': 'tel'}
    ))
    subject = forms.CharField(label=_('Subject'), label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Subject')}
    ))
    message = forms.CharField(label='Message', label_suffix='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': _('Message'), 'rows': 5}
    ))

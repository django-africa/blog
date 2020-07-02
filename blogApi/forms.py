from django import forms
from .models import ClientRegistration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = ClientRegistration
        fields = ('name', 'schema_name', 'domain_url')

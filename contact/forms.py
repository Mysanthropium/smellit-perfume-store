from django import forms
from .models import ContactEmail


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        fields = ['email_address', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email_address': 'Email',
            'message': 'Message'
        }

        self.fields['email_address'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

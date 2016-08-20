from django import forms
from landing.models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'message']
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email','required': True}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter you message', 'rows': 5,'required': True,'data-validation-required-message':"Please enter a message."}),
        }

    
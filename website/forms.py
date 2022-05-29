from django import forms

# creating a contact form
class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField() # checks for a valid email address
    message = forms.CharField(widget=forms.Textarea)
        
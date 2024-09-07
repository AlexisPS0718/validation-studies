from django import forms

class contact_form(forms.Form):
  name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
  email = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
    'placeholder': 'Email', 
    'type': 'email'
    }))
  subject = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
  message = forms.CharField(widget=forms.Textarea(attrs={
    'placeholder': 'Message',
    'rows': 5
    }))

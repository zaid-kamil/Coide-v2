from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               max_length=30,
                               widget=forms.TextInput(attrs={
                                   "class": "input-lg form-control",
                                   'name': 'username'
                               }))
    password = forms.CharField(label="password",
                               max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   "class": "input-lg form-control",
                                   "name": "password"
                               }))


class DocumentForm(forms.Form):
    docfile = forms.FileField(label="select a file", help_text="upto 25MB")


from django import forms
from django.contrib.auth.models import User
from django.contrib import auth


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Usuario'},render_value=False)))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Password'},render_value=False)))

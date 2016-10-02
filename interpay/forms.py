__author__ = 'Farzane'

from interpay.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', '')
        confirm_password = self.cleaned_data.get("confirm_password", '')
        if password != confirm_password:
            print("error")
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'email']

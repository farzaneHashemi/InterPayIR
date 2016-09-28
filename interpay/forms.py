__author__ = 'Farzane'

from interpay.models import *
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    # user_form
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', '')
        confirm_password = self.cleaned_data.get("confirm_password", '')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password


class RegistrationForm(forms.ModelForm):
    # profile_form
    class Meta:
        model = UserProfile
        exclude = ['user', 'picture']

    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}))
    # password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    # confirm_password = forms.CharField(required=True,
    #                                    widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    # def __init__(self, *args, **kw):
    #     super(RegistrationForm, self).__init__(*args, **kw)

        # def clean_password(self):
        #     data = self.cleaned_data.get('password', '')
        #     if len(data) < 8:
        #         raise forms.ValidationError("password too short. must be at least 8 characters.")
        #     return data
        #
        # def clean_confirm_password(self):
        #     password = self.cleaned_data.get('password', '')
        #     confirm_password = self.cleaned_data.get("confirm_password", '')
        #     if password != confirm_password:
        #         raise forms.ValidationError("passwords do not match.")
        #     return confirm_password

        # def clean_email(self):
        #     try:
        #         validate_email(self.cleaned_data.get("email", ''))
        #     except ValidationError:
        #         raise forms.ValidationError("oops! wrong email.")
        #
        #     return self.cleaned_data.get("email")
        #
        # def save(self, commit=True):
        #     profile = super(RegistrationForm, self).save(commit=False)
        #     user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'],
        #                                     email=self.cleaned_data['email'])
        #     user.save()
        #     profile.user = user
        #     profile.save()
        #     return profile

from django.core.mail import send_mail
from django.template import Context, Template
from InterPayIR.settings import MEDIA_ROOT
from interpay.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

__author__ = 'Farzane'


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
            raise forms.ValidationError("Passwords do not match!")
        return confirm_password

    # def send_email(self, datas):
    #     link = "http://127.0.0.1:8000//activate/" + datas['activation_key']
    #     c = Context({'activation_link': link, 'username': datas['username']})
    #     f = open(MEDIA_ROOT + datas['email_path'], 'r')
    #     t = Template(f.read())
    #     f.close()
    #     message = t.render(c)
    #     # print unicode(message).encode('utf8')
    #     send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [datas['email']],
    #               fail_silently=False)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'email']

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from InterPayIR import settings
from django.utils.translation import get_language

# request.session['lang'] = 'en'

def switch_lang(request):
    request.session['lang'] = 'fa'
    return True


def change_lang(request):
    return HttpResponse()


def home(request):
    print("request.lang", get_language())
    print("settings.LANGUAGE_CODE", settings.LANGUAGE_CODE)
    return render(request, "home.html")


def wallets(request):
    return render(request, "wallets.html")


def trans_history(request):
    return render(request, "trans_history.html")


def reports(request):
    return render(request, "reports.html")

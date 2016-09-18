from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def wallets(request):
    return render(request, "wallets.html")


def trans_history(request):
    return render(request, "trans_history.html")


def reports(request):
    return render(request, "reports.html")

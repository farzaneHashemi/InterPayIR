from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response


def home(request):
    return render(request, "home.html")


def wallets(request):
    print("wallets called")
    v = request.path
    print(v[6:])
    print(v)
    return render(request, "wallets.html")


def trans_history(request):
    return render(request, "trans_history.html")


def reports(request):
    return render(request, "reports.html")

def to_en(request):
    url = request.path
    p = url[6:0]
    en_url = "http://127.0.0.1:8000/" + p
    print(url)
    print(p)
    print(en_url)
    return HttpResponseRedirect(en_url)
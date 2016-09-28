from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from interpay.forms import UserForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext


def main_page(request):
    return render(request, 'main_page.html')


def home(request):
    return render(request, "home.html")


def wallets(request):
    return render(request, "wallets.html")


def trans_history(request):
    return render(request, "trans_history.html")


def reports(request):
    return render(request, "reports.html")


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        registration_form = RegistrationForm(data=request.POST)

        if user_form.is_valid() and registration_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = user_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, registration_form.errors

    else:
        user_form = UserForm()
        registration_form = RegistrationForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': registration_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user, None)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', {})

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from interpay.forms import RegistrationForm, UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def main_page(request):
    if request.user.is_authenticated():
        return home(request)
    return render(request, 'main_page.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        registration_form = RegistrationForm(data=request.POST)

        if user_form.is_valid() and registration_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = registration_form.save(commit=False)
            profile.email = user_form.cleaned_data['email']
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'], )
            login(request, new_user)

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
        print(username)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user, None)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def home(request):
    return render(request, "home.html")


@login_required()
def wallets(request):
    return render(request, "wallets.html")


@login_required()
def trans_history(request):
    return render(request, "trans_history.html")


@login_required()
def reports(request):
    return render(request, "reports.html")

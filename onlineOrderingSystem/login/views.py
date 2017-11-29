from django.shortcuts import render
from .models import Account
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'login/login.html', {})

        elif request.method == 'POST':
            username = request.POST.get("usernameInput", "")
            password = request.POST.get("passwordInput", "")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('login:index'))
            else:
                return render(request, 'login/login.html', {
                    'error': True,
                })

    else:
        return HttpResponseRedirect(reverse('login:index'))


def userLogout(request):
    logout(request)
    print("imma reverse")
    return HttpResponseRedirect(reverse('login:index'))


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tickets:manager_view'))

    else:
        return HttpResponseRedirect(reverse('login:login'))

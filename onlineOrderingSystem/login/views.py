from django.shortcuts import render
from .models import Account
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def userLogin(request):
    if not request.user.is_authenticated():
        if request.method == 'GET':
            return render(request, 'login/login.html', {})

        elif request.method == 'POST':
            username = request.POST.get("usernameInput", "")
            password = request.POST.get("passwordInput", "")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("<h1>Login.</h1>")
            else:
                return render(request, 'login/login.html', {
                    'error': True,
                })

    else:
        return HttpResponse("<h1>Already logged in.</h1>")


def userLogout(request):
    logout(request)
    return HttpResponse("<h1>logout.</h1>")
from django.shortcuts import render
from .models import Account
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    if request.user.is_authenticated:
        return render(request, 'register/register.html', {})

    else:
        return HttpResponseRedirect(reverse('login:login'))


# def create_account(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             InputName = request.POST.get("InputName", "")
#             InputLastName = request.POST.get("InputLastName", "")
#             InputEmail = request.POST.get("InputEmail", "")
#             InputPassword = request.POST.get("InputPassword", "")
#
#             account = Account()
#             account.firstname = InputName
#             account.lastname = InputLastName
#             account.email = InputEmail
#             account.password = InputPassword
#
#             account.save()
#
#         else:
#             return HttpResponseRedirect(reverse('login:index'))
#
#     else:
#         return HttpResponseRedirect(reverse('login:login'))

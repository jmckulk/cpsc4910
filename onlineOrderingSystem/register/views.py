from django.shortcuts import render
from .models import Account
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def register_user(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Manager'):
        if request.method == 'GET':
            return render(request, 'register/register.html', {})

        elif request.method == 'POST':
            InputUsername = request.POST.get("UserName", "")
            InputName = request.POST.get("InputName", "")
            InputLastName = request.POST.get("InputLastName", "")
            InputEmail = request.POST.get("InputEmail", "")
            InputPassword = request.POST.get("InputPassword", "")
            ConfirmPassword = request.POST.get("ConfirmPassword", "")

            if InputName == "":
                return render(request, 'register/register.html', {
                    'error':"Please enter a first name for this user!"
                })
            elif InputLastName == "":
                return render(request, 'register/register.html', {
                    'error': "Please enter a last name for this user!"
                })
            elif InputEmail == "":
                return render(request, 'register/register.html', {
                    'error': "Please enter an email for this user!"
                })
            elif InputPassword == "":
                return render(request, 'register/register.html', {
                    'error': "Please enter a password for this user!"
                })
            elif not InputPassword == ConfirmPassword:
                return render(request, 'register/register.html', {
                    'error':'Passwords do not match!'
                })
            else:
                user = User.objects.create_user(username=InputUsername,
                                                email=InputEmail,
                                                password=InputPassword)
                user.first_name = InputName
                user.last_name = InputLastName
                user.save()

                if not request.POST.get("isManager", "") == "":
                    my_group = Group.objects.get(name='Manager')
                    my_group.user_set.add(user)
                else:
                    my_group = Group.objects.get(name='Kitchen Staff')
                    my_group.user_set.add(user)

                return render(request, 'register/register.html', {
                    'success': True,
                })

        else:
            return HttpResponseRedirect(reverse('login:index'))

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

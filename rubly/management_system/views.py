from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# from .models import User
# from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in ' + username)
            return redirect('Dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Login')
    else:
        return render(request, 'auth-login-basic.html')


# Login Module
# def Login(request):
#     if request.method == "POST":
#        if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         check_user = User.objects.filter(username=username)
#         pwd = User.objects.filter(password=password)
#         if check_user:
#             if pwd:
#                 return redirect('Dashboard')
#         else:
#             return redirect('Login')
#     # user =User.objects.get_or_create()
#     return render(request, 'auth-login-basic.html')


# Dashboard Module
@login_required(login_url="/login/")
def Dashboard(request):
    # context= {}
    return render(request, 'dashboard.html')

# def Dashboard(request):
#  return render(request,'capex-order.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')

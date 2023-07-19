from django.shortcuts import redirect, render
from .models import User


# Login Module
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username)
        pwd = User.objects.filter(password=password)
        if user:
            if pwd:
                return redirect('Dashboard')
        else:
            return redirect('Login')
    return render(request, 'auth-login-basic.html')


# Dashboard Module
def Dashboard(request): 
    return render(request, 'dashboard.html')

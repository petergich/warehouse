from django.shortcuts import redirect, render
from .models import user

# Login Module.
def Login(request):
 if  request.method == "POST":
  username = request.POST.get('username')
  password = request.POST.get('password')

  data = user(username=username,password=password) 
  data.save()
  return redirect("Dashboard")
 return render(request,'auth-login-basic.html')


def Dashboard(request):
 return render(request,'dashboard.html')
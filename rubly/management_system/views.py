from django.shortcuts import render
from .models import user
# Login Module.
def Login(request):
 if  request.method == "POST":
  username = request.post['username']
  password = request.post['password']

  data = user(username=username,password=password) 
  return render('dashboard.html',request)
 return render(request,'login.html')

def Dashboard(request):
 return render()
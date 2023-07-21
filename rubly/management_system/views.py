

from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import *

from django.shortcuts import render,redirect
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse




from django.contrib.auth.decorators import login_required


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




# Dashboard Module
@login_required(login_url="/login/")
def Dashboard(request):
    try:
        skus = SKUs.objects.all()    
    except SKUs.DoesNotExist:
        skus = get_object_or_404
    # sku = {{'Description':'router microtic'},{'Type':'Gateway'},{'Quantity',10},{'Price': 3000}}
    for sku in skus:
            print(sku)
    return render(request, 'dashboard.html',{'skus': skus})

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')


 
# Dashboard-date Module
class dashboard(View):

    def post(self, request):
        data = json.loads(request.body) 
        date = data['date']
        print(date)
        return JsonResponse({'date': data['date']})




# Stock release module
class CapexOut(View):
    def post(self, request):
        data = json.loads(request.body)
#Stock release module
class CapexOut(View):
     def post(self, request):
        data = json.loads(request.body) 
        search = data['sku']
        print(search)
        return JsonResponse({'search': data['sku']})


 
 

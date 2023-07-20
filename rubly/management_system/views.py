from django.shortcuts import render,redirect
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required


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
# def Dashboard(request): 
#     return render(request, 'dashboard.html')

def Dashboard(request):
 return render(request,'capex-order.html')

 
# Dashboard Module
@login_required(login_url='Login')
def Dashboard(request):
    return render(request,'dashboard.html')

# Dashboard-date Module
class dashboard(View):

    def post(self, request):
        data = json.loads(request.body) 
        date = data['date']
        print(date)
        return JsonResponse({'date': data['date']})


#Stock release module
class CapexOut(View):
     def post(self, request):
        data = json.loads(request.body) 
        search = data['sku']
        print(search)
        return JsonResponse({'search': data['sku']})

 
 


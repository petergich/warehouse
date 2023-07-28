

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import *

from django.shortcuts import render,redirect
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
import os
import time
import datetime



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
    
    if 'search' in request.GET:
        id = request.GET['search']
        obj = SKUs.objects.filter(id=id)
        # print (obj)
        return render(request, 'dashboard.html',{'skus': obj}) 
    if 'search1' in request.GET:
        id = request.GET['search1']
        obj = SKUs.objects.filter(Description__contains= id)
        print (obj)
        return render(request, 'dashboard.html',{'skus': obj}) 
    
    skus = SKUs.objects.all()
    return render(request, 'dashboard.html',{'skus': skus})

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')
def selected(request):
    # redirect('Dashboard')
    if "array" in request.GET:
        if 'capex'in request.GET:
            capex=request.GET['capex']
            string=request.GET['array']
            array = string.split(',')
            mycapex=Capex.objects.get(capex_no=capex)
            if(mycapex):
                for i in range(0,len(array),2):
                    itemid=array[i]
                    amount=array[i+1]
                    instance=SKUs.objects.get(id=itemid)
                    instance.Quantity=int(instance.Quantity)-int(amount)
                    instance.save()
                now = datetime.datetime.now()

                # Convert the datetime object to a string
                current_date = now.strftime('%Y_%m_%d_%H_%M_%S')  # Generate a date-only timestamp
                directory = "transactions"
                # Create the directory if it doesn't exist
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file_name = os.path.join("transactions", f"_{capex}_{current_date}.json")  # Create a file path within the "data" directory

                with open(file_name, 'w') as file:
                    print("Success")
                    json.dump(string, file)
                return JsonResponse({'date': "Successfull"})
            else:
                return JsonResponse({'date': "Capex not found"})
        elif 'capex' not in request.GET:
            string=request.GET['array']
            array = string.split(',')
            for i in range(0,len(array),2):
                    itemid=array[i]
                    amount=array[i+1]
                    instance=SKUs.objects.get(id=itemid)
                    instance.Quantity=instance.Quantity-int(amount)
                    instance.save()
            now = datetime.datetime.now()
            current_date = now.strftime('%Y_%m_%d_%H_%M_%S')  # Generate a date-only timestamp
            directory = "transactions"
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_name = os.path.join("transactions", f"_Null_{current_date}.json")  # Create a file path within the "data" directory

            with open(file_name, 'w') as file:
                print("Success")
                json.dump(string, file)
            return JsonResponse({'date': "Successfull"})
    


 
# Dashboard-date Module


def dashboardstock(request):
    if request.method=="GET":
        if 'openingdate' in request.GET:

            respdict=[]
            date=request.GET['openingdate']
            search = 'opening' + date + '.json'
            file_path = os.path.join("data", f"{search}")
            with open(file_path, 'r') as file:
                datav = json.load(file)
                for jsonval in datav :
                    sublist=[]
                    for i in range(len(jsonval)):
                        if i==0:
                            sublist.append({"Description":jsonval[i]})
                        if i==1:
                            sublist.append({"Price":jsonval[i]})
                        if i==2:
                            sublist.append({"Packaging":jsonval[i]})
                        if i==3:
                            sublist.append({"Quantity":jsonval[i]})
                        if i==4:
                            sublist.append({"Purchase_order":jsonval[i]})
                    respdict.append(sublist)
                text="Opening Stock For:"+str(date)
            return render(request, 'dashboard.html',{'respdict': respdict,"type":text})
        elif 'closingdate' in request.GET:
            respdict=[]
            date=request.GET['closingdate']
            search = 'closing' + date + '.json'
            file_path = os.path.join("data", f"{search}")
            with open(file_path, 'r') as file:
                datav = json.load(file)
                for jsonval in datav :
                    sublist=[]
                    for i in range(len(jsonval)):
                        if i==0:
                            sublist.append({"Description":jsonval[i]})
                        if i==1:
                            sublist.append({"Price":jsonval[i]})
                        if i==2:
                            sublist.append({"Packaging":jsonval[i]})
                        if i==3:
                            sublist.append({"Quantity":jsonval[i]})
                        if i==4:
                            sublist.append({"Purchase_order":jsonval[i]})
                    respdict.append(sublist)
            text="Closing Stock for:"+str(date)
            return render(request, 'dashboard.html',{'respdict': respdict,"type":text})





#Stock release module
class CapexOut(View):
     def post(self, request):
        data = json.loads(request.body) 
        search = data['sku']
        skus = SKUs.objects.filter(Description__contains= search).values()
        return JsonResponse({'search': list(skus)})
 
    


 
 

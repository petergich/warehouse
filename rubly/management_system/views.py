from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.shortcuts import render, redirect
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
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Login')
    else:
        return render(request, 'auth-login-basic.html')


# Dashboard Module
@login_required(login_url="/login/")
def Dashboard(request):
    if  "warehouse" in request.GET and "type" in request.GET:
        warehouse_name=request.GET['warehouse']
        # des=Description.objects.filter(Type=request.POST['type']).id
        warehouse=Warehouse.objects.get(name=warehouse_name).id
        chekin=Checkin.objects.filter(description__Type =request.GET['type'],Warehouse=warehouse)
        descriptions=[]
        for des in chekin:
            chec=[]
            quantity=0
            for che in chekin:
                if che.description.Description==des.description.Description:
                    if che.Quantity!=0 and che.Purchase_Order.purchase_ID!="Null":
                            chec.append({"description":che.description.Description,"quantity":che.Quantity, "purchase_order":che.Purchase_Order.purchase_ID,"price":che.price})
                    quantity+=che.Quantity
            descriptions.append({"description":des.description.Description,"quantity":quantity,"pacaging":des.description.Packaging,"chekins":chec})
            print(chec)
        filtered=[]
        for instance in descriptions:
            if instance not in filtered:
                filtered.append(instance)
        return JsonResponse({"descriptions":filtered})
    else:
        description = Description.objects.all()
        warehouses=Warehouse.objects.all()
        chekins=Checkin.objects.all()
        types=list(set(Description.objects.values_list('Type', flat=True)))
        context={'Description': description,"warehouses":warehouses,"chekins":chekins,"types":types}
        
        return render(request, 'dashboard.html', context)


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('Login')
    return redirect('Login')


def selected(request):    
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
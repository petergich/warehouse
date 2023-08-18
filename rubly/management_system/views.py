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
from django.core.serializers import serialize
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
@login_required(login_url="Login")
def Dashboard(request):
        project_types=Project_Type.objects.all()
        clients=Client.objects.all()
        
        list_clients=[]
        for client in clients:
            projects=[]
            for project in project_types:
                if project.client.name==client.name:
                    Project_region = Project.objects.filter(project_type__name=project.name,project_type__client__name=client.name)
                    projects.append({"project_type":project,"project_region":Project_region})

            list_clients.append({
                "client":client,
                "projects":projects,
            })
        Pur=Purchase_Order.objects.all()
        POs=[]
        for p in Pur:
            if p.purchase_ID not in POs:
                POs.append(p.purchase_ID)
        return render(request, 'dashboard.html',{"list_clients":list_clients,"purchase_orders":POs})
@login_required(login_url="Login")
def issue(request):
    clients=Client.objects.all()
    project_types=Project_Type.objects.all()
    objects=[]
    for clien in clients:
        project=[]
        for pro in project_types:
            if pro.client.name==clien.name:
                project.append(pro.name)
        objects.append({"clients":clien,"projects":project})
    return render(request,"issue.html",{"objects":objects})
@login_required(login_url="Login")
def check(request):
    if request.GET['client']:
        client=request.GET['client']
        proje=request.GET['project']
        project=Project_Type.objects.get(client__name=client,name=proje)
        #get all goods where the project type is the one selected
        goods=Goods_received.objects.filter(Project_Type=project)
        des=[]
        #looping through the goods and adding their description in the list
        for good in goods:
            if good.description not in des:
                des.append(good.description)
        #loop on every descriptio appending the description instance and all the goods associated with it
        objects=[]
        for description in des:
            #loop on every good testing if the good.description matches the one for our current loop then adding it in the list
            Quantity=0
            for good in goods:
                if good.description==description:
                    Quantity+=good.remaining
            objects.append({"description":description,"quantity":Quantity})
        if objects==[]:
            message="No goods for selected type"
        else:
            message="found"
    return JsonResponse(message,safe=False)
@login_required(login_url="Login")
def projectGoods(request):
    if request.GET['client']:
        client=request.GET['client']
        proje=request.GET['project']
        project=Project_Type.objects.get(client__name=client,name=proje)
        #get all goods where the project type is the one selected
        goods=Goods_received.objects.filter(Project_Type=project)
        des=[]
        #looping through the goods and adding their description in the list
        for good in goods:
            if good.description not in des:
                des.append(good.description)
        #loop on every descriptio appending the description instance and all the goods associated with it
        objects=[]
        for description in des:
            instan=Description.objects.get(Description=description)
            #loop on every good testing if the good.description matches the one for our current loop then adding it in the list
            Quantity=0
            for good in goods:
                if good.description==description:
                    Quantity+=good.remaining
            objects.append({"description":instan,"quantity":Quantity})
        return render(request,"projectGoods.html",{"objects":objects,"client":client,"project":proje})
@login_required(login_url="Login")
def good(request):
    if request.GET['description']:
        des=request.GET['description']
        client=request.GET['client']
        proj=request.GET['project']
        goods=Goods_received.objects.filter(Project_Type__name=proj,Project_Type__client__name=client,description__Description=des,remaining__gt=0)
        desc=Description.objects.get(Description=des)
        Quantity=0
        for good in goods:
                Quantity+=good.remaining
        goods_json = []
        for good in goods:
            goods_json.append({"po":good.Purchase_Order.purchase_ID,"quantity":good.remaining})
        return render(request,"good.html",{"goods":goods,"description":desc,"quantity":Quantity,"client":client,"project":proj,"goods_json":goods_json})
@login_required(login_url="Login")
def checkout(request):
    if request.GET['company']:
        good=Goods_received.objects.get(Purchase_Order__purchase_ID=request.GET['po'],description__Description=request.GET['desc'],Project_Type__name=request.GET['project'],Project_Type__client__name=request.GET['client'])
        
@login_required(login_url="Login")
def capex(request):    
    return render(request,'capex.html')
def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('Login')
    return redirect('Login')

# Dashboard-date Module
@login_required(login_url="Login")
def stock(request):
    if request.GET['selected']=="all":
         clients=Client.objects.all()
         recieved=Goods_received.objects.all()
         return render(request,"stock.html")
    else:
        clients=Client.objects.all()

        return render(request,"stock.html")
@login_required(login_url="Login")
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
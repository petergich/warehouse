from django.urls import path,include 

from . import views

urlpatterns = [
    path("",views.Login,name="Login"),
    path("dashboard",views.Dashboard,name="Dashboard"),
]
from django.urls import path
from . import views

url_patterns = [
    path("",views.Login,name="Login"),
    path("dashboard",views.Dashboard,name="Dashboard"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("",views.Login,name="Login"),
    path("dashboard",views.Dashboard,name="Dashboard"),
]
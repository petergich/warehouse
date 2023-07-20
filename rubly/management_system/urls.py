from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login, name="Login"),
    path("dashboard", views.Dashboard, name="Dashboard"),
    path('logout', views.Logout, name='Logout')
]

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("login/",views.Login,name="Login"),
    path("dashboard",views.Dashboard,name="Dashboard"),
    path('dashboardstock',csrf_exempt(views.dashboard.as_view()),name = 'dashboardstock'),
    path('capexout',csrf_exempt(views.CapexOut.as_view()),name = 'capexout'),
]

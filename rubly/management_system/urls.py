from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("",views.Login,name="Login"),
    path("dashboard",views.Dashboard,name="dashboard"),
    path('dashboardstock/',views.dashboardstock,name = 'dashboardstock'),
    path('logout',views.Logout,name='Logout'),    
]





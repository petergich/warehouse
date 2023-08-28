from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path("",views.Login,name="Login"),
    path('current-stocks-list/', views.current_stocks_list, name='current-stocks-list'),
    path("dashboard",views.Dashboard,name="dashboard"),
    path("issue",views.issue,name="Issue"),
    path("capex",views.capex,name="Capex"),
    path("good",views.good,name="good"),
    path("selected",views.projectGoods,name="selected"),
    path("check",views.check,name="Check"),
    path("checkout",views.checkout,name="checkout"),
    path("postock",views.po_stock,name="postock"),
    path('logout',views.Logout,name='Logout'),    
]





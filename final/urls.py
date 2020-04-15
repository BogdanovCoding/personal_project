from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome', views.welcome, name='welcome'),
    path('stocks', views.stocks, name='stocks'),
    path('forex', views.forex, name='forex'),
    path('crud', views.crud, name='crud'),
]



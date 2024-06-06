from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('fazer_pedido/', views.fazer_pedido, name='fazer_pedido'), 
    path('login/', views.loginUser, name="loginUser"),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
   path('registro/', views.registro, name='registro'),
    path('pagina_de_sucesso/', views.pagina_de_sucesso, name='pagina_de_sucesso'),
    path('meus_pedidos/', views.meus_pedidos, name='meus_pedidos'),
]

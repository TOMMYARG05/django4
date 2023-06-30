"""
URL configuration for misitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.peli,name="peli"),
    path('dracula/',views.dracula,name="dracula"),
    path('elc/',views.elc, name="esperandolacarroza"),
    path('ipf/', views.ipf, name="Iluminados por el fuego"),
    path('psvl/', views.psvl, name="Papa se volvio loco"),
    path('lbmldm/', views.lbmldm, name="Los Bañeros Mas Locos Del Mundo"),
    path('st/', views.st,name="Starship Troopers"),
    path('login/', views.login, name="login"),
    path('addnew/',views.addnew , name="registro de usuario"),
    path('edit/<int:id',views.edit, name="editar"),
    path('destroy/<int:id',views.destroy,name="eliminar"),
    path('update/<int:id',views.update,name="actualizar"),
    path('mostrar/',views.mostrar,name="mostrar"),
]

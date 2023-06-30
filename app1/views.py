from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm

 
# Create your views here.
def dracula(request): 
    return render(request, 'dracula.html')

def elc(request):
    return render(request, 'EsperandolaCarroza.html')

def ipf(request):
    return render(request, 'Iluminadosporelfuego.html' )

def psvl(request):
    return render(request, 'papasevolvioloco.html')

def lbmldm(request):
    return render(request,'losbañerosmaslocosdelmundo.html')

def st(request):
    return render(request, 'Starshiptroopers.html')

def peli(request):
    return render(request,'peli.html')

def mostrar(request):
    return render(request, 'mostrar.html')

def addnew(request):  
    if request.method == "POST":  
        form = UsuarioForm(request.POST)  
        if form.is_valid():  
            form.save()
            return redirect('mostrar')
    else:  
        form = UsuarioForm()  
    return render(request,'registrodeusuario.html',{'form':form})
 
def login(request):  
    usuarios = Usuario.objects.all()  
    return render(request,"login.html",{'usuarios':usuarios})  
 
def edit(request, id):  
    usuario = Usuario.objects.get(id=id)  
    return render(request,'edit.html', {'usuario':usuario})  
 
def update(request, id):  
    usuario = Usuario.objects.get(id=id)  
    form = Usuario(request.POST, instance = usuario)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'usuario': usuario})  
     
def destroy(request, id):  
    usuario = Usuario.objects.get(id=id)  
    usuario.delete()  
    return redirect("/") 
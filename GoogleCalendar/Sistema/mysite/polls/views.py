# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import sys
import calendar
sys.path.append('/usr/bin/Python/GoogleCalendar/Listas')
sys.path.append('/usr/bin/Python/GoogleCalendar/Nodos')
from listaDoble import ClaseListaDoble
from nodosG import nodoCalendar
hola = "Ejemplo"
Lista = ClaseListaDoble()
usuarioActivo = None
user = ""
# Create your views here.
def index(request):
    hola = "Worlds"
    return HttpResponse("Hello, "+ str(hola))
def prueba(request):
	global hola
	hola += request.GET['prueba']
	return HttpResponse("Hello "+ str(hola))
@csrf_exempt
def registro(request):
    user = request.POST.get('txtUsuario')
    passw = request.POST.get('txtContrasena')
    return  HttpResponse(Lista.insertarAlFinal(nodoCalendar(str(user),str(passw))))

@csrf_exempt
def login(request):
    global usuarioActivo
    user = request.POST.get('txtUsuario')
    passw = request.POST.get('txtContrasena')
    usuarioActivo = Lista.loginNodo(str(user),str(passw))
    if usuarioActivo != None:
         return  HttpResponse(Lista.loginLista(str(user),str(passw)))
    return "Fallo"

@csrf_exempt
def registroE(request):
    print 
    fecha = str(request.POST.get('txtFecha'))
    fechaSplit = fecha.split("/")
    dia = fechaSplit[0]
    mes = fechaSplit[1]
    ano = fechaSplit[2]
    print str(dia)
    print str(calendar.month_name[int(mes)])
    nombre = str(request.POST.get('txtNombre'))
    descrip = str(request.POST.get('txtDescripcion'))
    dire = str(request.POST.get('txtDire'))
    hora = str(request.POST.get('txtHora'))
    date = str(ano) + "-" + str(mes) + "-" + str(dia) + "T"+ hora + ":00"
    print usuarioActivo.matrizD.insertarCorreo(str(calendar.month_name[int(mes)]),str(ano))
    print usuarioActivo.matrizD.insertarDatos(str(calendar.month_name[int(mes)]),str(ano),str(dia),"")
    print usuarioActivo.matrizD.insertarAvl(str(calendar.month_name[int(mes)]),str(ano),str(dia),nombre,descrip,dire,date)
    print usuarioActivo.matrizD.mostrar()
    return  HttpResponse("True")

	 
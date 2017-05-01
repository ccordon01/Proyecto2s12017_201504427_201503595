# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Files.ArbolB import Arbol
from Files.Usuarios import ListaSimple, NodoU


from rest_framework import viewsets
from rest_framework.decorators import api_view

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse

# Create your views here.
driveUsers = ListaSimple()
actualUser = None
a = None
actualTree = None

#=============================================================================================================

def first_page(request):
    if request.method == 'POST':
    	#curso_web = request.POST.get('nom')
        return HttpResponse('you are post method')
    else:
    	print 'anoher methond'
    return HttpResponseBadRequest('Request type {} is not allowed'.format(request.method))
#from . import ArbolB

def home(request):
	print 'pero que es esto tio'
	a.InsertarNuevo(a.nuevo("c1"))
	a.InsertarNuevo(a.nuevo("c2"))
	a.InsertarNuevo(a.nuevo("c3"))
	a.InsertarNuevo(a.nuevo("c4"))
	a.InsertarNuevo(a.nuevo("c5"))

	a.Imprime(a._principal)



	return HttpResponse("home page!")


'''curso_web = request.POST.get('nom')
		persona_web = request.POST.get('nom2')
		print curso_web
		print persona_web'''

def another(request):
	print 'anoder'
		
	return render(request,'Accounts/LogOn.html')

@api_view(['GET', 'POST'])
@csrf_exempt 
def prueba(request):
	print 'HA ENTRADO A PRUEBA'
	if request.POST:
		print "holi"
		curso_web = request.POST.get("nom")
		persona_web = request.POST.get("nom2")
		print curso_web
		print persona_web
		return HttpResponse("HOLIWIS")
	else:
		return HttpResponse("This is the real life, this is the fantasy :v")


#-======================POST FUNCIONALES===========================
def NewUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		driveUsers.insertar(name,password)
		return HttpResponse('Usuario Creado!')
	else:
		print 'It doesn\'t work D:'
	return HttpResponseBadRequest('Request type {} is not allowed'.format(request.method))


def VerifyUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		finduser=driveUsers.buscar(name)
		if( finduser != None):
			if(finduser.password==password):
				actualUser = finduser
				a=actualUser.root
			return HttpResponse('True')
		else:
			return HttpResponse('False')


#Para encontrar un usuario y mandar un archivo 
def FindUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		finduser=driveUsers.buscar(name)
		a=finduser.root
		actualTree = a._Carpetas
		if( finduser != None):
			return HttpResponse('Exist')
		else:
			return HttpResponse('DoesntExist')



def PrintUsers(request):
	if request.method == 'POST':
		driveUsers.imprimir()
		return HttpResponse('True')
	else:
		return HttpResponse('False')

#=====================

def CreateF(request):
	if request.method == 'POST':
		folder = request.POST.get('folder')
		actualTree.InsertarNuevo(actualTree.nuevo(folder))

def DeleteF(request):
	if request.method == 'POST':
		folder = request.POST.get('folder')
		actualTree.Eliminar(actualTree.nuevo(folder))





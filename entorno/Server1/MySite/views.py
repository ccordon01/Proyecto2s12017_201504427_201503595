# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Files.ArbolB import Arbol
from Files.Pagina import Nodo,Pagina

from Files.Usuarios import ListaSimple, NodoU

from Files.ActualSession import SessionN


from rest_framework import viewsets
from rest_framework.decorators import api_view

from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse

import json

from pprint import pprint

data = json.dumps({
  "Tags":["tag 1","tag 2","tag 3"],
	"Posts":{
		"PostZ":"lalala",
		"PostY":"Leer un JSON",
		"PostX":"Escribir un JSON"
	},
	"Blog":"http://javainutil.blogspot.com",
	"Inicio":2012,
	"Temas":"Informatica"})


# Create your views here.
driveUsers = ListaSimple()


a=Arbol()
actualUser = NodoU("None","None")#Nodo de Usuario
RootTree = Nodo("root") #este es el /account/usuario/root, el nodo principal
ActualFolder = Nodo("") #Nodo de arbol b
ActualTree = Arbol()#arbol b

s = SessionN()




#=============================================================================================================

def dinamic(request, offset):

	carpetas=offset.split("/")
	for x in xrange(len(carpetas)):
		print carpetas[x]
		pass
	return HttpResponse(offset)


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
	
	driveUsers.imprimir();
	return HttpResponse("Queso :v")


def LoginProve(request):
	if s.actualUser.user == "None":
		return render(request,'Accounts/LogOn.html')
	else:
		return HttpResponse("accounts/"+s.actualUser.Id)



@api_view(['GET', 'POST'])
@csrf_exempt 
def prueba(request):
	print 'HA ENTRADO A PRUEBA'
	if request.POST:
		print "holi"
		nombre = request.POST.get("nom")
		clave = request.POST.get("nom2")
		driveUsers.insertar(driveUsers.nuevoNodo(nombre,clave))
		s.actualUser = driveUsers.buscar(nombre)
		s.ActualFolder = s.actualUser.root
		s.ActualFolder._carpetas.InsertarNuevo(a.nuevo("carpeta1"))
		s.ActualFolder._carpetas.InsertarNuevo(a.nuevo("carpeta2"))

		return HttpResponse("Nooo way back from heell")
	else:
		return HttpResponse("This is the real life, this is the fantasy :v")




def log(request):
 
    # If we submitted the form...
    if request.method == 'POST':
 
        # Check that the test cookie worked (we set it below):
        if request.session.test_cookie_worked():
 
            # The test cookie worked, so delete it.
            request.session.delete_test_cookie()
 
            # In practice, we'd need some logic to check username/password
            # here, but since this is an example...
            return HttpResponse("You're logged in.")
 
        # The test cookie failed, so display an error message. If this
        # was a real site we'd want to display a friendlier message.
        else:
            return HttpResponse("Please enable cookies and try again.")
 
    # If we didn't post, send the test cookie along with the login form.
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')



#-======================POST FUNCIONALES===========================

#para cargar la pagina de login 
def LogIn(request):
	if s.actualUser.user == "None":
		return render(request,'Accounts/LogOn.html')
	else:

		return HttpResponse("accounts/"+actualUser.Id)

def viewSession(request):
	if s.actualUser.user == "None":
		print 'No se ha iniciado sesion'
		return HttpResponse('True')#si no se ha iniciado sesion, responder true
	else:
		print "\n el usuario actual es: "+s.actualUser.user
		try:
			s.ActualFolder = s.actualUser.root
			print s.ActualFolder.Id
			s.ActualFolder._carpetas.InsertarNuevo(s.ActualFolder._carpetas.nuevo("Por que a mi?"))
			s.ActualFolder._carpetas.InsertarNuevo(s.ActualFolder._carpetas.nuevo("Por 3 XD"))
			s.ActualFolder._carpetas.ListaCarpetas()
			print "Las carpetas actuales de esta raiz es " + s.ActualFolder._carpetas._np
			return HttpResponse(s.ActualFolder._carpetas._np)# si se ha iniciado sesion, mandar json :v
		except Exception as e:
			print '\n ERROR KK'
			raise e
			return HttpResponse("No hay nada en el folder?")


#====================================USERS=========================
#pos.. para crear un usuario no? :v
def NewUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		s.actualUser = driverUsers.nuevoNodo(name,password)#el usuario actual es el usuario creado
		#s.actualUser.root._Carpetas = Arbol()#crea un arbol para el nodo carpetas de la raiz
		s.ActualFolder = s.actualUser.root# el folder actual es la carpeta raiz del usuario
		driveUsers.insertar(s.actualUser)#insertar el usuario actual a la lista
		if not driverUsers.esta:
			return HttpResponse('Creado')
		else:
			return HttpResponse('Existe')

	else:
		print 'It doesn\'t work D:'
	return HttpResponseBadRequest('Request type {} is not allowed'.format(request.method))


#para iniciar sesion en un usario
def VerifyUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		finduser=driveUsers.buscar(name)#busca el nodo con el nombre de usuario
		#print finduser.user
		if( finduser != None): #si esta el usuario
			if(finduser.password==password):#si la contrasena es la misma
				print 'no es none'
				s.actualUser = finduser#el usuario actual es el encontrado
				s.RootTree = s.actualUser.root #rootTree es un nodo de arbol b, y se le asigna al nodo raiz esta peticion
				s.actualUser.root._carpetas.ListaCarpetas()
				#s.ActualFolder = s.actualUser.root# el folder actual es la carpeta raiz del usuario
				#s.ActualFolder._Carpetas.ListaCarpetas(s.ActualFolder._Carpetas._principal)
				retorno = s.actualUser.root._carpetas._np
				print retorno
				return HttpResponse(retorno)
			else:
				print 'contrasena incorrecta'
				return HttpResponse('False')
		else:
			return HttpResponse('False')
	else:
		return HttpResponse('Noway:v')



#Para encontrar un usuario y mandar un archivo 
def FindUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('pass')
		finduser=driveUsers.buscar(name)#el usuario encontrado es ese
		NodeA=finduser.root
		s.actualTree = NodeA._carpetas
		if( finduser != None):
			return HttpResponse('Exist')
		else:
			return HttpResponse('DoesntExist')


def PrintUsers(request):
	driveUsers.imprimir()
	return HttpResponse('True')

#=====================FOLDERS=============================

def ModifyFoler(request):
	print 'folder'

def CreateF(request,offset):
	if request.method == 'POST':
		folder = request.POST.get('folder')
		s.ActualFolder._carpetas.InsertarNuevo(a.nuevo(folder))
		if s.ActualFolder._carpetas.esta == True:
			return HttpResponse("Exist")
		else:
			return HttpResponse('No')
	else:
		return HttpResponse("no es un post")


def DeleteF(request):
	if request.method == 'POST':
		folder = request.POST.get('folder')
		s.ActualFolder._carpetas.Eliminar(a.nuevo(folder))


def buscaractual(request,offset):
	if request.method == 'POST':
		print 'se va a buscar' + request.POST.get('folder')
		folder = request.POST.get('folder')
		Node = s.ActualFolder._carpetas.NodoBus(a.nuevo(folder),s.ActualFolder._carpetas._principal)
		if(Node == None):
			return HttpResponse('false')
			print 'Se va a insertar un  nuevo folder'
		print 'Desea reemplazar?'
		return HttpResponse('true')
	else:
		print 'no existe metodo post'
		return HttpResponse('no existe')



def FindFolder(request, offset):

	print '\n\n=================se va a a findfolder'
	print offset
	carpetas=offset.split("/")
	busqueda = RootTree
	for x in xrange(len(carpetas)):
		devuelve = a.NodoBus(a.nuevo(str(carpetas[x])),busqueda._carpetas._principal)#devuelve un nodo de arbol, que es la carpeta a aencontrar
		busqueda = devuelve
	if(devuelve != None):
		print 'Se ha encontrado carpeta'
		print devuelve.Id
		s.ActualFolder = devuelve
		print devuelve.Id
		s.ActualFolder._carpetas.ListaCarpetas()
		devolucion = s.ActualFolder._carpetas._np
		print devolucion
		#devolucion = definirCarpetas()
		#dprint devolucion
		return HttpResponse(devolucion)#devuelve las listas de las carpetas
	return HttpResponse('notFound')








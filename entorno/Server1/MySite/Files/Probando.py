from Usuarios import ListaSimple
from ArbolB import Arbol
from Pagina import Nodo,Pagina

inn = ListaSimple()
class probando (object):



	def __init__ (self):
		print 'prueba'
		self.actual = None


	def menu(self):
		print "SELECCIONE OPCION"
		print '1. crear usuario \n2.ingresar a usuario \n3.Imprimir Lista '
		dato = str(raw_input())
		if dato=="1":
			self.insertarUsuario()
		elif dato =="2":
			self.buscarUsuario()
		elif dato =="3":
			inn.imprimir()
			self.menu()

		else:
			print 'opcion invalida, intente de nuevo\n'
			self.menu()


	def insertarUsuario(self):
		print 'Por favor escriba un nombre'
		name = str(raw_input())
		print ' por favor escriba password'
		password  = str(raw_input())
		print'\n===========================Creando usuario=====================\n'
		inn.insertar(name,password)
		self.menu()

	def buscarUsuario(self):
		if inn.primero == None:
			print 'No existen usuarios'
		else:			
			print 'Seleccione usuario'
			inn.imprimir()
			print ''
			user = str(raw_input())
			self.actual = inn.buscar(user)
			self.menuactual()

	def menuactual(self):
		print 'nn'

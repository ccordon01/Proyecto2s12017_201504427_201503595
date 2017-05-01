from Pagina import Nodo
from Acciones import Acciones


class ListaSimple(object):


	def __init__(self):
		print 'entro a la lista simple'
		self.primero= None
		self.con = 0
		self.ultimo= None
		self.esta = False

	def esVacio(self):
		if self.primero== None:
			return True
		else:
			return False

 	def insertar(self,user,password):
 		nuevo = NodoU(user,password)
 		nuevo.root = Nodo("root")
 		if self.primero == None:
 			self.primero = nuevo
 			self.ultimo = self.primero
 			self.con = self.con+1
 			print "se inserto" , str(self.primero.user)
			

 		else:
 			self.buscar(user)
 			if not self.esta:
	 			self.ultimo.siguiente = nuevo
	 			self.ultimo = self.ultimo.siguiente
	 			self.con = self.con+1
	 			print " se inserto "+str(self.ultimo.user)
	 			return " se inserto "+str(self.ultimo.user)
 			else:
 				return " USUARIO EXISTENTE, NO SE CREO"



 	"""def eliminar(self, user):
 		temp = self.primero
 		if self.primero ==None:
 			return "No hay usuarios"
		if no == 0:
			eliminado = self.__primero.getDato
			self.__primero= self.__primero.siguiente
			print 'se eliminio ', eliminado
			return "se elimino " + str(eliminado)
		else:
			for x in xrange(0,no-1):
				temp = temp.siguiente
				print 'se eliminio ',  temp.siguiente.dato
			temp.siguiente= temp.siguiente.siguiente

		return "indice excede el limite"""


 	def imprimir(self):
 		print '\nse entro a imprimir'

 		if self.primero==None:
 			print 'la lista esta vacia'

 			#return "lista Vacia"
 		else:
 			print 'no esta vacio'
 			a = str(self.primero.user) + ";"
 			aux = self.primero

 			while aux.siguiente!= None:
 				a=a+ str(aux.user)+";"
 				a=a+ str(aux.user)+" -> "+ str(aux.siguiente.user)+ ";"
 				print aux.user
 				aux = aux.siguiente

			print aux.user
			#return str(a)

	def buscar(self, palabra):
		print 'entro a buscar'
		cont = 0
		if self.primero ==None:
			self.esta = False
			print "Lista vacia"
			return self.primero
		else:
			aux = self.primero
			while aux!=None:
				if aux.user == palabra:
					print 'Se encontro'
					self.esta = True
					print "Se encontro "+str(palabra)+ " en el indice ",str(cont)
					return aux
					break
				else:
					aux = aux.siguiente
					cont = cont + 1
					self.esta = False
					print 'no esta'
			return None


class NodoU(object):

	def __init__(self, user,password):
		self.user = user
		self.password = password
		self.siguiente = None
		self.anterior = None
		self.root = Nodo("root")

	def getUser(self):
		return str(self.user)

	def getPassword(self):
		return str(self.password)

	def setRoot(self,root):
		self.root = root

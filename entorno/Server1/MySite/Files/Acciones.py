class Acciones(object):


	def __init__(self):
		self.primero= None
		self.con = 0
		self.ultimo= None

	def esVacio(self):
		if self.primero== None:
			return True
		else:
			return False

 	def insertar(self,descripcion,hora):
 		nuevo = NodoA(descripcion,hora)
 		if self.primero == None:
 			self.primero = nuevo
 			self.ultimo = self.primero
 			self.con = self.con+1
 		else:
 			self.ultimo.siguiente = nuevo
 			self.ultimo = self.ultimo.siguiente
 			self.con = self.con+1
 			print " se inserto "+str(self.ultimo.user)




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




class NodoA(object):

	def __init__(self, descripcion,hora):
		self.descripcion = descripcion
		self.hora = hora
		self.siguiente = None

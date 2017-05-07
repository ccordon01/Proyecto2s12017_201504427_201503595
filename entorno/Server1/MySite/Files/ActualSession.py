from ArbolB import Arbol
from Pagina import Nodo,Pagina

from Usuarios import ListaSimple, NodoU


driveUsers = ListaSimple()
a=Arbol()
actualUser = NodoU("None","None")#Nodo de Usuario
RootTree = Nodo("root") #este es el /account/usuario/root, el nodo principal
ActualFolder = Nodo("")#Nodo de arbol b
ActualTree = Arbol()#arbol b

class SessionN(object):
	
	def __init__(self):

		print '====================================\n  Nueva Session'
		self.a=Arbol()
		self.actualUser = NodoU("None","None")#Nodo de Usuario
		self.RootTree = Nodo("root") #este es el /account/usuario/root, el nodo principal
		self.ActualFolder = Nodo("")#Nodo de arbol b
		self.ActualTree = Arbol()#arbol b
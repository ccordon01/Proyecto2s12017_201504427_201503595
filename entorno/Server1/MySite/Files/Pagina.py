from collections import deque


class Pagina(object):

	def __init__(self):
		self.Ramas = [None, None,None,None,None]
		self.Claves = [None, None,None,None,None]
		self.Cuentas = 0 #es el numero de claves llenas
		self._Hijos = deque()
		self.name = ""
		print 'se creo una nueva pagina'


	def get_hijos(self):
		return self._Hijos

	def set_hijos(self, value):
		self._Hijos = value

	hijos = property(fget=get_hijos, fset=set_hijos)



class Nodo(object):

	def __init__(self,id):
		self._carpetas = None
		self._archivos = None
		self.Id = id

	def addCarpeta(self):
		print 'add'
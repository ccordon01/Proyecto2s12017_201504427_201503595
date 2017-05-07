from Pagina import Pagina, Nodo
from collections import deque


'''lista = deque()
hijos = deque()
num = 1
struc = 1
usados = 2
total = 0
esperaos = 2
archivo = "digraph structs { \n node[shape=record]"
aux = deque()
principal = Pagina()
MovDer = Pagina()
MovIz = Pagina()
EmpujarArriba = False
Esta = False
Mov = None
NRaiz = None'''


class Arbol (object):



	def __init__ (self):
		'''print 'INICIALIZANDO CARPETA'
		print ''
		'''
		print'Se ha creado nuevo arbolB'
		self._lista = deque()
		self._hijos = deque("Raiz")
		self._num = 1
		self._struc = 1
		self._usados = 2
		self._total = 0
		self._esperaos = 2
		self._com = 1
		self._np =""
		self._archivo = "digraph structs { \n node[shape=record] \n"
		self._aux = deque
		self._principal = None
		self._Mov = None
		self._NRaiz = None

		self._MovDer = Pagina()
		self._MovIz = Pagina()

		self._EmpujarArriba = False
		self._Esta = False

		




	





	def Buscar(self, clave, raiz):
		if raiz.Claves[0] == None:
			return "No existen Carpetas"
		else:
			k = 0
			reto = raiz.Claves[k]
			if self._Esta:
				return "Se supone que este aqui?"
			else:
				if raiz.Cuentas > 0:  #Recuerda que "Cuentas" es el numero de claves que posee la raiz actual

				#k sera el numero en donde este
					k = self.Buscar(clave, raiz.Ramas[0])
					return "Se encontro clave en "+k
		return "raiz vacia"

	def NodoBus(self,clave,raiz):
		print 'BUSCARA'
		k = 0
		self._Esta = False
		if self.pagVacia(raiz):# si la raiz actual esta vacia
			print 'la Pagina esta vacia'
			return None
		else:
			print 'la pagina NO esta vacia'

			k = self.BuscarNodo(clave, raiz)
			if self._Esta:
				print "SE Encontro clave en raiz que empieza con: " + raiz.Claves[0].Id + " en la posicion " + str(k)
				return raiz.Claves[k]
			else:
				print 'volvera a buscar'
				return self.NodoBus(clave, raiz.Ramas[k])#banderilla
			return None




	def BuscarNodo(self, clave, raiz): # clave: el nodo o carpeta que se busca (con nombre y todo), raiz: es la pagina en donde se busca
		print 'entro a buscar nodo'

		j = 0

		if min(clave.Id.lower(),raiz.Claves[0].Id.lower().strip()) == clave.Id.lower(): #es porque no hay que correrlo, es un |2| y la raiz es por ejemplo  8|25|33

			if(clave.Id.lower()==raiz.Claves[0].Id.lower().strip()):
				print 'CLAVE REPETIDA EN LA PRIMERA POSICION DE LA RAIZ ACTUAL'
				self._Esta= True


			else:
				print 'la clave va en la primera posicion de la pagina actual'
				self._Esta = False
				j = 0


		else:
			print 'esta clave va despues'
			print ''
			j = raiz.Cuentas #el numero actual de nodos llenos\
			print 'esta raiz tiene ' + str(j) + ' claves'
			while min(clave.Id.lower(),raiz.Claves[j-1].Id.lower().strip()) == clave.Id.lower() and j > 1: #mientras el nuevo nodo sea menor que el de la clave de la raiz -1 y j sea mayor a 1
				j = j - 1
				if(clave.Id.lower() ==raiz.Claves[j].Id.lower().strip()):
					self._Esta = True
					return j
				print clave.Id +" kk no es igual "+ raiz.Claves[j].Id
				print str(j)+"Esta en buscar nodo y cambiando j"
				print ''

			print clave.Id +" es mayor "+ raiz.Claves[j-1].Id +' '+str(j)

			if clave.Id == raiz.Claves[j-1].Id:
				print str(j)+ "Este es el valor actual de j :v"
				self._Esta = True
			else:
				print j
				print clave.Id +" no es igual "+ raiz.Claves[j-1].Id
				self._Esta = False

			#self._Esta = (clave.Id == raiz.Claves[j - 1].Id)
		print 'la posicion final es '+ str(j) +'. El nodo esta? '+ str(self._Esta)
		return j



	def pagVacia(self, raiz):
		print 'Entro a pagVacia()'
		#print raiz.Cuentas
		return (raiz == None or raiz.Cuentas == 0 ) #or raiz.Cuentas == 0 esto va despues del none

	def Empujar(self, clave, raiz):
		print '--Entro a Empujar clave'
		k = 0
		self._Esta = False
		if self.pagVacia(raiz):# si la raiz actual esta vacia
			print 'la Pagina esta vacia'
			#raiz.name = "nombre 1"
			self._EmpujarArriba = True
			self._Mov = clave
			self._NRaiz = None
			print 'Se empujara arriba?  '+ str(self._EmpujarArriba)
		else:
			print 'la pagina NO esta vacia'
			print raiz.name
			print raiz.Claves[0].Id

			k = self.BuscarNodo(clave, raiz)
			if self._Esta:
				print 'la clave esta repetida'
				self._EmpujarArriba = False
			else:
				print 'se va a insertar'
				self.Empujar(clave, raiz.Ramas[k])#banderilla
				if self._EmpujarArriba:
					if raiz.Cuentas < 4:
						print 'cuentas < 4'
						self._EmpujarArriba = False
						self.InsertarClave(self._Mov, raiz, k)
					else:
						print 'cuentas ya es 5'
						self._EmpujarArriba = True
						self.MoverNodos(self._Mov, raiz, k)



	def nuevo(self,id):
		nuev = Nodo(id)
		return nuev


	def InsertarNuevo(self, nuevo):
		print ''
		print 'SE CREARA UNA NUEVA CARPETA'
		print '-------------------------------'
		inserto = nuevo
		inserto._Carpetas = Arbol()
		self.InsertarYa(inserto, self._principal)
		print str(self._principal.Cuentas)
		#print principal.Cuentas


	def InsertarYa(self, clave, raiz): #insertara el nuevo nodo en la raiz que manden como parametro
		print 'Se entro a Insertar Ya \n'

		print "NOMBRE DE NUEVA CARPETA "+ clave.Id
		#print raiz.name + " este es el primer nombre y tiene estas claves "+ str(raiz.Cuentas)
		self.Empujar(clave, raiz)
		#print raiz.name + "este es el nombre ya asignado " + str(self._EmpujarArriba)
		if self._EmpujarArriba: #esto lo que hara es que si una clave se llena, se partira la raiz
			print 'empujar arriba'
			self._principal = Pagina()
			self._principal.name = "principal"
			self._principal.Cuentas = 1
			self._principal.Claves[0] = self._Mov #se inserta el nodo en la raiz (solo se procesa en la raiz)
			self._principal.Ramas[0] = raiz #la raiz principal anterior se convierte
			self._principal.Ramas[1] = self._NRaiz
			#print 'se tienen ' + str(raiz.Cuentas)
			print 'y la principal tiene' + str(self._principal.Cuentas)



	def InsertarClave(self, clave, raiz, k):
		i = raiz.Cuentas
		while i != k:
			raiz.Claves[i] = raiz.Claves[i - 1]
			raiz.Ramas[i + 1] = raiz.Ramas[i]
			i -= 1
		raiz.Claves[k] = clave
		raiz.Ramas[k + 1] = self._NRaiz
		raiz.Cuentas = raiz.Cuentas + 1

	def MoverNodos(self, Clave, Raiz, k):
		pos = 0
		pMedia = 0
		if k <= 2:
			pMedia = 2
		else: #
			pMedia = 3
		Mder = Pagina()
		pos = pMedia + 1
		while pos != 5:
			Mder.Claves[(pos - pMedia) - 1] = Raiz.Claves[pos - 1]
			Mder.Ramas[pos - pMedia] = Raiz.Ramas[pos]
			pos += 1

		Mder.Cuentas = 4 -pMedia
		Raiz.Cuentas = pMedia

		if k<=2:
			self.InsertarClave(Clave,Raiz,k)
		else:
			self.InsertarClave(Clave,Mder,k-pMedia)

		self._Mov = Raiz.Claves[Raiz.Cuentas -1]
		Mder.Ramas[0]=Raiz.Ramas[Raiz.Cuentas]
		Raiz.Cuentas = Raiz.Cuentas-1
		self._NRaiz = Mder

#===============Eliminacion================
	def Eliminar(self, clave):
		if self.pagVacia(self._principal):
			print 'El arbol esta vacio'
		else:
			self.Eliminara(self._principal, clave)



	def Eliminara(self, Raiz, clave):
		try:
			self.EliminarRegistro(Raiz, clave)#intentara borrar la clave
		except Exception, e:
			print 'SE QUEDO EN LA EXCEPTION DE ELIMINIAR'
			self._Esta = False

		if  not self._Esta: #SI NO ESTA XD
			print 'No se encontro el elemento'
		else:
			if Raiz.Cuentas == 0:
				Raiz = Raiz.Ramas[0]
			self._principal = Raiz
			print "Se elimino" + clave.Id




	def EliminarRegistro(self, raiz, c):
		print ' \n \n'
		print 'Se intentara eliminar registro de '+c.Id
		pos = 0
		if self.pagVacia(raiz):
			self._Esta = False
		else:
			pos = self.BuscarNodo(c, raiz)
			if self._Esta:
				if self.pagVacia(raiz.Ramas[pos]) or raiz.Ramas[pos].Cuentas == 0:#este es para eliminar de una hoja
					print 'Se eliminara DE una hoja en la posicion '+ str(pos)

					self.ALV(raiz, pos)
				else:
					self.Sucesor(raiz, pos)
					self.EliminarRegistro(raiz.Ramas[pos], raiz.Claves[pos - 1])
			else:
				self.EliminarRegistro(raiz.Ramas[pos], c)
				if (raiz.Ramas[pos] != None) and (raiz.Ramas[pos].Cuentas < 2):
					self.Restablecer(raiz, pos)



	def Sucesor(self, raiz, k):
		q = raiz.Ramas[k]
		while not self.pagVacia(q.Ramas[0]):#mientras la rama de la pagina actual no sea vacia
			q = q.Ramas[0]
		raiz.Claves[k] = q.Claves[1]



	def Combina(self, raiz, pos):
		q = raiz.Ramas[pos]
		nIz = raiz.Ramas[pos-1]
		nIz.Cuentas +=1
		nIz.Claves[nIz.Cuentas] = raiz.Claves[pos]
		nIz.Claves[nIz.Cuentas]= q.Ramas[0]
		j=1
		while j<=q.Cuentas:
			nIz.Cuentas+=1
			nIz.Claves[nIz.Cuentas] = q.Claves[j]
			nIz.Ramas[nIz.Cuentas] =q.Ramas[j]
			j +=1

		j=pos
		while j<= raiz.Cuentas-1:
			raiz.Claves[j]=raiz.Claves[j+1]
			raiz.Ramas[j]= raiz.Ramas[j+1]
			j+=1
		raiz.Cuentas -=1



		'''MovDer = raiz.Ramas[pos]
		MovIz = raiz.Ramas[pos - 1]
		MovIz.Cuentas += 1
		MovIz.Claves[MovIz.Cuentas - 1] = raiz.Claves[pos - 1]
		MovIz.Ramas[MovIz.Cuentas] = MovDer.Ramas[0]
		j = 1
		while j != MovDer.Cuentas + 1:
			MovIz.Cuentas += 1
			MovIz.Claves[MovIz.Cuentas - 1] = MovDer.Claves[j - 1]
			MovIz.Ramas[MovIz.Cuentas] = MovDer.Ramas[j]
			j += 1
		self.ALV(raiz, pos)'''


	def MoverDer(self, raiz, pos):

		problema = raiz.Rama[pos]
		nIz = raiz.Ramas[pos-1]
		j = problema.Cuentas

		while j >= 1:
			problema.Claves[j+1]= problema.Claves[j]
			problema.Ramas[j+1]= problema.Ramas[j]
			j-=1
		problema.Cuentas +=1
		problema.Ramas[1] = problema.Ramas[0]
		problema.Claves[1]= raiz.Claves[pos]
		raiz.Claves[pos] = nIz.Claves[nIz.Cuentas]
		problema.Ramas[0] = nIz.Ramas[Nodo.Cuentas]
		nIz.Cuentas -=1

		'''i = raiz.Ramas[pos].Cuentas
		while i != 0:
			raiz.Ramas[pos].Claves[i] = raiz.Ramas[pos].Claves[i - 1]
			raiz.Ramas[pos].Ramas[i + 1] = raiz.Ramas[pos].Ramas[i]
			i -= 1
		raiz.Ramas[pos].Cuentas += 1
		raiz.Ramas[pos].Ramas[1] = raiz.Ramas[pos].Ramas[0]
		raiz.Ramas[pos].Claves[0] = raiz.Claves[pos - 1]
		raiz.Claves[pos - 1] = raiz.Ramas[pos - 1].Claves[raiz.Ramas[pos - 1].Cuentas - 1]
		raiz.Ramas[pos].Ramas[0] = raiz.Ramas[pos - 1].Ramas[raiz.Ramas[pos - 1].Cuentas]
		raiz.Ramas[pos - 1].Cuentas -= 1'''

	def MoverIzq(self, raiz, pos):
		problema = raiz.Rama[pos-1]
		nDer = raiz.Ramas[pos]

		problema.Cuentas +=1
		problema.Claves[problema.Cuentas]= raiz.Claves[pos]
		problema.Ramas [problema.Cuentas] = nDer.Ramas[0]

		raiz.Claves[pos]= nDer.Claves[1]
		nDer.Ramas[1]=nDer.Ramas[0]
		nDer.Cuentas -=1
		j = 1
		while j<= nDer.Cuentas:
			nDer.Claves[j] = nDer.Claves[j+1]
			nDer.Ramas[j]=nDer.Ramas[j+1]
			j+=1

		'''raiz.Ramas[pos - 1].Cuentas += 1
		raiz.Ramas[pos - 1].Claves[raiz.Ramas[pos - 1].Cuentas - 1] = raiz.Claves[pos - 1]
		raiz.Ramas[pos - 1].Ramas[raiz.Ramas[pos - 1].Cuentas] = raiz.Ramas[pos].Ramas[0]
		raiz.Claves[pos - 1] = raiz.Ramas[pos].Claves[0]
		raiz.Ramas[pos].Ramas[0] = raiz.Ramas[pos].Ramas[1]
		raiz.Ramas[pos].Cuentas -= 1
		i = 1
		while i != raiz.Ramas[pos].Cuentas + 1:
			raiz.Ramas[pos].Claves[i - 1] = raiz.Ramas[pos].Claves[i]
			raiz.Ramas[pos].Ramas[i] = raiz.Ramas[pos].Ramas[i + 1]
			i += 1'''

	def ALV(self, raiz, pos): # O sea quitar XD
		print '\n ha entrado a ALV'
		print 'se va a eliminar el indice ' + str(pos) +'en la raiz actual que empieza con '+raiz.Claves[0].Id
		j = pos + 1
		while j <= raiz.Cuentas:
			raiz.Claves[j - 1] = raiz.Claves[j]
			raiz.Ramas[j - 1] = raiz.Ramas[j]
			j =j+ 1
		raiz.Cuentas -= 1

	def Restablecer(self, raiz, pos):
		if pos > 0:
			if raiz.Ramas[pos - 1].Cuentas > 2:
				self.MoverDer(raiz, pos)
			else:
				self.Combina(raiz, pos)

		else:
			if raiz.Ramas[1].Cuentas > 2:
				self.MoverIzq(raiz, 1)
			else:
				self.Combina(raiz, 1)


	def Imagen(self, raiz):
		self._archivo = "digraph structs { \n node[shape=record]"
		self._num = 1
		self._struc = 1
		self._usados = 2
		self._total = 0

		self.GenerarStruc(self._principal)
		self._total = self._struc-1

		self._struc = 0
		self._usados = 0

		self.GenerarRel(self._principal)
		self._archivo = self._archivo + "}"
		#self.GenerarImagen()
		print self._archivo

	def GenerarStruc(self,raiz):
		if not self.pagVacia(raiz):
			print raiz.Claves[0].Id +" esta rama tiene tantas cuentas : " + str(raiz.Cuentas)
			self._archivo = self._archivo + "\n node" + str(self._struc) + "[label = \""
			self._struc = self._struc+1

			for i in range(4):
				if(i<raiz.Cuentas):
					self._archivo = self._archivo + " <f" + str(i + 1) + "> " + raiz.Claves[i].Id
					if (i<raiz.Cuentas-1):
						self._archivo = self._archivo + "|"
				else:
					self._archivo = self._archivo + " | <f" + str(i+1) + ">"
			self._archivo = self._archivo + " \"]; "
			

			for j in range(raiz.Cuentas+1):
				self.GenerarStruc(raiz.Ramas[j])
		else:
			print 'pag v'

	def GenerarRel(self,raiz):
		print 'ke quee'


 	def GenerarImagen(self):
 		print 'generar'



 	def Imprime(self,raiz):
		self._com = 1
		self.ImprimeYa(raiz)



	def ImprimeYa(self,raiz):

		'''self._hijos.append("RAIZ")
		print str(self._hijos.popleft())'''

		print str(raiz.Cuentas) + " = numero de claves que posee y la raiz inicia con " + raiz.Claves[0].Id
		if raiz.Cuentas >0:
			for i in range(5):
				#print str(i) + str(raiz.Cuentas)
				if i>raiz.Cuentas-1 or raiz.Claves[i]== None :
					for k in range(i,5):
						raiz.Claves[k]==None
						k = k+1
					break
				else:
					print str(self._com) +". "+ raiz.Claves[i].Id
					self._com +=1


			'''for i in range(raiz.Cuentas):
				print str(self._com) +". "+ raiz.Claves[i].Id
				self._com +=1'''

			for n in range(raiz.Cuentas+1):

				if(raiz.Ramas[n]!= None):
					print ''
					print 'hijo '+str(n) +' del raiz que empieza con ' + str(raiz.Claves[0].Id)

					self.ImprimeYa(raiz.Ramas[n])

	def ListaCarpetas(self):
		if self.pagVacia(self._principal):
			self._np = "vacio"
		else:
			self.Lista(self._principal)


	def Lista(self,raiz):
		if not self.pagVacia(raiz):
			for i in xrange(raiz.Cuentas+1):
				if(raiz.Ramas[0]!= None):
					self.Lista(raiz.Ramas[i])
				if i<raiz.Cuentas:
					self._np = self._np+raiz.Claves[i].Id + "|"	

			

			
                    




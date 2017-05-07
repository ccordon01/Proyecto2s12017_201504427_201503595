from Usuarios import ListaSimple
from ArbolB import Arbol
from Pagina import Nodo,Pagina
from Probando import probando
a = Arbol()
p = probando()
class Prueba ():

	'''
	cd documents\edd\laboratorio\proyecto2\entorno\server1
	python manage.py runserver 0.0.0.0:8000


	cd documents\edd\laboratorio\proyecto2\entorno\server1\mysite\files
	python prueba.py
	'''

	def __init__():
		print 'prueba'
		self.inn= Usuarios()
		inicial()


	def inicial():
		inn = ListaSimple( )
		inn.insertar(inn.nuevoNodo('holi','pass123'))
		print 'hola'

	def eliminar():
		print 'que dato desea eliminar?'
		dato = str(raw_input())
		a.Eliminar(a.nuevo(dato))
		a.Imprime(a._principal)

	def buscar():
		print 'que dato desea buscar?'
		dato = str(raw_input())
		return a.NodoBus(a.nuevo(dato),a._principal)

	def OtraVEz():
		print '\n  probar borrar otro dato?'
		print '1. Si porfis \n 2. Nel shabo'

		op = input()

		if op ==1:
			eliminar()
		elif op ==2:
			input("press any key")
		else:
			print "que eres fracasado o que?"
			OtraVEz()

	if __name__ == '__main__':

		print '=========================== Inicializandooooo========================'
		#p.menu()

		inicial()
		k = "c1"
		n = "C10"

		print min(k.lower(),n.lower())==k.lower()

		'''a.InsertarNuevo(a.nuevo("M"))
		a.InsertarNuevo(a.nuevo("S"))
		a.Imprime(a._principal)
		a.InsertarNuevo(a.nuevo("h"))
		a.Imprime(a._principal)
		a.InsertarNuevo(a.nuevo("r"))

		print "ESTA MIERDA DEBERIA SER M " + a._principal.Claves[1].Id

		a.Imprime(a._principal)

		a.InsertarNuevo(a.nuevo("o"))'''




		a.InsertarNuevo(a.nuevo("05"))
		a.InsertarNuevo(a.nuevo("20"))
		a.InsertarNuevo(a.nuevo("40"))
		a.InsertarNuevo(a.nuevo("10"))
		a.InsertarNuevo(a.nuevo("30"))
		#a.Imprime(a._principal)

		a.InsertarNuevo(a.nuevo("15"))
		a.InsertarNuevo(a.nuevo("36"))
		a.InsertarNuevo(a.nuevo("07"))
		#a.Imprime(a._principal)
		a.InsertarNuevo(a.nuevo("26"))

		a.InsertarNuevo(a.nuevo("18"))
		a.InsertarNuevo(a.nuevo("22"))
		a.InsertarNuevo(a.nuevo("05"))
		a.InsertarNuevo(a.nuevo("42"))
		a.InsertarNuevo(a.nuevo("13"))
		a.InsertarNuevo(a.nuevo("46"))
		a.InsertarNuevo(a.nuevo("27"))
		a.InsertarNuevo(a.nuevo("08"))
		a.InsertarNuevo(a.nuevo("32"))
		a.InsertarNuevo(a.nuevo("38"))
		a.InsertarNuevo(a.nuevo("24"))
		a.InsertarNuevo(a.nuevo("45"))
		a.InsertarNuevo(a.nuevo("25"))



		print '\n \n'
		print '####impresion####'
		a.Imprime(a._principal)


		'''print '\n =================buscar============'

	 	nuevon = buscar()
	 	if nuevon != None:
	 		print 'se encontro ' + nuevon.Id
		 	nuevon._Carpetas = Arbol()
		 	nuevon._Carpetas.InsertarNuevo(nuevon._Carpetas.nuevo("c115"))
		 	nuevon._Carpetas.InsertarNuevo(nuevon._Carpetas.nuevo("4"))

		 	nuevon._Carpetas.InsertarNuevo(nuevon._Carpetas.nuevo("c5"))

		 	nuevon._Carpetas.InsertarNuevo(nuevon._Carpetas.nuevo("c5"))
		 	nuevon._Carpetas.Imprime(nuevon._Carpetas._principal)

'''

		print ' \n ====================eliminacion :v================= \n'
		#eliminar()
		a.Eliminar(a.nuevo("10"))
		#a.Imprime(a._principal)
		#a.Eliminar(a.nuevo("c3"))
		#a.Imprime(a._principal)


		'''a.InsertarNuevo(a.nuevo("a1"))
		a.InsertarNuevo(a.nuevo("a2"))
		a.InsertarNuevo(a.nuevo("a3"))
		a.InsertarNuevo(a.nuevo("a4"))
		a.InsertarNuevo(a.nuevo("a5"))
		a.InsertarNuevo(a.nuevo("a8"))
		a.InsertarNuevo(a.nuevo("j1"))
		a.InsertarNuevo(a.nuevo("j2"))
		a.InsertarNuevo(a.nuevo("j3"))
		a.InsertarNuevo(a.nuevo("j4"))
		a.InsertarNuevo(a.nuevo("j5"))'''
		print '==================finally========================='
		print '=================================================='
		#a.Imprime(a._principal)
		a.Imagen(a._principal)
		a.NodoBus(a.nuevo("j5"),a._principal)
		a.ListaCarpetas()
		print a._np
		#a.Eliminar(a.nuevo("c9"))
		a.Imprime(a._principal)








		#a.Imprime'''

from Usuarios import ListaSimple
from ArbolB import Arbol
from Pagina import Nodo,Pagina
from Probando import probando
a = Arbol()
p = probando()
class Prueba ():

	'''
	cd documents\estructura de datos\laboratorio\proyecto2\entorno\server1
	python manage.py runserver


	cd documents\estructura de datos\laboratorio\proyecto2\entorno\server1\mysite\files
	python prueba.py
	'''

	def __init__():
		print 'prueba'
		self.inn= Usuarios()
		inicial()


	def inicial():
		inn = ListaSimple( )
		inn.insertar('holi','pass123')
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




		a.InsertarNuevo(a.nuevo("c1"))
		a.InsertarNuevo(a.nuevo("c2"))
		a.InsertarNuevo(a.nuevo("c3"))
		a.InsertarNuevo(a.nuevo("c4"))
		a.InsertarNuevo(a.nuevo("c5"))
		#a.Imprime(a._principal)

		a.InsertarNuevo(a.nuevo("c6"))
		a.InsertarNuevo(a.nuevo("c7"))
		a.InsertarNuevo(a.nuevo("c8"))
		#a.Imprime(a._principal)
		a.InsertarNuevo(a.nuevo("c9"))

		a.InsertarNuevo(a.nuevo("c10"))
		a.InsertarNuevo(a.nuevo("c11"))
		a.InsertarNuevo(a.nuevo("c12"))
		a.InsertarNuevo(a.nuevo("c13"))
		a.InsertarNuevo(a.nuevo("c14"))
		a.InsertarNuevo(a.nuevo("c15"))
		a.InsertarNuevo(a.nuevo("c16"))
		a.InsertarNuevo(a.nuevo("c17"))
		a.InsertarNuevo(a.nuevo("c18"))
		a.InsertarNuevo(a.nuevo("c19"))
		a.InsertarNuevo(a.nuevo("c7"))
		a.InsertarNuevo(a.nuevo("c111"))
		a.InsertarNuevo(a.nuevo("c112"))
		a.InsertarNuevo(a.nuevo("c113"))
		a.InsertarNuevo(a.nuevo("c114"))
		a.InsertarNuevo(a.nuevo("c115"))




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
		#a.Eliminar(a.nuevo("c2"))
		#a.Imprime(a._principal)
		#a.Eliminar(a.nuevo("c3"))
		#a.Imprime(a._principal)


		a.InsertarNuevo(a.nuevo("a1"))
		a.InsertarNuevo(a.nuevo("a2"))
		a.InsertarNuevo(a.nuevo("a3"))
		a.InsertarNuevo(a.nuevo("a4"))
		a.InsertarNuevo(a.nuevo("a5"))
		a.InsertarNuevo(a.nuevo("a8"))
		a.InsertarNuevo(a.nuevo("j1"))
		a.InsertarNuevo(a.nuevo("j2"))
		a.InsertarNuevo(a.nuevo("j3"))
		a.InsertarNuevo(a.nuevo("j4"))
		a.InsertarNuevo(a.nuevo("j5"))
		print '==================finally========================='
		print '=================================================='
		a.Imprime(a._principal)
		a.GenerarStruc(a._principal)
		print a._archivo
		#a.Eliminar(a.nuevo("c9"))
		#a.Imprime(a._principal)








		#a.Imprime'''

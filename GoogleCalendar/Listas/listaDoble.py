import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/usr/bin/Python/GoogleCalendar/Nodos')
#Importo la Clase
from nodosG import Clasedos
from nodosG import nodoCalendar
class ClaseListaDoble(Clasedos):
     def __init__(self):
          self.primerNodo = None
          self.ultimoNodo = None

     def estaVacia(self):
         if self.primerNodo == None:
             print "si esta vacia"
             return True
         return False

     def insertarAlFrente(self,datos):
         if self.estaVacia():
              #print "insertar primer elemento en la lista"
              self.ultimoNodo = Clasedos(datos,None,None)
              self.primerNodo = self.ultimoNodo
         else:
               #print "existen elementos en la lista"
               nuevo = Clasedos

               (datos,self.primerNodo,None)
               self.primerNodo.nodoAnterior = nuevo
               self.primerNodo = nuevo
     def insertarAlFinal(self,datos):
         if self.estaVacia():
              #print "insertar primer elemento en la lista x2" 
              self.ultimoNodo = Clasedos(datos,None,None)
              self.primerNodo = self.ultimoNodo
              return "Usuario creado"
         else:
            if self.usuarioUnico(datos.usuario):
               #print "existen elementos en la lista x2"
               self.ultimoNodo.nodoSiguiente = Clasedos(datos,None,self.ultimoNodo)
               self.ultimoNodo = self.ultimoNodo.nodoSiguiente
               return "Usuario creado"
            else:
            	return "Usuario ya existe"
          #print("guau") 
     def eliminarDelFrente(self):
         if self.estaVacia():
             return "Esta vacia"
         else:
             data = self.primerNodo.datos
             self.primerNodo.nodoAnterior = None
             self.primerNodo = self.primerNodo.nodoSiguiente
             #self.primerNodo.nodoAnterior = None
             return data

     def usuarioUnico(self,user):
        if self.estaVacia():
           return True
        else:
         actual = self.primerNodo
         while (actual != None):
              if str(actual.datos.usuario) == str(user) :
              	return False
              actual = actual.nodoSiguiente
         print "Fin"
         return True

     def mostrar(self):
          actual = self.primerNodo
          while (actual != None):
              print "Dato: " + actual.datos
              actual = actual.nodoSiguiente
          print "Fin"

     def size(self):
          size = 0
          actual = self.primerNodo
          while (actual != None):
              size = size + 1
              #print "Dato: " + actual.datos
              actual = actual.nodoSiguiente
          #print "Fin"
          return size
     def delbypos(self,pos):
          if not self.estaVacia():
              actual = self.primerNodo
          if int(pos) == 0:
               return self.eliminarDelFrente()
          if (int(pos) + 1) == self.size():
                  actual = self.ultimoNodo
                  data = actual.datos
                  actual.nodoAnterior.nodoSiguiente = actual.nodoSiguiente
                   #actual.nodoSiguiente.nodoAnterior = actual.nodoAnterior
                  return data
          else:
              for x in xrange(1,self.size()):
               actual = actual.nodoSiguiente
               if x==int(pos):
                   data = actual.datos
                   actual.nodoAnterior.nodoSiguiente = actual.nodoSiguiente
                   actual.nodoSiguiente.nodoAnterior = actual.nodoAnterior
                   return data
          return "null"
     def delbyvalue(self,value):
          actual = self.primerNodo
          for x in xrange(0,self.size()):
               #return value + "=" + actual.datos
               if str(value) == str(actual.datos):
                   print "Se encontro en la posicion: " + str(x)
                   return self.delbypos(x)
               actual = actual.nodoSiguiente
     def byvalue(self,value):
          actual = self.primerNodo
          for x in xrange(0,self.size()):
               if str(value) == str(actual.datos):
                   return x
                   #return self.delbypos(x)
               actual = actual.nodoSiguiente
          return "null"
     def mostrarc(self):
          actual = self.primerNodo
          text = ""
          while (actual != None):
              text= actual.datos.usuario + "," +text
              actual = actual.nodoSiguiente
          return text
     def loginLista(self,user,passw):
        if self.estaVacia():
           return "Lista Vacia"
        else:
         actual = self.primerNodo
         while (actual != None):
              if str(actual.datos.usuario) == str(user) :
                 if str(actual.datos.passw) == str(passw):
              		 return "Accesso permitido"
              actual = actual.nodoSiguiente
         print "Fin"
         return "Accesso denegado"

     def loginNodo(self,user,passw):
        if self.estaVacia():
           return "Lista Vacia"
        else:
         actual = self.primerNodo
         while (actual != None):
              if str(actual.datos.usuario) == str(user) :
                 if str(actual.datos.passw) == str(passw):
                   print "nodo encontrado"
                   return actual
              actual = actual.nodoSiguiente
         print "Fin"
         return None



nodo = None     
Lista = ClaseListaDoble()
print Lista.insertarAlFinal(nodoCalendar("charliecech","1234"))
print Lista.insertarAlFinal(nodoCalendar("charlie","1234"))
print Lista.loginLista("charlie","1234")
nodo = Lista.loginNodo("charlie","1234")
if nodo != None:
  print "funciona"
print Lista.size()
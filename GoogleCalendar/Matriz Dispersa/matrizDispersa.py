import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/usr/bin/Python/GoogleCalendar/Matriz Dispersa')
#Importo la Clase
from nodo import Claseuno
from nodo import Clasedos
from nodo import Clasetres
from nodo import Clasecuatro
from nodo import Clasecinco
from lista import ClaseListaDoble
from ArbolAVL import Arbol
from NodoArbolAVL import NodoArbol
datosAVL=[]
class ClassMatriz(Clasetres):
    """docstring for ClassName"""
    def __init__(self):
        #super(ClassName, self).__init__()
        #self.arg = arg
        self.primerNodo = Clasetres("Nodo Inicial",None,None,None,None)

##########################   Cabecera Letras  #################################################        
    def insertarCabeceraLetras(self,letra):
        if self.primerNodo.nodoInferior == None:
             self.primerNodo.nodoInferior = Clasetres(letra,None,None,self.primerNodo,None)
             return "Primer nodo creado con " + letra
        if not self.elementExistInCabeceraLetras(letra):
             actual = self.primerNodo.nodoInferior
             temp = self.primerNodo.nodoInferior
             val = ord(letra[0])
             if val < ord(actual.datos[0]):
                 nuevo = Clasetres(letra,None,None,self.primerNodo,actual)
                 self.primerNodo.nodoInferior = nuevo
                 actual.nodoSuperior = nuevo
                 return "Nodo Creado " + letra
             else:
                  while (actual != None):
                      if val < ord(actual.datos[0]):
                          nuevo = Clasetres(letra,None,None,actual.nodoSuperior,actual)
                          actual.nodoSuperior.nodoInferior = nuevo
                          actual.nodoSuperior = nuevo
                          return "Nodo Creado " + letra
                      if not actual.nodoInferior == None:
                            temp = actual.nodoInferior
                      actual = actual.nodoInferior
                  nuevo = Clasetres(letra,None,None,temp,None)
                  temp.nodoInferior = nuevo 
                  return "Nodo Creado " + letra


    def elementExistInCabeceraLetras(self,letra):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               if actual.datos == letra:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoInferior
         print "No existe nodo"
         return False

    def mostrarCabeceraLetras(self):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               print "Nodo " + actual.datos
               actual = actual.nodoInferior
         print "Fin"
#########################################################################################

############################   Cabecera De Dominios    ##################################

    def insertarCabeceraDominios(self,dominio):
         if self.primerNodo.nodoSiguiente == None:
             self.primerNodo.nodoSiguiente = Clasetres(dominio,None,self.primerNodo,None,None)
             return "Primer dominio creado " + dominio
         if not self.elementExistInCabeceraDominios(dominio):
             actual = self.primerNodo.nodoSiguiente
             temp = self.primerNodo.nodoSiguiente
             val = ord(dominio[0])
             if val < ord(actual.datos[0]):
                 nuevo = Clasetres(dominio,actual,self.primerNodo,None,None)
                 self.primerNodo.nodoSiguiente = nuevo
                 actual.nodoAnterior = nuevo
                 return "Nodo Creado " + dominio
             else:
                  while (actual != None):
                      if val < ord(actual.datos[0]):
                          nuevo = Clasetres(dominio,actual,actual.nodoAnterior,None,None)
                          actual.nodoAnterior.nodoSiguiente = nuevo
                          actual.nodoAnterior = nuevo
                          return "Nodo Creado ant " + dominio
                      if val == ord(actual.datos[0]):
                          print "Nodo igual " + dominio
                          tam = 0
                          if cmp(str(dominio),str(actual.datos)) < 0:
                                nuevo = Clasetres(dominio,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado 7 " + dominio
                      if not actual.nodoSiguiente == None:
                            temp = actual.nodoSiguiente
                      actual = actual.nodoSiguiente
                  nuevo = Clasetres(dominio,None,temp,None,None)
                  temp.nodoSiguiente = nuevo 
                  return "Nodo Creado post" + dominio


    def elementExistInCabeceraDominios(self,dominio):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               if actual.datos == dominio:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoSiguiente
         print "No existe nodo"
         return False

    def mostrarCabeceraDominios(self):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               print "Nodo " + actual.datos
               actual = actual.nodoSiguiente
         print "Fin"
#############################################################################################


###########################        Insertar correo        ###################################

    def insertarCorreo(self,name,dominio):
      #primerCambio
         self.insertarCabeceraLetras(name)
         self.insertarCabeceraDominios(dominio)
         listaData = ClaseListaDoble()
         NodoLetra = self.nodoL(name)
         nodoData = Clasecuatro(name,dominio,listaData)
         if NodoLetra.nodoSiguiente == None:
             nuevo = Clasetres(nodoData,None,NodoLetra,None,None)
             NodoLetra.nodoSiguiente = nuevo
             return "Nodo Creado " + name + "-"+ dominio
         if not self.elementExistInMatriz(NodoLetra,dominio):
             actual = NodoLetra.nodoSiguiente
             temp = NodoLetra.nodoSiguiente
             val = ord(dominio[0])
             if val < ord(actual.datos.correo[0]):
                 nuevo = Clasetres(nodoData,actual,NodoLetra,None,None)
                 NodoLetra.nodoSiguiente = nuevo
                 actual.nodoAnterior = nuevo
                 return "Nodo Creado " + name + "-"+ dominio
             else:
                  while (actual != None):
                      if val < ord(actual.datos.correo[0]):
                          nuevo = Clasetres(nodoData,actual,actual.nodoAnterior,None,None)
                          actual.nodoAnterior.nodoSiguiente = nuevo
                          actual.nodoAnterior = nuevo
                          return "Nodo Creado " + name + "-"+ dominio
                      if val == ord(actual.datos.correo[0]):
                          print "Nodo igual " + dominio
                          tam = 0
                          if cmp(str(dominio),str(actual.datos.correo)) < 0:
                                nuevo = Clasetres(nodoData,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado 7 " + dominio
                      if not actual.nodoSiguiente == None:
                            temp = actual.nodoSiguiente
                      actual = actual.nodoSiguiente
                  nuevo = Clasetres(nodoData,None,temp,None,None)
                  temp.nodoSiguiente = nuevo 
                  return "Nodo Creado " + name + "-"+ dominio

    def nodoL(self,letra):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               if actual.datos == letra:
                   return actual
               actual = actual.nodoInferior
         return None

    def elementExistInMatriz(self,NodoLetra, correo):
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               if actual.datos.correo == correo:
                   return True
               actual = actual.nodoSiguiente
         return False

    def insertarDatos(self,name,dominio,user,password):
         NodoLetra = self.nodoL(name)
         if NodoLetra.nodoSiguiente == None:
             return "no hay siguiente"
         NodoDominio = self.nodoD(dominio)
         nodoMagico = self.nodoM(NodoLetra,dominio)
         if NodoDominio == None:
             return "null dominio"
         if nodoMagico == None:
             return "null magico"
         NodoUser = Clasecinco(user,password)
         nodoMagico.lista.insertarAlFinal(NodoUser)
         if NodoDominio.nodoInferior == None:
             NodoDominio.nodoInferior = Clasetres(nodoMagico,None,None,NodoDominio,None)
             return "Primer nodo creado con " + nodoMagico.letra
         if not self.elementExistInCabeceraLetrasM(nodoMagico.letra,NodoDominio):
             actual = NodoDominio.nodoInferior
             temp = NodoDominio.nodoInferior
             val = ord(nodoMagico.letra[0])
             if val < ord(actual.datos.letra[0]):
                 nuevo = Clasetres(nodoMagico,None,None,self.primerNodo,actual)
                 NodoDominio.nodoInferior = nuevo
                 actual.nodoSuperior = nuevo
                 return "Nodo Creado " + nodoMagico.letra
             else:
                  while (actual != None):
                      if val < ord(actual.datos.letra):
                          nuevo = Clasetres(nodoMagico,None,None,actual.nodoSuperior,actual)
                          actual.nodoSuperior.nodoInferior = nuevo
                          actual.nodoSuperior = nuevo
                          return "Nodo Creado " + nodoMagico.letra
                      if not actual.nodoInferior == None:
                            temp = actual.nodoInferior
                      actual = actual.nodoInferior
                  nuevo = Clasetres(nodoMagico,None,None,temp,None)
                  temp.nodoInferior = nuevo 
                  return "Nodo Creado " + nodoMagico.letra
         return self.getMagico(nodoMagico.letra,NodoDominio).lista.insertarAlFinal(NodoUser)

    def nodoD(self,dominio):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               if actual.datos == dominio:
                        return actual
               actual = actual.nodoSiguiente
         return None

    def nodoM(self,NodoLetra, correo):
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               if actual.datos.correo == correo:
                   return actual.datos
               actual = actual.nodoSiguiente
         return None
    def elementExistInCabeceraLetrasM(self,letra,nd):
         actual = nd.nodoInferior
         while (actual != None):
               if actual.datos.letra == letra:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoInferior
         print "No existe nodo"
         return False


    def getMagico(self,letra,nd):
         actual = nd.nodoInferior
         while (actual != None):
               if actual.datos.letra == letra:
                        print "Nodo Magico encontrado"
                        return actual.datos
               actual = actual.nodoInferior
         print "No existe Nodo Magico"
         return False

    def findbyl(self,letra):
         NodoLetra = self.nodoL(letra)
         if NodoLetra == None:
           return "Letra no existe"
         actual = NodoLetra.nodoSiguiente
         text = ""
         while (actual != None):
               text =text + actual.datos.lista.mostrarc()
               actual = actual.nodoSiguiente
         return text

    def findbyd(self,dominio):
         NodoLetra = self.nodoD(dominio)
         if NodoLetra == None:
           return "Dominio no existe"
         actual = NodoLetra.nodoInferior
         text = ""
         while (actual != None):
               text = text + actual.datos.lista.mostrarc()
               #return text
               actual = actual.nodoInferior
         return text
    def borrarDatos(self,name,dominio):
       NodoLetra = self.nodoL(name)
       if NodoLetra.nodoSiguiente == None:
        return "no hay siguiente"
       NodoDominio = self.nodoD(dominio)
       nodoMagico = self.nodoM(NodoLetra,dominio)
       if NodoDominio == None:
        return "null dominio"
       if nodoMagico == None:
        return "null magico"
       return nodoMagico.lista.delbyvalue(name + "@" + dominio)

    def login(self,name,dominio,user,password):
         NodoLetra = self.nodoL(name)
         if NodoLetra == None:
           return "Departamento no existe"
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               #text =text + actual.datos.lista.mostrarc()
               if actual.datos.correo == dominio:
                  actualM = actual.datos.lista.primerNodo
                  text = ""
                  while (actualM != None):
                       if actualM.datos.usuario == user:
                         if str(actualM.datos.passw) == str(password):
                           return "Bienvenido "+ user
                         else:
                           return "Contrasena incorrecta"
                       actualM = actualM.nodoSiguiente
                  return "Usuario incorrecto"
               actual = actual.nodoSiguiente
         return "No existe empresa"

    def insertarAvl(self,name,dominio,user,nombre,descripcion,lugar,hora):
         NodoLetra = self.nodoL(name)
         if NodoLetra == None:
           return "Departamento no existe"
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               #text =text + actual.datos.lista.mostrarc()
               if actual.datos.correo == dominio:
                  actualM = actual.datos.lista.primerNodo
                  text = ""
                  while (actualM != None):
                       if actualM.datos.usuario == user:
                        return actualM.datos.nodoAvl.insertar(nombre,lugar,descripcion,hora)
                       actualM = actualM.nodoSiguiente
                  return "Usuario incorrecto"
               actual = actual.nodoSiguiente
         return "No existe empresa"

    def mostrarAvl(self,name,dominio,user):
         NodoLetra = self.nodoL(name)
         if NodoLetra == None:
           return "Departamento no existe"
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               #text =text + actual.datos.lista.mostrarc()
               if actual.datos.correo == dominio:
                  actualM = actual.datos.lista.primerNodo
                  text = ""
                  while (actualM != None):
                       if actualM.datos.usuario == user:
                        actualM.datos.nodoAvl.preOrden(actualM.datos.nodoAvl.obtenerRaiz())
                       actualM = actualM.nodoSiguiente
                  return "Usuario incorrecto"
               actual = actual.nodoSiguiente
         return "No existe empresa"

    def mostrarHash(self):
         del datosAVL[:]
         datosTH = ""
         NodoLetra = self.primerNodo.nodoInferior
         while (NodoLetra != None):
             actual = NodoLetra.nodoSiguiente
             while (actual != None):
                  actualM = actual.datos.lista.primerNodo
                  while (actualM != None):
                        datosTH+=actualM.datos.nodoAvl.mostrar()
                        actualM = actualM.nodoSiguiente
                  actual = actual.nodoSiguiente
             NodoLetra = NodoLetra.nodoInferior
         print "----------------------------------------------------------"
         return datosTH 

    def rentarAVL(self,us,idp,dias):
         NodoLetra = self.primerNodo.nodoInferior
         while (NodoLetra != None):
             actual = NodoLetra.nodoSiguiente
             while (actual != None):
                  actualM = actual.datos.lista.primerNodo
                  while (actualM != None):
                        if str(actualM.datos.nodoAvl.buscaR(us,idp,dias,actualM.datos.nodoAvl.obtenerRaiz())) != str("None"):
                          return "Renta Realizada Con Exito"
                        actualM = actualM.nodoSiguiente
                  actual = actual.nodoSiguiente
             NodoLetra = NodoLetra.nodoInferior
         return "Renta Realizada Con Exito"

    def devolverAVL(self,idp):
         NodoLetra = self.primerNodo.nodoInferior
         while (NodoLetra != None):
             actual = NodoLetra.nodoSiguiente
             while (actual != None):
                  actualM = actual.datos.lista.primerNodo
                  while (actualM != None):
                        if str(actualM.datos.nodoAvl.devolverR(idp,actualM.datos.nodoAvl.obtenerRaiz())) != str("None"):
                          return "Devolucion Realizada Con Exito"
                        actualM = actualM.nodoSiguiente
                  actual = actual.nodoSiguiente
             NodoLetra = NodoLetra.nodoInferior
         return "Devolucion Realizada Con Exito"



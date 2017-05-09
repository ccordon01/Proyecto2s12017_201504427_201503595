import sys
sys.path.append('/usr/bin/Python/GoogleCalendar/Matriz Dispersa/')
from matrizDispersa import ClassMatriz

#Clase De Nodo Base De Una Lista
class Claseuno(object):
#Constructor
     def __init__(self,datos,nodo):
     	 self.datos = datos
     	 self.nodo = nodo
class Clasedos(object):
#Constructor
     def __init__(self,datos,nodoSiguiente,nodoAnterior):
     	 self.datos = datos
     	 self.matrizD = ClassMatriz()
     	 self.nodoSiguiente = nodoSiguiente
     	 self.nodoAnterior = nodoAnterior

class nodoCalendar(object):
	
#Constructor
     def __init__(self,usuario,passw):
     	 self.usuario = usuario
     	 self.passw = passw
     	 self.drive = None
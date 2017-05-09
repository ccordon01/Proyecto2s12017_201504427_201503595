class nodoHash(object):
    def __init__(self):
        super(nodoHash, self).__init__()
        self.dato=None
        self.estado= 0
        
class nodoEvento(object):
    def __init__(self,nombre,direccion,descripcion,hora):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.hora = hora

class adminHash(object):
    def __init__(self,tam):
        super(adminHash, self).__init__()
        self.tam = tam
        self.hash = []
        for x in xrange(0,tam):
        	self.hash.append(nodoHash())

    def calculoString(self,palabra):
        valorAscci = 0
        for x in palabra:
            #print str(ord(x))
            valorAscci += ord(x)
        return valorAscci

    def function(self,valor):
    	valor=valor*valor
    	#print valor
    	valueStr=str(valor)
    	if len(str(valor)) %2==0:
            return valueStr[len(str(valor))/2 - 1:len(str(valor))/2 + 1]
    		#print len(str(valor))/2
        else:
        	return valueStr[(len(str(valor)) -1)/2 - 1:(len(str(valor)) -1)/2 + 1]
    	return len(str(valor)) 	

    def insertarHash(self,nodo,pos):
        if int(self.hash[pos].estado)==0 or int(self.hash[pos].estado)==1:
            self.hash[pos].estado = 2
            self.hash[pos].dato = nodo
            return pos
        else: 
        	pos+=1
        while pos<self.tam:
            if int(self.hash[pos].estado)==0 or int(self.hash[pos].estado)==1:
                self.hash[pos].estado = 2
                self.hash[pos].dato = nodo
                return pos
            else: 
        	    pos+=1
        return -1

    def insertar(self,nombre,direccion,descripcion,hora):
    	evento = nodoEvento(nombre,direccion,descripcion,hora)
    	return self.insertarHash(evento,int(self.function(self.calculoString(nombre))))
    
    def eliminar(self,nombre):
    	pos = int(self.function(self.calculoString(str(nombre))))
        print nombre
    	while pos<self.tam:
            if int(self.hash[pos].estado)==2:
                if self.hash[pos].dato.nombre == nombre:
                     self.hash[pos].dato.nombre = None
                     self.hash[pos].estado = 1
                     return "Evento Eliminado"
            pos+=1
        return "No existe evento"    

    def mostrar(self):
        pos = 0
        datos = ""
        while pos<self.tam:
            if int(self.hash[pos].estado)==2:
                datos += str(self.hash[pos].dato.nombre) + "," + str(self.hash[pos].dato.hora) + ";"
            pos+=1
        return datos

adminTabla = adminHash(101)
#print len(adminTabla.hash)
index =adminTabla.insertar("Cumple Papi","Zona 2","Cumple Papi", "8:45")
print str(index) +" "+adminTabla.hash[index].dato.nombre
index =adminTabla.insertar("Cumple Papi","Zona 2","Cumple Papi", "8:45")
print str(index) +" "+adminTabla.hash[index].dato.nombre
print adminTabla.mostrar()
print adminTabla.eliminar("Cumple Papi")
#print "Hola Mundo"
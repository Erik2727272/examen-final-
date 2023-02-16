#MANERA COMPLEJA RELACIONADO A PILA Y COLAS

#1. Crea un programa en Python que simule
#  una lista de compras. El programa debe
#  permitir al usuario agregar productos 
# al final de la lista, eliminar productos 
# del inicio de la lista y mostrar todos los 
# productos en la lista en orden de compra.

#CREAMOS UNA CLASE NODO
class Nodo:
    def __init__(self, dato): #DEFINIMOS LOS PARAMETROS SELF, DATO
        self.dato = dato        #SELF.SIGUIENTE APUNTA A DATO
        self.siguiente = None   #SEL.SIGUIENTE APUNTA A NULL O VACIO 
        self.anterior = None

class ListaCola:  #CREAMOS UNA CLASE LISTACOLA:

    def __init__(self): #FUNCION INIT QUE RECIBE EN SU PARAMETRO SELF
        self.primero = None    #SELF. primero APUNTA A VACIO o null 
        self.ultimo = None      #SELF. ultimo APUNTA A VACIO o null 
        self.size = 0        # apuntamos a 0
    
    #agregar final
    def vacia(self):            #funcion vacia
        return self.primero == None    #retoramos self.primero apuntado a null 
    
    def agregar_producto(self, dato):    #funcion para agregar productos
        if self.vacia():                        #condicional si self.vacio
            self.primero = self.ultimo = Nodo(dato)     #self.primero apunta a self.ultimo tambine a punta a Nodo
        else:                               #caso contrario
            aux = self.ultimo       #auxiliar apunta a self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)    #self.ultimo apunta a aux.siguiente apunta a nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1                          #aumentamos el contador en 1
    
    #eliminar inicio
    def eliminar_producto(self):            #funcion eliminar producto  
        if self.vacia():                    #si self.vacio 
            print("Lista vacía")            #imprimos "LISTA VACIA"
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:                                   #cONTRARIO
            self.primero = self.primero.siguiente       #SEL.primero apunta a self. primero. siguiente 
            self.primero.anterior = None
            self.size -= 1
    

    #recorrer final
    def mostrar_productos(self):  #funcion para mostrar producto
        aux = self.ultimo               #auxiliar apunta a self.ultimo
        while aux:
            print(f"[]>>[{aux.dato}]")      #ESTO ES PARA EL FORMATO EN VERTICAL 
            aux = aux.anterior


#mMenú en orden de compra  #MENU 
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCola()
        while opcion != 4:
            print("--- Lista de compra de productos ---\n 1. Agregar al final\n 2. Eliminar inicio\n 3. mostrar_productos \n 4. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_producto(dato)

            elif opcion == 2:
                lista.eliminar_producto()
            
            elif opcion == 3:
                lista.mostrar_productos()
            
            elif opcion == 4:
                print("Fin del programa")
            else:
                print("Opcion incorrecta, intente de nuevo")
except Exception as e:
    print(e)

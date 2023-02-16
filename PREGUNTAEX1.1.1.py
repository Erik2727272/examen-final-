class Cola:
    def _init_(self):
        self.items = []

    def Vacio(self):
        return self.items == []

    def Añadir(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def verificarTamaño(self):
        return len(self.items)

    def mostrar(self):
        
        print("Lista de compras")
        print(self.items)
            
def AñadirCompra():
    Añadir = input("Añadir compra: ")
    COLA_PRIMERO.Añadir(Añadir)

def eliminarCompra():
    print("Se quito:")
    print(c.avanzar())
    

#Programa Principal

COLA_PRIMERO = Cola()
while True:
    print("Menú")
    print("[1]AGREGAR AL FINAL ")
    print("[2]ELIMINAR INICIO")
    print("[3]mostrar compras")
    print("[0]salir")
    n = int(input("Ingrese opción: "))
    if n == 1:
        AñadirCompra()
    elif n == 2:
        eliminarCompra()
    elif n ==3:
        COLA_PRIMERO.mostrar()
    else:
        print("saliendo")
        break 
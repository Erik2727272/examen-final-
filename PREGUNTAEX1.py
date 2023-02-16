#Crea un programa en Python que 
# simule una lista de compras. 
# El programa debe permitir al 
# usuario agregar productos al
#  final de la lista, eliminar 
# productos del inicio de la lista
#  y mostrar todos los productos 
# en la lista en orden de compra.


lista_de_compras= [] #lista de compras
 
while True:
    print("BIENVENIDO ")
    acción = input("\n¿Qué deseas hacer? \n [1] Agregar producto\n [2] eliminar producto\n [3] mostrar productos \n") # Preguntamos qué desea hacer el usuario
    if acción == "1": # Si el usuario desea agregar
        producto = input("Nombre del producto: ") # Pedimos el nombre del producto
        lista_de_compras.append(producto) #Agregamos el producto al final de la lista
    elif acción == "2": # Si el usuario desea eliminar
        lista_de_compras.pop(0) #Eliminamos el elemento del principio de la lista
    elif acción == "3": #Si el usuario desea mostrar
        print(lista_de_compras)




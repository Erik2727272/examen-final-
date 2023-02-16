#2. Crea un programa en Python que mantenga un historial 
# de tareas pendientes. El programa debe permitir al usuario
#  agregar una tarea al inicio de la lista, eliminar una tarea del
#  final de la lista y mostrar todas las tareas en la lista en orden
#  inverso al que se agregaron. Además, el programa debe contar 
# la cantidad total de tareas en la lista y mostrar ese número al usuario.


# Definir una lista para almacenar las tareas 
tarea = []

# Define una función para agregar una tarea al comienzo de la lista
def agregar_tareas(task):
    tarea.insert(0, task)
    return "Tarea agregada exitosamente"

# Define una función para eliminar la última tarea de la lista
def eliminar_ultimatarea():
    if len(tarea) > 0: 
        tarea.pop()
        return "Última tarea eliminada exitosamente"
    else:
        return "No hay tareas en la lista"

def mostrartarea_inversa():
    for tarea in reversed(tarea):
        return tarea

def contar_tareas():
    print(len(tarea))     

# Define una función para mostrar la lista de tareas en orden inverso

#Definir una función para mostrar la cantidad de tareas en la lista 

#Define una función para ejecutar el programa 

while True:
    print("Menú")
    print("[1]Añadir tarea al inicio")
    print("[2]Quitar tarea del final")
    print("[3]Mostrar tareas inversa")
    print("[4]Contar tareas")
    print("[0]salir")
    n = int(input("Ingrese opción: "))
    if n == 1:
        tarea = input("Por favor ingrese la tarea a agregar: ") 
        tarea.agregar_tareas()

    elif n == 2:
        eliminar_ultimatarea()

    elif n == 2:    
        mostrartarea_inversa()

    elif n == 4:
        contar_tareas()

    else:
        break
    
from imprimir import ImprimirTodo

def Menu():
    print("################## MENU ##################" "\n1) Agregar alumno", "\n2) Agregar pedido", "\n3) Imprimir todo", "\4) Salir")
    Opc = int(input("Selecciona una opcion... "))


    if Opc != 4:
        Menu()    #<-------- RECURSIVIDAD

    elif Opc == 1:
        AgregarAlumno()
    elif Opc == 2:
        AgregarPedido()
    elif Opc == 3:
        ImprimirTodo()
    elif Opc == 4:
        print("El programa ha finalizado.")

Menu()
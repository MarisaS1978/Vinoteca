from funciones.alta_vinos import alta_vinos
from funciones.consulta_vinos import consulta_vinos
from funciones.modificar_vino import modificar_vino
from funciones.eliminar_vino import eliminar_vino
from funciones.listar_vinos import listar_vinos
from funciones.listar_min_stock import listar_vinos_min_stock

def menu(conexion):
    while True:
        print("\n         -----Menú de gestión de vinos----- \n")
        print("1- Alta de vinos.")
        print("2- Consulta de datos de vinos.")
        print("3- Modificar datos de vinos.")
        print("4- Baja de vinos.")
        print("5- Lista completa de vinos.")
        print("6- Lista de artículos con mínimo stock aceptable.")
        print("7- Salir.")

        opcion = input("Por favor, selecciona una de las opciones (entre 1 y 7): ")

        if opcion == '1':
            alta_vinos(conexion)
        elif opcion == '2':
            consulta_vinos(conexion)
        elif opcion == '3':
            modificar_vino(conexion)
        elif opcion == '4':
            eliminar_vino(conexion)
        elif opcion == '5':
            listar_vinos(conexion)
        elif opcion == '6':
            listar_vinos_min_stock(conexion)
        elif opcion == '7':
            print("Saliendo del programa....")
            break
        else:
            print("Opción incorrecta.")


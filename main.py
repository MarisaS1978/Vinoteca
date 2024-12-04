from base_datos.conexion import conectar
from base_datos.crear_tabla import crear_tabla
from interfaz.encabezado import mostrar_encabezado
from interfaz.menu import menu

if __name__ == "__main__":
    conexion = conectar()
    crear_tabla(conexion)
    mostrar_encabezado()
    menu(conexion)
    conexion.close()

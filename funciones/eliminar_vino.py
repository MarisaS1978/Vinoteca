def eliminar_vino(conexion):
    cursor = conexion.cursor()
    id_vino = input("Ingrese el ID del vino a eliminar: ").strip()
    if not id_vino.isdigit():
        print("El ID debe ser numérico.")
        return

    cursor.execute("SELECT * FROM vinos WHERE id = ?", (int(id_vino),))
    vino = cursor.fetchone()
    if vino:
        print(f"Información del vino a eliminar: ID: {vino[0]}, Nombre: {vino[1]}, Precio: $ {vino[2]}, Stock: {vino[3]}")
        confirmar = input("¿Está seguro de que desea eliminar este vino? (si/no): ").lower()
        if confirmar in ('si', 's'):
            cursor.execute("DELETE FROM vinos WHERE id = ?", (vino[0],))
            conexion.commit()
            print("Vino eliminado con éxito!")
        else:
            print("Eliminación cancelada.")
    else:
        print("Vino no encontrado con el ID proporcionado.")

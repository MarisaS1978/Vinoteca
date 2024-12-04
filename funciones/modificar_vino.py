def modificar_vino(conexion):
    cursor = conexion.cursor()
    id_vino = input("Ingrese el ID del vino a modificar: ").strip()
    if not id_vino.isdigit():
        print("El ID debe ser numérico.")
        return

    cursor.execute("SELECT * FROM vinos WHERE id = ?", (int(id_vino),))
    vino = cursor.fetchone()
    if vino:
        print(f"Información actual: ID: {vino[0]}, Nombre: {vino[1]}, Precio: $ {vino[2]}, Stock: {vino[3]}")
        nombre = input("Ingrese nuevo nombre (presione Enter para conservar el actual): ").strip() or vino[1]
        precio = input("Ingrese nuevo precio (presione Enter para conservar el actual): ").strip()
        precio = float(precio) if precio.replace('.', '', 1).isdigit() else vino[2]
        stock = input("Ingrese nuevo stock (presione Enter para conservar el actual): ").strip()
        stock = int(stock) if stock.isdigit() else vino[3]

        cursor.execute("UPDATE vinos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
                       (nombre.capitalize(), precio, stock, vino[0]))
        conexion.commit()
        print("Vino modificado con éxito!")
    else:
        print("Vino no encontrado con el ID proporcionado.")

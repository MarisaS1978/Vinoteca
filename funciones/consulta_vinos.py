def consulta_vinos(conexion):
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del vino a consultar: ").strip()
    while not nombre:
        print("Debe ingresar un nombre.")
        nombre = input("Ingrese el nombre del vino: ").strip()

    cursor.execute("SELECT * FROM vinos WHERE LOWER(nombre) = LOWER(?)", (nombre,))
    vino = cursor.fetchone()
    if vino:
        print(f"ID: {vino[0]}")
        print(f"Nombre: {vino[1]}")
        print(f"Precio: $ {vino[2]}")
        print(f"Stock: {vino[3]}")
    else:
        print("Vino no encontrado!")

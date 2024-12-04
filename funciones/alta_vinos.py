def alta_vinos(conexion):
    cursor = conexion.cursor()
    while True:
        print("1-Alta de vinos: ")
        nombre = input("Ingrese el nombre del vino: ").strip()
        precio = input("Ingrese el precio:$ ").strip()
        stock = input("Ingrese la cantidad en stock: ").strip()

        while not nombre:
            print("Debe ingresar nombre.")
            nombre = input("Ingrese nombre del vino: ").strip()
        while not precio or not precio.replace('.', '', 1).isdigit():
            print("Debe ingresar un precio válido.")
            precio = input("Ingrese el precio del vino: ").strip()
        while not stock or not stock.isdigit():
            print("Debe ingresar un stock válido.")
            stock = input("Ingrese el stock del vino: ").strip()

        # Verificar si el vino ya existe
        cursor.execute("SELECT * FROM vinos WHERE LOWER(nombre) = LOWER(?)", (nombre,))
        if cursor.fetchone():
            print(f"El vino {nombre} ya está registrado.")
        else:
            cursor.execute("INSERT INTO vinos (nombre, precio, stock) VALUES (?, ?, ?)",
                           (nombre.capitalize(), float(precio), int(stock)))
            conexion.commit()
            print(f"El vino {nombre} fue registrado con éxito!")

        seguir = input("¿Desea agregar otro vino? (si/no): ").lower()
        if seguir in ('n', 'no'):
            break

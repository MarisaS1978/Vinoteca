def listar_vinos_min_stock(conexion):
    """
    Lista los vinos cuyo stock sea menor al umbral definido por el usuario.
    """
    cursor = conexion.cursor()
    umbral_stock = input("Ingrese el umbral de stock aceptable: ").strip()
    if not umbral_stock.isdigit():
        print("El umbral debe ser un número.")
        return

    umbral_stock = int(umbral_stock)
    cursor.execute("SELECT * FROM vinos WHERE stock <= ?", (umbral_stock,))
    vinos_bajo_stock = cursor.fetchall()

    if not vinos_bajo_stock:
        print("No hay vinos con stock por debajo del umbral establecido.")
    else:
        print(f"Vinos con stock menor a {umbral_stock}:")
        print(f"{'ID':<5} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
        print("-" * 50)
        for vino in vinos_bajo_stock:
            print(f"{vino[0]:<5} {vino[1]:<20} ${vino[2]:<10} {vino[3]:<10}")

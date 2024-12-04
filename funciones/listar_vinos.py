def listar_vinos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM vinos")
    vinos = cursor.fetchall()
    if vinos:
        print(f"{'ID':<5} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
        print("-" * 50)
        for vino in vinos:
            print(f"{vino[0]:<5} {vino[1]:<20} ${vino[2]:<10} {vino[3]:<10}")
    else:
        print("No hay vinos registrados.")

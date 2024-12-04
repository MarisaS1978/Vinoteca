def mostrar_encabezado():
    NOMBRE = "Vinos Baco"
    DIRECCION = "Avda Gral Paz 1560 - CABA"
    TELEFONO = "4339-1698"
    linea = '-' * 70
    print(linea)
    print(f"{NOMBRE.upper():^60}")
    print(f"{DIRECCION.upper():^60}")
    print(f"{TELEFONO.upper():^60}")
    print(linea)

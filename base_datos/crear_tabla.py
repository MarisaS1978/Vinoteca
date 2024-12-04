def crear_tabla(conexion):
    """Crear la tabla de vinos si no existe."""
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)
    conexion.commit()
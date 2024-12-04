import sqlite3

def conectar():
    """Conectar a la base de datos SQLite y devolver la conexión."""
    return sqlite3.connect("maru.db")

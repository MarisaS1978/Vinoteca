 <p align="center">
  <a href="#español">🇦🇷 Español</a> |
  <a href="#english">🇬🇧 English</a>
</p>

---

<a id="español"></a>

# 🍷 Vinoteca — Sistema de gestión

**Aplicación desarrollada en Python para la gestión de una vinoteca.**

Este proyecto utiliza una estructura modular que separa la conexión y creación de la base de datos, las funciones del sistema y la interfaz de usuario.

El objetivo es organizar el código en componentes independientes, facilitando su mantenimiento, comprensión y futuras mejoras.

## 🛠️ Tecnologías y herramientas

- **Python:** lenguaje de programación.
- **SQLite:** almacenamiento local mediante una base de datos.
- **Programación modular:** separación de responsabilidades en distintos módulos.

## 📂 Estructura del proyecto

```text
Vinoteca/
│
├── base_datos/
│   ├── conexion.py
│   └── crear_tabla.py
│
├── funciones/
│   └── ...
│
├── interfaz/
│   ├── encabezado.py
│   └── menu.py
│
├── maru.db
└── main.py
```

## ⚙️ Funcionamiento general

El archivo `main.py` es el punto de entrada de la aplicación.

Al ejecutarse:

1. Establece la conexión con la base de datos.
2. Inicializa la estructura de tablas.
3. Muestra el encabezado de la aplicación.
4. Ejecuta el menú principal.
5. Cierra la conexión al finalizar.

## 🚀 Cómo ejecutar el proyecto

### Requisitos

- Python instalado.
- Archivos del repositorio descargados o clonados.

### Instalación

```bash
git clone https://github.com/MarisaS1978/Vinoteca.git
cd Vinoteca
```

### Ejecución

```bash
python main.py
```

## 🎯 Objetivos del proyecto

- Aplicar conocimientos de programación con Python.
- Organizar una aplicación mediante módulos.
- Implementar conexión y gestión de una base de datos.
- Desarrollar una interfaz para interactuar con el sistema.
- Practicar la integración de componentes de software.

## 👩‍💻 Autora

**Marisa Silvina Sandroni**

[GitHub](https://github.com/MarisaS1978) | [LinkedIn](https://www.linkedin.com/in/marisa-silvina-sandroni/)

---

<a id="english"></a>

# 🍷 Vinoteca — Management System

**A Python application developed for wine shop management.**

This project follows a modular architecture, separating database connection and initialization, system functions, and the user interface.

The goal is to organize the application into independent components, making the code easier to maintain, understand, and improve.

## 🛠️ Technologies and Tools

- **Python:** programming language.
- **SQLite:** local database storage.
- **Modular programming:** separation of responsibilities into different modules.

## 📂 Project Structure

```text
Vinoteca/
│
├── base_datos/
│   ├── conexion.py
│   └── crear_tabla.py
│
├── funciones/
│   └── ...
│
├── interfaz/
│   ├── encabezado.py
│   └── menu.py
│
├── maru.db
└── main.py
```

## ⚙️ General Workflow

The `main.py` file is the application's entry point.

When executed, it:

1. Establishes a database connection.
2. Initializes the database tables.
3. Displays the application header.
4. Runs the main menu.
5. Closes the database connection when finished.

## 🚀 How to Run the Project

### Requirements

- Python installed.
- Repository files downloaded or cloned.

### Installation

```bash
git clone https://github.com/MarisaS1978/Vinoteca.git
cd Vinoteca
```

### Run

```bash
python main.py
```

## 🎯 Project Goals

- Apply Python programming skills.
- Organize an application using modular architecture.
- Implement database connectivity and management.
- Develop an interface to interact with the system.
- Practice software component integration.

## 👩‍💻 Author

**Marisa Silvina Sandroni**

[GitHub](https://github.com/MarisaS1978) | [LinkedIn](https://www.linkedin.com/in/marisa-silvina-sandroni/)

---

*Project developed as part of my programming and software development learning journey.*

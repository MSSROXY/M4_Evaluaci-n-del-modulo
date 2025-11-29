# 📚 Sistema de Gestión de Biblioteca en Python

Este proyecto implementa un sistema de gestión de libros utilizando **Programación Orientada a Objetos (OOP)** y **manejo de archivos** en Python.  
El programa permite administrar libros físicos y digitales, registrarlos, buscarlos, prestar o devolverlos, y guardar la información en un archivo de texto.

---

## 🧩 Estructura del Proyecto

El sistema se compone de tres clases principales:

### **1. Clase `Libro`**
Representa un libro físico.

**Atributos:**
- `titulo`
- `autor`
- `anio`
- `estado` (Disponible / Prestado)

---

### **2. Clase `LibroDigital` (hereda de `Libro`)**
Extiende la clase `Libro`.

**Atributo adicional:**
- `formato` (PDF, ePub, etc.)

**Métodos:**
- Getters y setters para `formato`
- `__str__()` sobrescrito para mostrar también el formato

---

### **3. Clase `Biblioteca`**
Gestiona una lista de objetos `Libro` y `LibroDigital`.

**Funciones principales:**
- Agregar libros
- Eliminar libros
- Listar libros
- Buscar por título
- Marcar como prestado
- Devolver libros
- Cargar libros desde `biblioteca.txt`
- Guardar cambios en `biblioteca.txt`

---

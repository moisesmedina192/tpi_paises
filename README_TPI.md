# Gestión de Datos de Países en Python

## Trabajo Práctico Integrador - Programación 1

### Alumno

Moises Alejandro Medina Rivero

---

# Descripción General

Este proyecto consiste en el desarrollo de una aplicación de consola en Python para la gestión de información de países mediante el uso de listas, diccionarios, funciones y archivos CSV.

La aplicación permite almacenar, consultar y analizar información geográfica y demográfica de distintos países, implementando funcionalidades de búsqueda, filtrado, ordenamiento y generación de estadísticas.

El objetivo principal es aplicar los conceptos fundamentales estudiados durante la materia Programación 1, desarrollando una solución modular, organizada y robusta.

---

# Objetivos del Proyecto

* Aplicar estructuras de datos como listas y diccionarios.
* Implementar funciones para modularizar el código.
* Utilizar archivos CSV para persistencia de datos.
* Realizar búsquedas y filtrados sobre conjuntos de información.
* Implementar ordenamientos según distintos criterios.
* Generar estadísticas básicas a partir de los datos almacenados.
* Aplicar validaciones y manejo de errores.

---

# Estructura de Datos

Cada país se representa mediante un diccionario con la siguiente estructura:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

Todos los países se almacenan dentro de una lista principal que permite recorrer, filtrar y ordenar la información de manera eficiente.

---

# Funcionalidades Implementadas

## Gestión de Países

* Mostrar todos los países almacenados.
* Agregar nuevos países.
* Actualizar población y superficie de un país.
* Buscar países por nombre.

## Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

## Ordenamientos

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Mostrar resultados en orden ascendente o descendente.

## Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

# Tecnologías Utilizadas

* Python 3
* CSV (Comma Separated Values)
* Visual Studio Code
* GitHub

---

# Archivo de Datos

La aplicación trabaja con un archivo llamado:

```text
paises.csv
```

Este archivo almacena los datos de los países y permite conservar la información entre ejecuciones del programa.

---

# Validaciones Implementadas

La aplicación incorpora diferentes mecanismos de validación para evitar errores durante su ejecución:

* Control de archivos CSV inexistentes.
* Validación de datos numéricos.
* Control de nombres vacíos.
* Prevención de países duplicados.
* Búsquedas sin distinción entre mayúsculas y minúsculas.
* Búsquedas compatibles con nombres escritos con o sin acentos.
* Manejo de excepciones mediante estructuras try/except.

---

# Conceptos Aplicados

Durante el desarrollo del proyecto se utilizaron los siguientes conceptos de Programación 1:

* Listas
* Diccionarios
* Funciones
* Estructuras condicionales
* Estructuras repetitivas
* Archivos CSV
* Ordenamientos
* Estadísticas básicas
* Modularización
* Manejo de errores

---

# Ejemplos de Uso

### Búsqueda de País

Entrada:

```text
espana
```

Resultado:

```text
España
Población: 47450795
Superficie: 505990 km²
Continente: Europa
```

### Filtrado por Continente

Entrada:

```text
america
```

Resultado:

```text
Argentina
Brasil
Chile
Perú
Uruguay
Paraguay
...
```

---

# Conclusión

Este proyecto permitió integrar los principales contenidos desarrollados en la materia Programación 1 mediante la construcción de una aplicación funcional y organizada. Se aplicaron estructuras de datos, funciones, archivos CSV, técnicas de búsqueda, filtrado, ordenamiento y generación de estadísticas, fortaleciendo tanto la lógica de programación como las buenas prácticas de desarrollo.

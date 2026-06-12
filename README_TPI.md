# Gestión de Datos de Países en Python

## Trabajo Práctico Integrador - Programación 1

### Integrantes

* Nombre Apellido
* Nombre Apellido

---

## Descripción del Proyecto

Este proyecto consiste en una aplicación desarrollada en Python para la gestión de información de países mediante el uso de listas, diccionarios, funciones y archivos CSV.

El sistema permite cargar, consultar, actualizar y analizar datos de distintos países, proporcionando herramientas de búsqueda, filtrado, ordenamiento y generación de estadísticas.

El objetivo principal es aplicar los conceptos estudiados en la materia Programación 1, desarrollando una solución modular, robusta y fácil de utilizar.

---

## Estructura de Datos

Cada país se almacena como un diccionario con la siguiente estructura:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

Todos los países se almacenan dentro de una lista.

---

## Funcionalidades

### Gestión de Países

* Mostrar todos los países.
* Agregar nuevos países.
* Actualizar población y superficie.
* Buscar países por nombre.

### Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

### Ordenamientos

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Orden ascendente y descendente.

### Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

## Tecnologías Utilizadas

* Python 3
* CSV
* Visual Studio Code

---

## Requisitos

Tener instalado:

* Python 3.10 o superior

Verificar instalación:

```bash
python --version
```

---

## Ejecución

Ubicarse dentro de la carpeta del proyecto y ejecutar:

```bash
python main.py
```

o

```bash
python3 main.py
```

---

## Archivo CSV

El sistema utiliza un archivo llamado:

```text
paises.csv
```

El mismo contiene la información base de los países.

Ejemplo:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
España,47450795,505990,Europa
```

---

## Validaciones Implementadas

* No permite nombres vacíos.
* No permite países duplicados.
* Controla errores de lectura del CSV.
* Controla errores de formato.
* Maneja búsquedas sin resultados.
* Valida valores numéricos.
* Permite búsquedas ignorando mayúsculas, minúsculas y acentos.

---

## Ejemplos de Uso

### Buscar un país

Entrada:

```text
espana
```

Salida:

```text
España
Población: 47450795
Superficie: 505990
Continente: Europa
```

### Filtrar por continente

Entrada:

```text
america
```

Salida:

```text
Argentina
Brasil
Chile
Peru
...
```

---

## Aprendizajes Aplicados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

* Listas
* Diccionarios
* Funciones
* Condicionales
* Ciclos repetitivos
* Archivos CSV
* Ordenamientos
* Estadísticas básicas
* Manejo de errores

---

## Repositorio

Agregar aquí el enlace al repositorio GitHub:

https://github.com/USUARIO/REPOSITORIO

---

## Video Demostración

Agregar aquí el enlace al video:

https://LINK-DEL-VIDEO

---

## Conclusión

Este proyecto permitió integrar los principales contenidos desarrollados en la materia Programación 1, aplicando estructuras de datos, modularización, lectura de archivos CSV y análisis estadístico. Además, se fortalecieron las buenas prácticas de programación mediante el desarrollo de un sistema robusto, organizado y fácil de mantener.

import csv
import os
import unicodedata


ARCHIVO_CSV = "paises.csv"


# ==================================================
# FUNCIONES DE UTILIDAD
# ==================================================

def normalizar_texto(texto):
    """
    Convierte un texto a minúsculas y elimina acentos
    para facilitar búsquedas y comparaciones.
    """

    texto = texto.strip().lower()

    texto = ''.join(
        caracter
        for caracter in unicodedata.normalize('NFD', texto)
        if unicodedata.category(caracter) != 'Mn'
    )

    return texto


def crear_csv_si_no_existe():
    """
    Crea un CSV base si no existe.
    """

    if not os.path.exists(ARCHIVO_CSV):

        with open(
            ARCHIVO_CSV,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow(
                ["nombre", "poblacion", "superficie", "continente"]
            )

            escritor.writerow(
                ["Argentina", 45376763, 2780400, "America"]
            )

            escritor.writerow(
                ["Brasil", 213993437, 8515767, "America"]
            )

            escritor.writerow(
                ["Chile", 19603733, 756102, "America"]
            )

            escritor.writerow(
                ["Peru", 33715471, 1285216, "America"]
            )

            escritor.writerow(
                ["Japon", 125800000, 377975, "Asia"]
            )

            escritor.writerow(
                ["Alemania", 83149300, 357022, "Europa"]
            )

            escritor.writerow(
                ["España", 47450795, 505990, "Europa"]
            )

            escritor.writerow(
                ["Australia", 25687041, 7692024, "Oceania"]
            )


# ==================================================
# CARGA Y GUARDADO
# ==================================================

def cargar_paises():
    """
    Lee el CSV y devuelve una lista de diccionarios.
    """

    paises = []

    try:

        with open(
            ARCHIVO_CSV,
            mode="r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:

                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except (ValueError, KeyError):
                    print(
                        "Advertencia: registro inválido ignorado."
                    )

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")

    return paises


def guardar_paises(paises):
    """
    Guarda todos los países en el CSV.
    """

    with open(
        ARCHIVO_CSV,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


# ==================================================
# BÚSQUEDAS
# ==================================================

def buscar_pais_exacto(paises, nombre):

    nombre = normalizar_texto(nombre)

    for pais in paises:

        if normalizar_texto(
            pais["nombre"]
        ) == nombre:

            return pais

    return None


def buscar_paises_parcial(paises, texto):

    texto = normalizar_texto(texto)

    resultados = []

    for pais in paises:

        if texto in normalizar_texto(
            pais["nombre"]
        ):

            resultados.append(pais)

    return resultados


# ==================================================
# VALIDACIONES
# ==================================================

def validar_entero_positivo(mensaje):

    while True:

        try:

            valor = int(input(mensaje))

            if valor < 0:
                raise ValueError

            return valor

        except ValueError:
            print(
                "Error: debe ingresar un número entero válido."
            )
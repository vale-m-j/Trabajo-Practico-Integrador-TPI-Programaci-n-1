<<<<<<< Updated upstream
=======

import csv
import os

# Constantes
ARCHIVO_PAISES = "paises.csv"

# Validaciones
def es_numero(valor):
   
    return valor.isdigit() and int(valor) > 0

def obtener_input_no_vacio(mensaje):
   
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío.")

# Gestión de archivos
def cargar_datos():
    
    paises = []

    if not os.path.exists(ARCHIVO_PAISES):
        return paises

    with open(ARCHIVO_PAISES, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for fila in reader:
            try:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                paises.append(fila)

            except ValueError:
                print(f"Error de formato en el registro: {fila}")

    return paises


def guardar_datos(paises):
    
    with open(ARCHIVO_PAISES, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["nombre", "poblacion", "superficie", "continente"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(paises)


#  Agregar, Buscar, Actualizar.
def agregar_pais(paises):

    print("\n--- Agregar nuevo país ---")

    nombre = obtener_input_no_vacio("Nombre: ")

    # Verificar que no exista
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Error: El país ya existe.")
            return

    pob = input("Población: ")

    while not es_numero(pob):
        pob = input("Error. Ingrese una población válida: ")

    sup = input("Superficie: ")

    while not es_numero(sup):
        sup = input("Error. Ingrese una superficie válida: ")

    cont = obtener_input_no_vacio("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(pob),
        "superficie": int(sup),
        "continente": cont
    }

    paises.append(nuevo_pais)

    guardar_datos(paises)

    print("País agregado exitosamente.")


def buscar_pais(paises):

    busqueda = input("\nIngrese nombre del país a buscar: ").strip()

    if not busqueda:
        print("Error: Debe ingresar un nombre.")
        return

    encontrados = []

    for p in paises:
        if busqueda.lower() in p["nombre"].lower():
            encontrados.append(p)

    if encontrados:
        print("\nResultados encontrados:")

        for p in encontrados:
            print(
                f"{p['nombre']} | "
                f"Población: {p['poblacion']} | "
                f"Superficie: {p['superficie']} | "
                f"Continente: {p['continente']}"
            )

    else:
        print("No se encontraron resultados.")


def actualizar_pais(paises):

    nombre = input(
        "\nIngrese el nombre del país a actualizar: "
    ).strip().lower()

    for p in paises:

        if p["nombre"].lower() == nombre:

            nueva_pob = input(
                f"Nueva población (actual: {p['poblacion']}): "
            )

            while not es_numero(nueva_pob):
                nueva_pob = input(
                    "Error. Ingrese una población válida: "
                )

            nueva_sup = input(
                f"Nueva superficie (actual: {p['superficie']}): "
            )

            while not es_numero(nueva_sup):
                nueva_sup = input(
                    "Error. Ingrese una superficie válida: "
                )

            p["poblacion"] = int(nueva_pob)
            p["superficie"] = int(nueva_sup)

            guardar_datos(paises)

            print("Datos actualizados correctamente.")
            return

    print("País no encontrado.")
>>>>>>> Stashed changes

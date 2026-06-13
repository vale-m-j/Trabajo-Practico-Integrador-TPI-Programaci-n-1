import csv
import os

# Nombre del archivo CSV
archivo_paises = "paises.csv"


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

    if not os.path.exists(archivo_paises):
        return paises

    with open(archivo_paises, mode="r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            try:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])

                paises.append(fila)

            except ValueError:
                print(f"Error de formato en el registro: {fila}")

    return paises


def guardar_datos(paises):

    with open(
        archivo_paises,
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
        escritor.writerows(paises)


# Agregar país
def agregar_pais(paises):

    print("\n-- Agregar nuevo país --")

    nombre = obtener_input_no_vacio("Nombre: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: El país ya existe.")
            return

    poblacion = input("Población: ")

    while not es_numero(poblacion):
        poblacion = input(
            "Error. Ingrese una población válida: "
        )

    superficie = input("Superficie: ")

    while not es_numero(superficie):
        superficie = input(
            "Error. Ingrese una superficie válida: "
        )

    continente = obtener_input_no_vacio(
        "Continente: "
    )

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_datos(paises)

    print("País agregado exitosamente.")


# Buscar país
def buscar_pais(paises):

    busqueda = input(
        "\nIngrese nombre del país a buscar: "
    ).strip()

    if not busqueda:
        print("Error: Debe ingresar un nombre.")
        return

    encontrados = []

    for pais in paises:

        if busqueda.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if encontrados:

        print("\nResultados encontrados:\n")

        for pais in encontrados:

            print(
                f"{pais['nombre']} | "
                f"Población: {pais['poblacion']} | "
                f"Superficie: {pais['superficie']} | "
                f"Continente: {pais['continente']}"
            )

    else:
        print("No se encontraron resultados.")


# Actualizar país
def actualizar_pais(paises):

    nombre = input(
        "\nIngrese el nombre del país a actualizar: "
    ).strip().lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            nueva_poblacion = input(
                f"Nueva población "
                f"(actual: {pais['poblacion']}): "
            )

            while not es_numero(nueva_poblacion):
                nueva_poblacion = input(
                    "Error. Ingrese una población válida: "
                )

            nueva_superficie = input(
                f"Nueva superficie "
                f"(actual: {pais['superficie']}): "
            )

            while not es_numero(nueva_superficie):
                nueva_superficie = input(
                    "Error. Ingrese una superficie válida: "
                )

            pais["poblacion"] = int(nueva_poblacion)
            pais["superficie"] = int(nueva_superficie)

            guardar_datos(paises)

            print(
                "Datos actualizados correctamente."
            )

            return

    print("País no encontrado.")

    # -- Menú Principal --
def menu():
    # Cargamos los datos una sola vez al iniciar
    lista_paises = cargar_datos()
    
    while True:
        print("\n-- Gestión de países ---")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Actualizar país")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_pais(lista_paises)
        elif opcion == "2":
            buscar_pais(lista_paises)
        elif opcion == "3":
            actualizar_pais(lista_paises)
        elif opcion == "4":
            print("Sistema finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()

    
   
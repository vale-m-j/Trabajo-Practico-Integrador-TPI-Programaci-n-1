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

# Función auxiliar para validar solo letras
def es_texto(valor):
    return valor.replace(" ", "").isalpha()

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
    with open(archivo_paises, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

# Agregar país
def agregar_pais(paises):
    print("\n-- Agregar nuevo país --")
    
    nombre = obtener_input_no_vacio("Nombre: ")
    while not es_texto(nombre):
        print("Error: El nombre debe contener solo letras.")
        nombre = obtener_input_no_vacio("Nombre: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: El país ya existe.")
            return

    poblacion = input("Población: ")
    while not es_numero(poblacion):
        poblacion = input("Error. Ingrese una población válida (número positivo): ")

    superficie = input("Superficie: ")
    while not es_numero(superficie):
        superficie = input("Error. Ingrese una superficie válida (número positivo): ")

    continente = obtener_input_no_vacio("Continente: ")
    while not es_texto(continente):
        print("Error: El continente debe contener solo letras.")
        continente = obtener_input_no_vacio("Continente: ")

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
    busqueda = input("\nIngrese nombre del país a buscar: ").strip()
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
            print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
    else:
        print("No se encontraron resultados.")

# Actualizar país
def actualizar_pais(paises):
    nombre = input("\nIngrese el nombre del país a actualizar: ").strip().lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            nueva_poblacion = input(f"Nueva población (actual: {pais['poblacion']}): ")
            while not es_numero(nueva_poblacion):
                nueva_poblacion = input("Error. Ingrese una población válida: ")
            
            nueva_superficie = input(f"Nueva superficie (actual: {pais['superficie']}): ")
            while not es_numero(nueva_superficie):
                nueva_superficie = input("Error. Ingrese una superficie válida: ")
            
            pais["poblacion"] = int(nueva_poblacion)
            pais["superficie"] = int(nueva_superficie)
            guardar_datos(paises)
            print("Datos actualizados correctamente.")
            return
    print("País no encontrado.")

# Filtros
def filtrar_continente(paises):
    continente = input("\nIngrese continente: ").strip().lower()
    encontrados = []
    for pais in paises:
        if pais["continente"].lower() == continente:
            encontrados.append(pais)
    if encontrados:
        print("\nPaíses encontrados:\n")
        for pais in encontrados:
            print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
    else:
        print("No se encontraron países.")

def filtrar_poblacion(paises):
    minimo = input("\nPoblación mínima: ")
    while not minimo.isdigit():
        minimo = input("Error. Ingrese un número válido: ")
    maximo = input("Población máxima: ")
    while not maximo.isdigit():
        maximo = input("Error. Ingrese un número válido: ")
    
    try:
        minimo = int(minimo)
        maximo = int(maximo)
        if minimo > maximo:
            print("Error: la población mínima no puede ser mayor que la máxima.")
            return
        encontrados = []
        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                encontrados.append(pais)
        if encontrados:
            print("\nPaíses encontrados:\n")
            for pais in encontrados:
                print(f"{pais['nombre']} | Población: {pais['poblacion']}")
        else:
            print("No se encontraron países.")
    except ValueError:
        print("Error inesperado en los valores.")

def filtrar_superficie(paises):
    minimo = input("\nSuperficie mínima: ")
    while not minimo.isdigit():
        minimo = input("Error. Ingrese un número válido: ")
    maximo = input("Superficie máxima: ")
    while not maximo.isdigit():
        maximo = input("Error. Ingrese un número válido: ")
    
    try:
        minimo = int(minimo)
        maximo = int(maximo)
        if minimo > maximo:
            print("Error: la superficie mínima no puede ser mayor que la máxima.")
            return
        encontrados = []
        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                encontrados.append(pais)
        if encontrados:
            print("\nPaíses encontrados:\n")
            for pais in encontrados:
                print(f"{pais['nombre']} | Superficie: {pais['superficie']}")
        else:
            print("No se encontraron países.")
    except ValueError:
        print("Error inesperado en los valores.")

# Estadísticas
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No existen países cargados para generar estadísticas.")
        return
    mayor = max(paises, key=lambda pais: pais["poblacion"])
    menor = min(paises, key=lambda pais: pais["poblacion"])
    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    print("\n--- Estadísticas ---")
    print(f"Mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("\nCantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")

# Ordenamientos
def ordenar_nombre(paises):
    ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower())
    print("\nPaíses ordenados por nombre:\n")
    for pais in ordenados:
        print(pais["nombre"])

def ordenar_poblacion(paises):
    orden = input("1. Ascendente\n2. Descendente\nSeleccione: ")
    descendente = orden == "2"
    ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
    print("\nPaíses ordenados por población:\n")
    for pais in ordenados:
        print(f"{pais['nombre']} - {pais['poblacion']}")

def ordenar_superficie(paises):
    orden = input("1. Ascendente\n2. Descendente\nSeleccione: ")
    descendente = orden == "2"
    ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
    print("\nPaíses ordenados por superficie:\n")
    for pais in ordenados:
        print(f"{pais['nombre']} - {pais['superficie']}")

# Menú Principal
def menu():
    lista_paises = cargar_datos()
    while True:
        print("\n-- Gestión de países ---")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Actualizar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar por nombre")
        print("8. Ordenar por población")
        print("9. Ordenar por superficie")
        print("10. Mostrar estadísticas")
        print("11. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_pais(lista_paises)
        elif opcion == "2":
            buscar_pais(lista_paises)
        elif opcion == "3":
            actualizar_pais(lista_paises)
        elif opcion == "4":
            filtrar_continente(lista_paises)
        elif opcion == "5":
            filtrar_poblacion(lista_paises)
        elif opcion == "6":
            filtrar_superficie(lista_paises)
        elif opcion == "7":
            ordenar_nombre(lista_paises)
        elif opcion == "8":
            ordenar_poblacion(lista_paises)
        elif opcion == "9":
            ordenar_superficie(lista_paises)
        elif opcion == "10":
            mostrar_estadisticas(lista_paises)
        elif opcion == "11":
            print("Sistema finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
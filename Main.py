# Filtros
def filtrar_continente(paises):

    continente = input(
        "\nIngrese continente: "
    ).strip().lower()

    encontrados = []

    for pais in paises:

        if pais["continente"].lower() == continente:
            encontrados.append(pais)

    if encontrados:

        print("\nPaíses encontrados:\n")

        for pais in encontrados:

            print(
                f"{pais['nombre']} | "
                f"Población: {pais['poblacion']} | "
                f"Superficie: {pais['superficie']} | "
                f"Continente: {pais['continente']}"
            )

    else:
        print("No se encontraron países.")


def filtrar_poblacion(paises):

    minimo = input(
        "\nPoblación mínima: "
    )

    while not minimo.isdigit():

        minimo = input(
            "Error. Ingrese un número válido: "
        )

    maximo = input(
        "Población máxima: "
    )

    while not maximo.isdigit():

        maximo = input(
            "Error. Ingrese un número válido: "
        )

    minimo = int(minimo)
    maximo = int(maximo)

    if minimo > maximo:

        print(
            "Error: la población mínima no puede "
            "ser mayor que la máxima."
        )

        return

    encontrados = []

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            encontrados.append(pais)

    if encontrados:

        print("\nPaíses encontrados:\n")

        for pais in encontrados:

            print(
                f"{pais['nombre']} | "
                f"Población: {pais['poblacion']}"
            )

    else:
        print("No se encontraron países.")


def filtrar_superficie(paises):

    minimo = input(
        "\nSuperficie mínima: "
    )

    while not minimo.isdigit():

        minimo = input(
            "Error. Ingrese un número válido: "
        )

    maximo = input(
        "Superficie máxima: "
    )

    while not maximo.isdigit():

        maximo = input(
            "Error. Ingrese un número válido: "
        )

    minimo = int(minimo)
    maximo = int(maximo)

    if minimo > maximo:

        print(
            "Error: la superficie mínima no puede "
            "ser mayor que la máxima."
        )

        return

    encontrados = []

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            encontrados.append(pais)

    if encontrados:

        print("\nPaíses encontrados:\n")

        for pais in encontrados:

            print(
                f"{pais['nombre']} | "
                f"Superficie: {pais['superficie']}"
            )

    else:
        print("No se encontraron países.")

# Estadísticas
def mostrar_estadisticas(paises):

    if len(paises) == 0:

        print(
            "No existen países cargados "
            "para generar estadísticas."
        )

        return

    mayor = max(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    menor = min(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    promedio_poblacion = (
        sum(
            pais["poblacion"]
            for pais in paises
        ) / len(paises)
    )

    promedio_superficie = (
        sum(
            pais["superficie"]
            for pais in paises
        ) / len(paises)
    )

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n--- Estadísticas ---")

    print(
        f"Mayor población: "
        f"{mayor['nombre']} "
        f"({mayor['poblacion']})"
    )

    print(
        f"Menor población: "
        f"{menor['nombre']} "
        f"({menor['poblacion']})"
    )

    print(
        f"Promedio de población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():

        print(
            f"{continente}: "
            f"{cantidad}"
        )

# Ordenamientos
def ordenar_nombre(paises):

    ordenados = sorted(
        paises,
        key=lambda pais: pais["nombre"].lower()
    )

    print("\nPaíses ordenados por nombre:\n")

    for pais in ordenados:

        print(pais["nombre"])


def ordenar_poblacion(paises):

    orden = input(
        "1. Ascendente\n"
        "2. Descendente\n"
        "Seleccione: "
    )

    descendente = orden == "2"

    ordenados = sorted(
        paises,
        key=lambda pais: pais["poblacion"],
        reverse=descendente
    )

    print("\nPaíses ordenados por población:\n")

    for pais in ordenados:

        print(
            f"{pais['nombre']} - "
            f"{pais['poblacion']}"
        )


def ordenar_superficie(paises):

    orden = input(
        "1. Ascendente\n"
        "2. Descendente\n"
        "Seleccione: "
    )

    descendente = orden == "2"

    ordenados = sorted(
        paises,
        key=lambda pais: pais["superficie"],
        reverse=descendente
    )

    print("\nPaíses ordenados por superficie:\n")

    for pais in ordenados:

        print(
            f"{pais['nombre']} - "
            f"{pais['superficie']}"
        )

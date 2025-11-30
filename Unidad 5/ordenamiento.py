def parse_input_lista(s):
    # convierte "1, 2,3" o "1 2 3" a lista de enteros
    s = s.replace(",", " ").strip()
    if not s:
        return []
    return [int(x) for x in s.split()]

# ------------------ Burbuja con traza ------------------ #
def burbuja_traza(arreglo, verbose=True):
    n = len(arreglo)
    comparaciones = 0
    intercambios = 0
    iteraciones_externas = 0

    if verbose:
        print("\n--- BURBUJA (traza paso a paso) ---")
        print("Estado inicial:", arreglo)

    for i in range(n):
        iteraciones_externas += 1
        if verbose:
            print(f"\nPasada externa {iteraciones_externas} (i={i}):")
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if verbose:
                print(f"  Comparación #{comparaciones}: arreglo[{j}]={arreglo[j]} ? arreglo[{j+1}]={arreglo[j+1]}", end="")
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambios += 1
                swapped = True
                if verbose:
                    print(f" -> intercambio (ahora: {arreglo})")
            else:
                if verbose:
                    print(" -> no hay intercambio")
        if not swapped and verbose:
            print("  No se realizaron intercambios en esta pasada; el arreglo ya está ordenado (optimización).")
            # Podemos romper si queremos optimización; se deja así para mostrar que se detectó.
            break

    if verbose:
        print("\nResultado final:", arreglo)
        print(f"Comparaciones totales: {comparaciones}")
        print(f"Intercambios totales: {intercambios}")
        print(f"Iteraciones externas realizadas: {iteraciones_externas}")
    return arreglo, comparaciones, intercambios, iteraciones_externas

# ------------------ Inserción con traza ------------------ #
def insercion_traza(arreglo, verbose=True):
    comparaciones = 0
    movimientos = 0   # desplazamientos hacia la derecha
    iteraciones_externas = 0

    if verbose:
        print("\n--- INSERCIÓN (traza paso a paso) ---")
        print("Estado inicial:", arreglo)

    for i in range(1, len(arreglo)):
        iteraciones_externas += 1
        clave = arreglo[i]
        j = i - 1
        if verbose:
            print(f"\nIteración externa {iteraciones_externas} (i={i}): tomar clave={clave} desde índice {i}")

        # contaremos la comparación inicial que decide entrar o no al while
        primera_comparacion = True
        while j >= 0:
            comparaciones += 1
            if verbose:
                print(f"  Comparación #{comparaciones}: clave({clave}) ? arreglo[{j}]={arreglo[j]}", end="")
            if arreglo[j] > clave:
                arreglo[j + 1] = arreglo[j]  # desplazar hacia la derecha
                movimientos += 1
                if verbose:
                    print(f" -> desplazar {arreglo[j]} a la derecha (índice {j+1}), estado: {arreglo}")
                j -= 1
                primera_comparacion = False
            else:
                if verbose:
                    print(" -> no desplazar (posición encontrada)")
                break

        # si el while no se ejecutó por j<0, aún contamos la comparación final que falló (si aplica)
        if j < 0 and primera_comparacion:
            # en caso que no haya elementos a la izquierda se cuenta comparación? depende de la convención;
            # aquí no sumamos extra porque no hubo comparación con elemento existente.
            pass

        arreglo[j + 1] = clave
        if verbose:
            print(f"  Insertar clave={clave} en índice {j+1}, estado: {arreglo}")

    if verbose:
        print("\nResultado final:", arreglo)
        print(f"Comparaciones totales: {comparaciones}")
        print(f"Movimientos (desplazamientos) totales: {movimientos}")
        print(f"Iteraciones externas realizadas: {iteraciones_externas}")
    return arreglo, comparaciones, movimientos, iteraciones_externas

# ------------------ Selección con traza ------------------ #
def seleccion_traza(arreglo, verbose=True):
    n = len(arreglo)
    comparaciones = 0
    intercambios = 0
    iteraciones_externas = 0

    if verbose:
        print("\n--- SELECCIÓN (traza paso a paso) ---")
        print("Estado inicial:", arreglo)

    for i in range(n):
        iteraciones_externas += 1
        minimo = i
        if verbose:
            print(f"\nIteración externa {iteraciones_externas} (i={i}): buscar mínimo desde índice {i} hasta {n-1}")
        for j in range(i + 1, n):
            comparaciones += 1
            if verbose:
                print(f"  Comparación #{comparaciones}: arreglo[{j}]={arreglo[j]} ? arreglo[{minimo}]={arreglo[minimo]}", end="")
            if arreglo[j] < arreglo[minimo]:
                minimo = j
                if verbose:
                    print(f" -> nuevo mínimo en índice {minimo}")
            else:
                if verbose:
                    print(" -> no cambia mínimo")
        if minimo != i:
            if verbose:
                print(f"  Intercambio: poner el mínimo arreglo[{minimo}]={arreglo[minimo]} en la posición {i}")
            arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
            intercambios += 1
            if verbose:
                print(f"  Estado tras intercambio: {arreglo}")
        else:
            if verbose:
                print("  No se requiere intercambio en esta iteración (el elemento ya es el mínimo).")

    if verbose:
        print("\nResultado final:", arreglo)
        print(f"Comparaciones totales: {comparaciones}")
        print(f"Intercambios totales: {intercambios}")
        print(f"Iteraciones externas realizadas: {iteraciones_externas}")
    return arreglo, comparaciones, intercambios, iteraciones_externas

# ------------------ Menú interactivo ------------------ #
def menu():
    while True:
        print("\n=== MENÚ: Métodos de ordenamiento con traza ===")
        print("1 - Burbuja (Bubble Sort)")
        print("2 - Inserción (Insertion Sort)")
        print("3 - Selección (Selection Sort)")
        print("4 - Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "4":
            print("Saliendo...")
            break

        raw = input("Ingresa la lista de números (separados por comas o espacios), por ejemplo: 5, 3, 8, 1\n> ")
        try:
            lista = parse_input_lista(raw)
        except Exception as e:
            print("Entrada no válida. Asegúrate de ingresar solo números separados por comas o espacios.")
            continue

        if not lista:
            print("La lista está vacía. Intenta de nuevo.")
            continue

        # preguntar si quiere ver la traza paso a paso
        respuesta_traza = input("¿Mostrar traza paso a paso? (s/n): ").strip().lower()
        verbose = respuesta_traza == "s"

        # copiar la lista si queremos preservar el original para mostrarlo después
        lista_inicial = lista.copy()

        if opcion == "1":
            resultado = burbuja_traza(lista, verbose=verbose)
            metodo = "Burbuja"
        elif opcion == "2":
            resultado = insercion_traza(lista, verbose=verbose)
            metodo = "Inserción"
        elif opcion == "3":
            resultado = seleccion_traza(lista, verbose=verbose)
            metodo = "Selección"
        else:
            print("Opción inválida. Intenta de nuevo.")
            continue

        lista_final, compar, swaps, iter_ext = resultado
        print("\n--- RESUMEN ---")
        print("Método:", metodo)
        print("Lista original:", lista_inicial)
        print("Lista ordenada:", lista_final)
        print("Comparaciones totales:", compar)
        # Dependiendo del método el tercer valor puede ser movimientos o intercambios; lo mostramos genérico.
        print("Intercambios/Movimientos totales:", swaps)
        print("Iteraciones externas:", iter_ext)
        print("---------------\n")

if __name__ == "__main__":
    menu()

def seleccion(lista):
    print("Lista inicial:", lista)
    print("----- INICIANDO SELECCIÓN -----")

    n = len(lista)

    for i in range(n):
        min_index = i
        print(f"\nPasada {i + 1}: buscando el mínimo desde la posición {i}")

        for j in range(i + 1, n):
            print(f"  Comparando mínimo actual {lista[min_index]} con {lista[j]}")
            if lista[j] < lista[min_index]:
                print(f"  → Nuevo mínimo encontrado: {lista[j]}")
                min_index = j

        if min_index != i:
            print(f"  Intercambiando {lista[i]} con mínimo {lista[min_index]}")
            lista[i], lista[min_index] = lista[min_index], lista[i]
        else:
            print("  No se necesita intercambio")

        print("  Lista actual:", lista)

    print("\nLista final ordenada:", lista)
    return lista

tiempos = [15.2, 14.8, 16.0, 13.5, 15.0]
seleccion(tiempos)

def burbuja(lista):
    n = len(lista)
    print("Lista inicial:", lista)
    print("----- INICIANDO BURBUJA -----")

    for i in range(n - 1):
        print(f"\nPasada {i + 1}:")
        for j in range(n - 1 - i):
            print(f"  Comparando {lista[j]} y {lista[j+1]}")

            if lista[j] > lista[j + 1]:
                print(f"  → Intercambio: {lista[j]} ↔ {lista[j+1]}")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                print("  → No se intercambia")

            print("  Lista actual:", lista)

    print("\nLista final ordenada:", lista)
    return lista

calificaciones = [70, 85, 90, 60, 75, 95, 55]
burbuja(calificaciones)

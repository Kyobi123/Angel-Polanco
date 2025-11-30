def insercion(lista):
    print("Lista inicial:", lista)
    print("----- INICIANDO INSERCIÓN -----")

    for i in range(1, len(lista)):
        valor = lista[i]
        print(f"\nInsertando {valor}...")

        j = i - 1

        # Mover elementos mayores a la derecha
        while j >= 0 and lista[j] > valor:
            print(f"  {lista[j]} es mayor que {valor}, moviendo {lista[j]} a la derecha")
            lista[j + 1] = lista[j]
            j -= 1
            print("  Lista:", lista)

        lista[j + 1] = valor
        print(f"  → Insertado {valor} en la posición {j+1}")
        print("  Lista después de insertar:", lista)

    print("\nLista final ordenada:", lista)
    return lista

precios = [120, 80, 300, 150, 90]
insercion(precios)

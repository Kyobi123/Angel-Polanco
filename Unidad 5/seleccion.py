def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i  

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

tiempos = [15.2, 14.8, 16.0, 13.5, 15.0]
print("Tiempos origninales", tiempos)

resultado = seleccion(tiempos)
print("Tiempos ordenados:", resultado)

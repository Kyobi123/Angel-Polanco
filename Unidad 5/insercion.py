def insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor

    return lista

precios = [120, 80, 300, 150, 90]
print("Precios origniales", precios)

resultado = insercion(precios)
print("Precios ordenados:", resultado)

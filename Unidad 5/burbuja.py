def burbuja(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

calificaciones = [70, 85, 90, 60, 75, 95, 55]
print("Calificaciones originales:", calificaciones)
resultado = burbuja(calificaciones)

print("Calificaciones ordenadas:", resultado)

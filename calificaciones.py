# Creamos una lista con 5 valores, todos inicializados en cero
calificaciones = [0] * 5 

# Solicitamos 5 calificaciones
for i in range(5):
    calificaciones[i] = int(input(f"Captura la calificación {i+1}: "))

# Imprimimos las 5 calificaciones
print("\nLas calificaciones capturadas son:")
for i in range(5):
    print(f"Calificación {i+1}: {calificaciones[i]}")

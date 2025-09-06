calificaciones = [] # Se crea una lista vacía para almacenar datos

for i in range(6):
    calificacion = float(input(f"Ingrese la calificación {i+1}: ")) # Creamos el ciclo de iteración para que el usuario pueda colocar 6 calificaciones
    calificaciones.append(calificacion) # Se agrega a la lista

print("\nTus calificaciones son:")
print(calificaciones) # Se imprimien las calificaciones

promedio = sum(calificaciones) / len(calificaciones) # Se calcula el promedio
print(f"\nPromedio: {promedio:.2f}") # Se imprime el promedio y lo dejamos con 2 decimales
print(f"Calificación más alta: {max(calificaciones)}") # Mostramos la calificación más alta

print(f"Calificación más baja: {min(calificaciones)}") # Mostramos la calificación más baja

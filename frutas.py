frutas = [] # Creamos una lista vacía para almacenar datos luego

# Empezamos a agregar elementos a la lista
frutas.append("Mango") 
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uva")

# Imprimimos por primera vez la lista para checar que se guardaron los elementos
print(frutas)

# Eliminamos elementos a partir de su índice
frutas.pop(0) # Elimina el primer elemento de la lista 
frutas.pop(1) #Elimina el segundo elemento de la lista

# Agregamos un nuevo elemento a la lista
frutas.append("Sandias")

# Imprimimos la lista con los elementos que contiene ahora
print(frutas)

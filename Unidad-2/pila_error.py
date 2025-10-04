class Pila:
    def __init__(self, capacidad_maxima):
        self.elementos = []
        self.capacidad_maxima = capacidad_maxima

    def insertar(self, elemento):
        if len(self.elementos) >= self.capacidad_maxima:
            print(f"Error: Desbordamiento. La pila está llena (capacidad {self.capacidad_maxima}).")
        else:
            self.elementos.append(elemento)
            print(f"Insertado: {elemento} | Pila actual: {self.elementos}")

    def eliminar(self):
        if len(self.elementos) == 0:
            print("Error: Subdesbordamiento. La pila está vacía, no se puede eliminar.")
        else:
            eliminado = self.elementos.pop()
            print(f"Eliminado: {eliminado} | Pila actual: {self.elementos}")

pila = Pila(8)  


pila.insertar("X") 
pila.insertar("Y")  
pila.eliminar() 
pila.eliminar()    
pila.eliminar()     
pila.insertar("V")  
pila.insertar("W")  
pila.eliminar()     
pila.insertar("R")  

print(f"\nPila final: {pila.elementos}")
print(f"Total de elementos en la pila: {len(pila.elementos)}")

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, elemento):
        self.items.append(elemento)
        print(f"✓ Apilado: {elemento}")
    
    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            print(f"✗ Desapilado: {elemento}")
            return elemento
        else:
            print("La pila está vacía")
            return None
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return "Pila vacía"
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def mostrar(self):
        if self.esta_vacia():
            print("Pila: []")
        else:
            print(f"Pila: {self.items}")

def main():
    pila = Pila()
    
    while True:
        print("\n--- MENÚ PILA ---")
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Ver cima")
        print("4. Mostrar pila")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            elemento = input("Ingresa el elemento a apilar: ")
            pila.apilar(elemento)
        
        elif opcion == "2":
            pila.desapilar()
        
        elif opcion == "3":
            print(f"Elemento en cima: {pila.cima()}")
        
        elif opcion == "4":
            pila.mostrar()
        
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

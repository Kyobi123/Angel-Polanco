# Alumno: Angel Emmanuel Polanco Tuz
# Carrera: Ingeniería en sistemas computacionales
# Semestre: Tercer semestre

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def tamano(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

def torres_hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        movimientos.append(f"Mover disco {disco} de {obtener_nombre_torre(origen)} a {obtener_nombre_torre(destino)}")
        return
    
    torres_hanoi(n-1, origen, auxiliar, destino, movimientos)
    
    disco = origen.desapilar()
    destino.apilar(disco)
    movimientos.append(f"Mover disco {disco} de {obtener_nombre_torre(origen)} a {obtener_nombre_torre(destino)}")
    
    torres_hanoi(n-1, auxiliar, destino, origen, movimientos)

def obtener_nombre_torre(torre):
    if torre == torre_A:
        return "Torre A"
    elif torre == torre_B:
        return "Torre B"
    elif torre == torre_C:
        return "Torre C"
    return "Torre Desconocida"

def mostrar_torres():
    print(f"Torre A (PRINCIPAL): {torre_A}")
    print(f"Torre B (AUXILIAR): {torre_B}")
    print(f"Torre C (DESTINO): {torre_C}")
    print("-" * 30)

if __name__ == "__main__":
    torre_A = Pila()
    torre_B = Pila()
    torre_C = Pila()
    
    num_discos = 3
    
    for disco in range(num_discos, 0, -1):
        torre_A.apilar(disco)
    
    print("Estado inicial de las torres:")
    mostrar_torres()
    
    movimientos = []
    
    print("Resolviendo Torres de Hanoi...")
    torres_hanoi(num_discos, torre_A, torre_C, torre_B, movimientos)
    
    print("\nSecuencia de movimientos:")
    for i, movimiento in enumerate(movimientos, 1):
        print(f"{i}. {movimiento}")
    
    print(f"\nTotal de movimientos: {len(movimientos)}")
    
    print("\nEstado final de las torres:")
    mostrar_torres()
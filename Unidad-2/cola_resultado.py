from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            return None

    def tamaño(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

def sumar_colas(cola1, cola2):
    resultado = Cola()

    while not cola1.esta_vacia() and not cola2.esta_vacia():
        a = cola1.desencolar()
        b = cola2.desencolar()
        resultado.encolar(a + b)

    return resultado

colaA = Cola()
colaB = Cola()

for n in [3, 4, 2, 8, 12]:
    colaA.encolar(n)

for n in [6, 2, 9, 11, 3]:
    colaB.encolar(n)

colaResultado = sumar_colas(colaA, colaB)

print("Cola Resultado:", colaResultado)

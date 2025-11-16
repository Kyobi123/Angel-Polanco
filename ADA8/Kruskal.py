# Algoritmo de Kruskal para obtener el Árbol de Expansión Mínima (MST).
# Se ordenan las aristas por peso y se utiliza Union–Find para evitar ciclos.

class UF:
    """Estructura Union–Find (Disjoint Set) para detectar ciclos."""
    def __init__(self, elems):
        self.p = {e: e for e in elems}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])  # compresión de camino
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.p[pb] = pa
            return True
        return False


def kruskal(nodos, aristas):
    """
    nodos: lista de nodos
    aristas: lista de tuplas (peso, nodo1, nodo2)
    """
    aristas.sort()  # ordena por peso
    uf = UF(nodos)
    mst = []

    for w, u, v in aristas:
        if uf.union(u, v):   # solo agrega si no forma ciclo
            mst.append((u, v, w))

    return mst


# Ejemplo de ejecución
if __name__ == "__main__":
    nodos = ['A', 'B', 'C', 'D']
    aristas = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (2, 'B', 'C'),
        (3, 'C', 'D')
    ]
    print(kruskal(nodos, aristas))
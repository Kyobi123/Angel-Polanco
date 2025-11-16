# Algoritmo de Floyd–Warshall para calcular caminos mínimos entre todos los nodos.
# Se usa una matriz de distancias que contiene pesos o infinito si no hay conexión.

import math

def floyd_warshall(nodos, dist):
    for k in nodos:
        for i in nodos:
            for j in nodos:
                # Si pasar por k es mejor, actualizar
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# Ejemplo de ejecución
if __name__ == "__main__":
    nodos = ['A', 'B', 'C']
    dist = {
        'A': {'A': 0, 'B': 3, 'C': 8},
        'B': {'A': math.inf, 'B': 0, 'C': 2},
        'C': {'A': math.inf, 'B': math.inf, 'C': 0}
    }
    print(floyd_warshall(nodos, dist))
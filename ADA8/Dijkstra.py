# Algoritmo de Dijkstra para calcular el camino más corto desde un nodo origen.
# Requiere que los pesos del grafo sean positivos.
import math
import heapq

def dijkstra(grafo, inicio):
    # Distancias iniciales: infinito para todos excepto el inicio
    dist = {n: math.inf for n in grafo}
    dist[inicio] = 0

    # Cola de prioridad para elegir siempre la menor distancia disponible
    cola = [(0, inicio)]

    while cola:
        d, u = heapq.heappop(cola)  # se extrae el nodo con menor distancia

        # Relajación de aristas
        for v, w in grafo[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(cola, (dist[v], v))

    return dist


# Ejemplo de ejecución
if __name__ == "__main__":
    grafo = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 1)],
        'C': []
    }
    print(dijkstra(grafo, 'A'))
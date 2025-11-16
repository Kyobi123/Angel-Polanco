# Algoritmo de Warshall para calcular la alcanzabilidad entre nodos.
# Matriz booleana: 1 si existe camino, 0 si no.

def warshall(nodos, mat):
    """
    nodos: lista de nodos
    mat: matriz booleana con conexiones directas (0 o 1)
    """
    for k in nodos:
        for i in nodos:
            for j in nodos:
                # Si existe camino i->k y k->j, entonces existe i->j
                mat[i][j] = mat[i][j] or (mat[i][k] and mat[k][j])
    return mat


# Ejemplo de ejecución
if __name__ == "__main__":
    nodos = ['A', 'B', 'C', 'D']
    mat = {
        'A': {'A': 1, 'B': 1, 'C': 0, 'D': 0},
        'B': {'A': 0, 'B': 1, 'C': 1, 'D': 0},
        'C': {'A': 0, 'B': 0, 'C': 1, 'D': 1},
        'D': {'A': 0, 'B': 0, 'C': 0, 'D': 1}
    }
    print(warshall(nodos, mat))
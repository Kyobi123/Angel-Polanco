# Búsaqueda secuencial
def sequential_search(students, target_id):
    for i, s in enumerate(students):
        if s['id'] == target_id:
            return i, s
    return -1, None

if __name__ == "__main__":
    students = [
        {'id': 102, 'name': 'Ana', 'grade': 8.5},
        {'id': 215, 'name': 'Luis', 'grade': 7.0},
        {'id': 150, 'name': 'María', 'grade': 9.0},
        {'id': 301, 'name': 'Pedro', 'grade': 6.5},
    ]

    # Realizamos la búsqueda y nos de la información que tenemos de ello
    idx, rec = sequential_search(students, 150)
    print("Resultado:", idx, rec)

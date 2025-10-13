from collections import deque

class Cliente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo.lower() 
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class ColaBanco:
    def __init__(self):
        self.cola_prioritarios = deque()
        self.cola_normales = deque()

    def agregar_cliente(self, cliente):
        if cliente.tipo == "prioritario":
            self.cola_prioritarios.append(cliente)
        else:
            self.cola_normales.append(cliente)

    def atender_cliente(self):
        if self.cola_prioritarios:
            return self.cola_prioritarios.popleft()
        elif self.cola_normales:
            return self.cola_normales.popleft()
        else:
            return None

    def hay_clientes(self):
        return bool(self.cola_prioritarios or self.cola_normales)

    def mostrar_colas(self):
        print("\nEstado actual de las colas:")
        print("Prioritarios:", [str(c) for c in self.cola_prioritarios] or "Ninguno")
        print("Normales:    ", [str(c) for c in self.cola_normales] or "Ninguno")
        print("-" * 50)


def simular_banco():
    banco = ColaBanco()

    clientes = [
        Cliente("Ana", "normal"),
        Cliente("Carlos", "prioritario"),
        Cliente("Lucía", "normal"),
        Cliente("Pedro", "prioritario"),
        Cliente("Sofía", "normal"),
        Cliente("Miguel", "prioritario"),
        Cliente("Laura", "normal"),
        Cliente("José", "normal"),
        Cliente("Elena", "prioritario"),
        Cliente("Raúl", "normal")
    ]

    print("Llegada de clientes al banco:")
    for cliente in clientes:
        print(f"- {cliente}")
        banco.agregar_cliente(cliente)

    print("\nOrden de atención final:")
    contador = 1
    while banco.hay_clientes():
        cliente = banco.atender_cliente()
        print(f"{contador}. {cliente}")
        contador += 1


def modo_manual():
    banco = ColaBanco()

    while True:
        print("""
========= MENÚ BANCO =========
1. Agregar cliente
2. Atender siguiente cliente
3. Mostrar colas
4. Salir
==============================
        """)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ").strip()
            tipo = input("Tipo ('normal' o 'prioritario'): ").strip().lower()
            if tipo not in ("normal", "prioritario"):
                print("Tipo inválido. Usa 'normal' o 'prioritario'.")
                continue
            banco.agregar_cliente(Cliente(nombre, tipo))
            print(f"Cliente agregado: {nombre} ({tipo})")

        elif opcion == "2":
            cliente = banco.atender_cliente()
            if cliente:
                print(f"Cliente atendido: {cliente}")
            else:
                print("No hay clientes en espera.")

        elif opcion == "3":
            banco.mostrar_colas()

        elif opcion == "4":
            print("Saliendo del modo manual.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# ------------------- PROGRAMA PRINCIPAL -------------------

if __name__ == "__main__":
    while True:
        print("""
=====================================
🏦 SISTEMA DE GESTIÓN DE TURNOS - BANCO
=====================================
1. Simulación automática
2. Modo manual
3. Salir
=====================================
        """)
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            simular_banco()
        elif opcion == "2":
            modo_manual()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

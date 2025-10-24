class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad

    def imprimir(self):
        print("   Cliente: " + self.obtenerCliente())
        print("   Cantidad: " + str(self.obtenerCantidad()))
        print("   -----------")

    def obtenerCantidad(self):
        return self.cantidad

    def obtenerCliente(self):
        return self.cliente


class Nodo:
    def __init__(self, info=None, siguiente=None):
        self.info = info
        self.siguiente = siguiente

    def obtenerSiguiente(self):
        return self.siguiente

    def establecerSiguiente(self, nodo):
        self.siguiente = nodo

    def obtenerInfo(self):
        return self.info


class InterfazCola:
    def tamaño(self):
        raise NotImplementedError

    def estaVacia(self):
        raise NotImplementedError

    def frente(self):
        raise NotImplementedError

    def encolar(self, info):
        raise NotImplementedError

    def desencolar(self):
        raise NotImplementedError


class Cola(InterfazCola):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._tamaño = 0

    def tamaño(self):
        return self._tamaño

    def estaVacia(self):
        return self._tamaño == 0

    def frente(self):
        if self.primero is None:
            return None
        return self.primero.obtenerInfo()

    def encolar(self, info):
        nodo = Nodo(info)
        if self.primero is None:
            self.primero = self.ultimo = nodo
        else:
            self.ultimo.establecerSiguiente(nodo)
            self.ultimo = nodo
        self._tamaño += 1

    def desencolar(self):
        if self.primero is None:
            return None
        info = self.primero.obtenerInfo()
        self.primero = self.primero.obtenerSiguiente()
        if self.primero is None:
            self.ultimo = None
        self._tamaño -= 1
        return info

    def obtenerEnesimo(self, pos):
        if pos < 1 or pos > self._tamaño:
            return None
        actual = self.primero
        contador = 1
        while actual is not None:
            if contador == pos:
                return actual.obtenerInfo()
            actual = actual.obtenerSiguiente()
            contador += 1
        return None

    def imprimirInfo(self):
        print("********** CONTENIDO DE LA COLA **********")
        print("Tamaño:", self.tamaño())
        nodo = self.primero
        indice = 1
        while nodo is not None:
            print("** Elemento", indice)
            info = nodo.obtenerInfo()
            if hasattr(info, "imprimir"):
                info.imprimir()
            else:
                print("   ", info)
                print("   -----------")
            nodo = nodo.obtenerSiguiente()
            indice += 1
        print("*****************************************\n")


class PruebaCola:
    @staticmethod
    def main():
        c = Cola()

        p1 = Pedido(20, "cliente1")
        p2 = Pedido(30, "cliente2")
        p3 = Pedido(40, "cliente3")
        p4 = Pedido(50, "cliente4")

        print("Añadiendo 4 elementos a la cola...\n")
        c.encolar(p1)
        c.encolar(p2)
        c.encolar(p3)
        c.encolar(p4)

        c.imprimirInfo()

        print("Obteniendo el tercer elemento con obtenerEnesimo(3):")
        enesimo = c.obtenerEnesimo(3)
        if enesimo is not None:
            enesimo.imprimir()
        else:
            print("Posición no válida.")
        print("\n")

        print("Intentando obtener el elemento 10 (inexistente):")
        invalido = c.obtenerEnesimo(10)
        if invalido is None:
            print("Resultado: None (posición inválida)")
        print("\n")


if __name__ == "__main__":
    PruebaCola.main()

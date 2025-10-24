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


class Cola(InterfazCola):
    def __init__(self):
        self.inicio = None
        self.final = None
        self._tamaño = 0

    def tamaño(self):
        return self._tamaño

    def estaVacia(self):
        return self._tamaño == 0

    def frente(self):
        if self.inicio is None:
            return None
        return self.inicio.obtenerInfo()

    def encolar(self, info):
        nodo = Nodo(info)
        if self.inicio is None:
            self.inicio = self.final = nodo
        else:
            self.final.establecerSiguiente(nodo)
            self.final = nodo
        self._tamaño += 1

    def desencolar(self):
        if self.inicio is None:
            return None
        info = self.inicio.obtenerInfo()
        self.inicio = self.inicio.obtenerSiguiente()
        if self.inicio is None:
            self.final = None
        self._tamaño -= 1
        return info

    def imprimirInfo(self):
        print("********** CONTENIDO DE LA COLA **********")
        print("Tamaño:", self.tamaño())
        nodo = self.inicio
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
        print("******************************************\n")


class PruebaCola:
    @staticmethod
    def main():
        c = Cola()

        p1 = Pedido(20, "cliente1")
        p2 = Pedido(30, "cliente2")
        p3 = Pedido(40, "cliente3")
        p4 = Pedido(50, "cliente4")

        print("Encolar p1, p2, p3")
        c.encolar(p1)
        c.encolar(p2)
        c.encolar(p3)
        c.imprimirInfo()

        print("Consultar frente (sin remover):")
        f = c.frente()
        if f is not None:
            f.imprimir()
        else:
            print("Frente: Ninguno\n")

        print("Encolar p4 y mostrar estado:")
        c.encolar(p4)
        c.imprimirInfo()

        print("Desencolar (extraer un elemento) y mostrar estado:")
        eliminado = c.desencolar()
        print("Elemento eliminado:")
        if eliminado is not None:
            eliminado.imprimir()
        else:
            print("Ninguno")
        c.imprimirInfo()

        print("Extraer todos los elementos uno por uno:")
        while not c.estaVacia():
            r = c.desencolar()
            print("Desencolado:")
            r.imprimir()
            c.imprimirInfo()

        print("¿Cola vacía? ->", c.estaVacia())


if __name__ == "__main__":
    PruebaCola.main()

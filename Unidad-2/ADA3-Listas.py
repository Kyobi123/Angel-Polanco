import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from bisect import bisect_left

# -------------------------
#   ESTRUCTURAS DE DATOS
# -------------------------

class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nombre = nombre.strip().title()
        if not nombre or self.contiene(nombre):
            return False
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
            return True
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo
        return True

    def eliminar(self, nombre):
        actual, anterior = self.cabeza, None
        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior, actual = actual, actual.siguiente
        return False

    def contiene(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                return True
            actual = actual.siguiente
        return False

    def to_list(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.nombre)
            actual = actual.siguiente
        return resultado


# -------------------------
#   GESTOR PRINCIPAL
# -------------------------

class GestorPostres:
    def __init__(self):
        self.postres = []

    def _clave(self, nombre):
        return nombre.lower().strip()

    def _buscar_indice(self, nombre):
        claves = [self._clave(p['nombre']) for p in self.postres]
        return bisect_left(claves, self._clave(nombre))

    def nombres(self):
        return [p['nombre'] for p in self.postres]

    def ingredientes(self, nombre):
        i = self._buscar_indice(nombre)
        if i < len(self.postres) and self._clave(self.postres[i]['nombre']) == self._clave(nombre):
            return self.postres[i]['ingredientes'].to_list()
        raise KeyError(f"No existe el postre '{nombre}'.")

    def agregar_postre(self, nombre, ingredientes):
        nombre = nombre.strip().title()
        if not nombre:
            raise ValueError("Nombre vacío.")
        i = self._buscar_indice(nombre)
        if i < len(self.postres) and self._clave(self.postres[i]['nombre']) == self._clave(nombre):
            raise KeyError(f"El postre '{nombre}' ya está registrado.")
        lista = ListaIngredientes()
        for ing in ingredientes:
            lista.agregar(ing)
        self.postres.insert(i, {'nombre': nombre, 'ingredientes': lista})

    def eliminar_postre(self, nombre):
        i = self._buscar_indice(nombre)
        if i < len(self.postres) and self._clave(self.postres[i]['nombre']) == self._clave(nombre):
            del self.postres[i]
        else:
            raise KeyError(f"No existe '{nombre}'.")

    def agregar_ingrediente(self, nombre, ingrediente):
        i = self._buscar_indice(nombre)
        if i < len(self.postres) and self._clave(self.postres[i]['nombre']) == self._clave(nombre):
            return self.postres[i]['ingredientes'].agregar(ingrediente)
        raise KeyError(f"No se encontró el postre '{nombre}'.")

    def eliminar_ingrediente(self, nombre, ingrediente):
        i = self._buscar_indice(nombre)
        if i < len(self.postres) and self._clave(self.postres[i]['nombre']) == self._clave(nombre):
            if not self.postres[i]['ingredientes'].eliminar(ingrediente):
                raise ValueError(f"'{ingrediente}' no pertenece a '{nombre}'.")
            return True
        raise KeyError(f"No existe '{nombre}'.")

    def eliminar_duplicados(self):
        nueva_lista, prev = [], None
        for p in self.postres:
            clave = self._clave(p['nombre'])
            if clave != prev:
                nueva_lista.append(p)
                prev = clave
        eliminados = len(self.postres) - len(nueva_lista)
        self.postres = nueva_lista
        return eliminados


# -------------------------
#   INTERFAZ GRÁFICA
# -------------------------

class VentanaPostres:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Postres 🍮")
        self.root.geometry("980x600")
        self.root.configure(bg="#faf7f5")

        estilo = ttk.Style()
        estilo.configure("TLabel", background="#faf7f5", font=("Calibri", 11))
        estilo.configure("Titulo.TLabel", background="#faf7f5", font=("Calibri", 17, "bold"), foreground="#5a3825")
        estilo.configure("TButton", font=("Calibri", 10, "bold"))

        self.gestor = GestorPostres()
        self._crear_interfaz()

        # Datos iniciales
        self.gestor.agregar_postre("Brownie", ["Chocolate", "Harina", "Azúcar", "Huevo"])
        self.gestor.agregar_postre("Flan", ["Leche", "Azúcar", "Vainilla"])
        self.gestor.agregar_postre("Pay de Limón", ["Galleta", "Leche Condensada", "Limón"])
        self._actualizar_postres()

    def _crear_interfaz(self):
        ttk.Label(self.root, text="GESTOR DE POSTRES", style="Titulo.TLabel").pack(pady=10)
        contenedor = ttk.Frame(self.root)
        contenedor.pack(fill="both", expand=True, padx=15, pady=10)

        # Panel izquierdo
        panel_izq = ttk.Frame(contenedor)
        panel_izq.pack(side="left", fill="both", expand=True, padx=10)
        ttk.Label(panel_izq, text="Postres registrados:").pack(anchor="w", pady=5)
        self.lista_postres = tk.Listbox(panel_izq, font=("Calibri", 11), height=15, exportselection=False, bg="#fff9f4")
        self.lista_postres.pack(fill="both", expand=True)
        self.lista_postres.bind("<<ListboxSelect>>", lambda e: self._mostrar_ingredientes())

        frame_botones = ttk.Frame(panel_izq)
        frame_botones.pack(pady=8)
        ttk.Button(frame_botones, text="➕ Nuevo", command=self._nuevo_postre).grid(row=0, column=0, padx=4)
        ttk.Button(frame_botones, text="🗑 Eliminar", command=self._eliminar_postre).grid(row=0, column=1, padx=4)
        ttk.Button(frame_botones, text="♻ Depurar", command=self._limpiar).grid(row=0, column=2, padx=4)
        ttk.Button(frame_botones, text="📊 Visualizar", command=self._mostrar_estructura).grid(row=0, column=3, padx=4)

        # Panel derecho
        panel_der = ttk.Frame(contenedor)
        panel_der.pack(side="right", fill="both", expand=True, padx=10)
        ttk.Label(panel_der, text="Ingredientes:").pack(anchor="w", pady=5)
        self.lista_ing = tk.Listbox(panel_der, font=("Calibri", 11), height=15, bg="#f0fff3")
        self.lista_ing.pack(fill="both", expand=True)

        frame_botones_ing = ttk.Frame(panel_der)
        frame_botones_ing.pack(pady=8)
        ttk.Button(frame_botones_ing, text="➕ Añadir", command=self._nuevo_ing).grid(row=0, column=0, padx=4)
        ttk.Button(frame_botones_ing, text="🗑 Quitar", command=self._eliminar_ing).grid(row=0, column=1, padx=4)

    def _actualizar_postres(self):
        self.lista_postres.delete(0, tk.END)
        for n in self.gestor.nombres():
            self.lista_postres.insert(tk.END, n)

    def _mostrar_ingredientes(self):
        self.lista_ing.delete(0, tk.END)
        sel = self.lista_postres.curselection()
        if not sel:
            return
        nombre = self.lista_postres.get(sel[0])
        for ing in self.gestor.ingredientes(nombre):
            self.lista_ing.insert(tk.END, ing)

    def _nuevo_postre(self):
        nombre = simpledialog.askstring("Agregar Postre", "Nombre del postre:")
        if not nombre:
            return
        ingredientes = simpledialog.askstring("Ingredientes", "Lista de ingredientes (separados por coma):")
        lista = [i.strip() for i in ingredientes.split(",")] if ingredientes else []
        try:
            self.gestor.agregar_postre(nombre, lista)
            self._actualizar_postres()
            messagebox.showinfo("Éxito", f"'{nombre.title()}' ha sido agregado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_postre(self):
        sel = self.lista_postres.curselection()
        if not sel:
            return messagebox.showwarning("Atención", "Selecciona un postre para eliminar.")
        n = self.lista_postres.get(sel[0])
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{n}' definitivamente?"):
            self.gestor.eliminar_postre(n)
            self._actualizar_postres()
            self.lista_ing.delete(0, tk.END)

    def _nuevo_ing(self):
        sel = self.lista_postres.curselection()
        if not sel:
            return messagebox.showwarning("Aviso", "Selecciona un postre.")
        nombre = self.lista_postres.get(sel[0])
        ing = simpledialog.askstring("Nuevo Ingrediente", "Nombre del ingrediente:")
        if not ing:
            return
        self.gestor.agregar_ingrediente(nombre, ing)
        self._mostrar_ingredientes()

    def _eliminar_ing(self):
        sel_p, sel_i = self.lista_postres.curselection(), self.lista_ing.curselection()
        if not sel_p or not sel_i:
            return messagebox.showwarning("Aviso", "Selecciona un ingrediente para eliminar.")
        postre = self.lista_postres.get(sel_p[0])
        ing = self.lista_ing.get(sel_i[0])
        if messagebox.askyesno("Confirmar", f"¿Quitar '{ing}' de '{postre}'?"):
            self.gestor.eliminar_ingrediente(postre, ing)
            self._mostrar_ingredientes()

    def _limpiar(self):
        eliminados = self.gestor.eliminar_duplicados()
        self._actualizar_postres()
        messagebox.showinfo("Depuración", f"Se eliminaron {eliminados} duplicados." if eliminados else "No había duplicados.")

    def _mostrar_estructura(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Estructura Enlazada de Postres")
        canvas = tk.Canvas(ventana, width=1100, height=600, bg="#ffffff")
        canvas.pack(fill="both", expand=True)

        ancho, alto = 130, 45
        x0, y0, dy = 80, 80, 110

        for idx, p in enumerate(self.gestor.postres):
            y = y0 + idx * dy
            canvas.create_rectangle(x0, y, x0 + ancho, y + alto, fill="#ffebcc", outline="#6f4e37", width=2)
            canvas.create_text(x0 + ancho / 2, y + alto / 2, text=p['nombre'], font=("Calibri", 10, "bold"))
            canvas.create_line(x0 + ancho, y + alto / 2, x0 + ancho + 25, y + alto / 2, arrow=tk.LAST, fill="#6f4e37")

            actual = p['ingredientes'].cabeza
            x = x0 + ancho + 50
            while actual:
                canvas.create_rectangle(x, y, x + ancho, y + alto, fill="#c9f4c5", outline="#355e3b", width=2)
                canvas.create_text(x + ancho / 2, y + alto / 2, text=actual.nombre, font=("Calibri", 9))
                if actual.siguiente:
                    canvas.create_line(x + ancho, y + alto / 2, x + ancho + 25, y + alto / 2, arrow=tk.LAST, fill="#355e3b")
                else:
                    canvas.create_text(x + ancho + 30, y + alto / 2, text="None", font=("Calibri", 9, "italic"))
                x += ancho + 50
                actual = actual.siguiente


# -------------------------
#   EJECUCIÓN
# -------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPostres(root)
    root.mainloop()

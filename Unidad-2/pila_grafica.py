import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)
        self.mostrar_grafico()

    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            self.mostrar_grafico()
            return elemento
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar_grafico(self):
        self.ax.clear()
        if self.esta_vacia():
            self.ax.text(0.5, 0.5, "Pila vacía", ha='center', va='center', fontsize=12, color="red")
        else:
            for i, elemento in enumerate(self.items):
                self.ax.bar(0, 1, bottom=i, width=0.5, color="skyblue", edgecolor="black")
                self.ax.text(0, i + 0.5, str(elemento), ha='center', va='center', fontsize=10, color="black")

        self.ax.set_title("Visualización de la Pila")
        self.ax.axis("off")
        self.canvas.draw()

    def set_canvas(self, ax, canvas):
        self.ax = ax
        self.canvas = canvas


def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Simulación de Pila con Tkinter y Matplotlib")

    pila = Pila()

    # Crear figura de Matplotlib
    fig, ax = plt.subplots(figsize=(3, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    pila.set_canvas(ax, canvas)

    # Funciones para botones
    def apilar():
        elemento = simpledialog.askstring("Apilar", "Ingresa el elemento:")
        if elemento:
            pila.apilar(elemento)

    def desapilar():
        elemento = pila.desapilar()
        if elemento:
            messagebox.showinfo("Desapilar", f"Se quitó: {elemento}")
        else:
            messagebox.showwarning("Desapilar", "La pila está vacía")

    def ver_cima():
        elemento = pila.cima()
        if elemento:
            messagebox.showinfo("Cima", f"Elemento en cima: {elemento}")
        else:
            messagebox.showwarning("Cima", "La pila está vacía")

    def mostrar():
        if pila.esta_vacia():
            messagebox.showinfo("Mostrar", "La pila está vacía")
        else:
            messagebox.showinfo("Mostrar", f"Pila: {pila.items}")

    def salir():
        root.quit()

    # Crear botones
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10, pady=10)

    tk.Button(frame, text="Apilar", width=15, command=apilar).pack(pady=5)
    tk.Button(frame, text="Desapilar", width=15, command=desapilar).pack(pady=5)
    tk.Button(frame, text="Ver cima", width=15, command=ver_cima).pack(pady=5)
    tk.Button(frame, text="Mostrar pila", width=15, command=mostrar).pack(pady=5)
    tk.Button(frame, text="Salir", width=15, command=salir).pack(pady=5)

    # Mostrar gráfico inicial
    pila.mostrar_grafico()

    root.mainloop()


if __name__ == "__main__":
    main()

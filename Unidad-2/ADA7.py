# ===============================================
# GRAFO DE ESTADOS DE MÉXICO - VISUAL + MAPA
# Autor: ChatGPT - Versión Profesional
# ===============================================

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import folium
import webbrowser
import networkx as nx

# Coordenadas reales aproximadas de los estados principales
COORDS = {
    "Aguascalientes": (21.8853, -102.2916),
    "Baja California": (30.8406, -115.2838),
    "Baja California Sur": (26.0444, -111.6661),
    "Campeche": (19.8301, -90.5349),
    "Chiapas": (16.7569, -93.1292),
    "Chihuahua": (28.6320, -106.0691),
    "Ciudad de México": (19.4326, -99.1332),
    "Coahuila": (27.0587, -101.7068),
    "Colima": (19.2452, -103.7240),
    "Durango": (24.0277, -104.6532),
    "Guanajuato": (21.0190, -101.2574),
    "Guerrero": (17.4392, -99.5451),
    "Hidalgo": (20.0911, -98.7624),
    "Jalisco": (20.6597, -103.3496),
    "México": (19.3525, -99.6252),
    "Michoacán": (19.5660, -101.7068),
    "Morelos": (18.6813, -99.1013),
    "Nayarit": (21.7514, -104.8455),
    "Nuevo León": (25.5922, -99.9962),
    "Oaxaca": (17.0732, -96.7266),
    "Puebla": (19.0413, -98.2062),
    "Querétaro": (20.5888, -100.3899),
    "Quintana Roo": (19.1817, -88.4791),
    "San Luis Potosí": (22.1565, -100.9855),
    "Sinaloa": (25.1721, -107.4795),
    "Sonora": (29.0729, -110.9559),
    "Tabasco": (17.8409, -92.6189),
    "Tamaulipas": (24.2669, -98.8363),
    "Tlaxcala": (19.3182, -98.2375),
    "Veracruz": (19.1738, -96.1342),
    "Yucatán": (20.7099, -89.0943),
    "Zacatecas": (22.7709, -102.5832)
}


# ===============================================
# Clase del Grafo
# ===============================================
class GrafoMexico:
    def __init__(self):
        self.G = nx.Graph()

    def agregar_estado(self, estado):
        if estado not in COORDS:
            messagebox.showerror("Error", f"'{estado}' no está en la base de datos.")
            return False
        self.G.add_node(estado, coord=COORDS[estado])
        return True

    def conectar_estados(self):
        estados = list(self.G.nodes)
        for i in range(len(estados)):
            for j in range(i + 1, len(estados)):
                if random.random() < 0.5:  # probabilidad de conexión
                    costo = random.randint(100, 900)
                    self.G.add_edge(estados[i], estados[j], weight=costo)

    def recorrido_sin_repetir(self):
        estados = list(self.G.nodes)
        if len(estados) < 2:
            return [], 0
        random.shuffle(estados)
        costo = self.costo_total(estados)
        return estados, costo

    def recorrido_con_repeticion(self):
        estados = list(self.G.nodes)
        if len(estados) < 2:
            return [], 0
        recorrido = estados + [random.choice(estados)]
        random.shuffle(recorrido)
        costo = self.costo_total(recorrido)
        return recorrido, costo

    def ruta_critica(self):
        # Usa algoritmo de menor peso total (mínimo árbol generador)
        if len(self.G.nodes) < 2:
            return [], 0
        mst = nx.minimum_spanning_tree(self.G)
        total = sum(nx.get_edge_attributes(mst, "weight").values())
        return list(mst.edges), total

    def costo_total(self, recorrido):
        total = 0
        for i in range(len(recorrido) - 1):
            if self.G.has_edge(recorrido[i], recorrido[i + 1]):
                total += self.G[recorrido[i]][recorrido[i + 1]]["weight"]
        return total

    def generar_mapa(self, ruta_simple=None, ruta_repetida=None, ruta_critica=None):
        m = folium.Map(location=[23.0, -102.0], zoom_start=5, tiles="CartoDB dark_matter")

        # Dibujar nodos
        for estado in self.G.nodes:
            lat, lon = COORDS[estado]
            folium.CircleMarker(
                location=[lat, lon],
                radius=8,
                color="#22d3ee",
                fill=True,
                fill_color="#22d3ee",
                popup=f"<b>{estado}</b>",
            ).add_to(m)

        # Dibujar conexiones
        for u, v, data in self.G.edges(data=True):
            folium.PolyLine(
                locations=[COORDS[u], COORDS[v]],
                color="#38bdf8",
                weight=2,
                tooltip=f"Costo: {data['weight']}"
            ).add_to(m)

        # Resaltar rutas
        if ruta_critica:
            for u, v in ruta_critica:
                folium.PolyLine(
                    locations=[COORDS[u], COORDS[v]],
                    color="#ef4444",
                    weight=4,
                    tooltip="Ruta Crítica"
                ).add_to(m)

        m.save("grafo_mexico_interactivo.html")
        webbrowser.open("grafo_mexico_interactivo.html")


# ===============================================
# Interfaz gráfica principal
# ===============================================
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grafo México Interactivo - Profesional")
        self.geometry("900x600")
        self.configure(bg="#0f172a")

        self.grafo = GrafoMexico()
        self._interfaz()

    def _interfaz(self):
        frame = tk.Frame(self, bg="#1e293b")
        frame.pack(side="left", fill="y", padx=10, pady=10)

        title = tk.Label(frame, text="Configuración del Grafo", bg="#1e293b", fg="#22d3ee",
                         font=("Segoe UI", 14, "bold"))
        title.pack(pady=10)

        ttk.Button(frame, text="Agregar Estados", command=self.agregar_estados).pack(pady=5)
        ttk.Button(frame, text="Conectar Estados Aleatoriamente", command=self.conectar).pack(pady=5)
        ttk.Button(frame, text="Mostrar Mapa", command=self.mostrar_mapa).pack(pady=15)
        ttk.Button(frame, text="Recorrido sin repetir", command=self.mostrar_ruta_simple).pack(pady=5)
        ttk.Button(frame, text="Recorrido con repetición", command=self.mostrar_ruta_repetida).pack(pady=5)
        ttk.Button(frame, text="Ruta Crítica", command=self.mostrar_ruta_critica).pack(pady=5)
        ttk.Button(frame, text="Limpiar Grafo", command=self.limpiar).pack(pady=15)

        self.resultado = tk.Text(self, bg="#0f172a", fg="white", font=("Consolas", 11))
        self.resultado.pack(fill="both", expand=True, padx=10, pady=10)

    # ================= FUNCIONES ===================
    def agregar_estados(self):
        n = simpledialog.askinteger("Cantidad", "¿Cuántos estados quieres agregar? (mínimo 7)")
        if not n or n < 7:
            messagebox.showerror("Error", "Debes agregar al menos 7 estados.")
            return

        for _ in range(n):
            estado = simpledialog.askstring("Estado", "Ingresa nombre del estado:")
            if estado:
                self.grafo.agregar_estado(estado)

        messagebox.showinfo("Éxito", "Estados agregados correctamente.")
        self.mostrar_info()

    def conectar(self):
        self.grafo.conectar_estados()
        messagebox.showinfo("Listo", "Se han creado conexiones aleatorias entre estados.")
        self.mostrar_info()

    def mostrar_info(self):
        self.resultado.delete("1.0", "end")
        info = f"Estados: {list(self.grafo.G.nodes)}\n\n"
        info += f"Conexiones:\n"
        for u, v, d in self.grafo.G.edges(data=True):
            info += f" - {u} ↔ {v}  (Costo: {d['weight']})\n"
        self.resultado.insert("end", info)

    def mostrar_ruta_simple(self):
        ruta, costo = self.grafo.recorrido_sin_repetir()
        messagebox.showinfo("Recorrido sin repetir", f"{ruta}\nCosto total: {costo}")
        self.resultado.insert("end", f"\n\nRecorrido sin repetir:\n{ruta}\nCosto total: {costo}\n")

    def mostrar_ruta_repetida(self):
        ruta, costo = self.grafo.recorrido_con_repeticion()
        messagebox.showinfo("Recorrido con repetición", f"{ruta}\nCosto total: {costo}")
        self.resultado.insert("end", f"\n\nRecorrido con repetición:\n{ruta}\nCosto total: {costo}\n")

    def mostrar_ruta_critica(self):
        edges, total = self.grafo.ruta_critica()
        messagebox.showinfo("Ruta Crítica", f"Ruta mínima total: {total}")
        self.resultado.insert("end", f"\n\nRuta crítica (mínimo árbol generador):\n{edges}\nCosto total: {total}\n")
        self.grafo.generar_mapa(ruta_critica=edges)

    def mostrar_mapa(self):
        self.grafo.generar_mapa()
        messagebox.showinfo("Mapa", "Se ha generado el mapa interactivo en tu navegador.")

    def limpiar(self):
        self.grafo = GrafoMexico()
        self.resultado.delete("1.0", "end")
        messagebox.showinfo("Limpieza", "Grafo reiniciado.")


# ===============================================
# EJECUCIÓN PRINCIPAL
# ===============================================
if __name__ == "__main__":
    app = App()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox


class RailwayControl:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Control Ferroviario Simplificado")
        self.canvas = tk.Canvas(root, width=900, height=600, bg="black")
        self.canvas.pack()

        self.vias = {}  # Diccionario de vías y sus configuraciones
        self.itinerario_activo = []
        self.trenes = []

        self.setup_vias()
        self.create_controls()

    def setup_vias(self):
        """Configura el diseño de las vías."""
        # Vías de entrada (izquierda)
        self.vias["entrada-1"] = self.draw_via(50, 100, 200, 100, "entrada-1")
        self.vias["entrada-2"] = self.draw_via(50, 200, 200, 200, "entrada-2")

        # Vías intermedias (centro)
        self.vias["intermedia-1"] = self.draw_via(200, 100, 600, 100, "intermedia-1")
        self.vias["intermedia-2"] = self.draw_via(200, 200, 600, 200, "intermedia-2")
        self.vias["intermedia-3"] = self.draw_via(200, 300, 600, 300, "intermedia-3")

        # Vías de salida (derecha)
        self.vias["salida-1"] = self.draw_via(600, 100, 850, 100, "salida-1")
        self.vias["salida-2"] = self.draw_via(600, 300, 850, 300, "salida-2")

        # Conexiones entre vías
        self.draw_connection(200, 100, 200, 200)
        self.draw_connection(200, 200, 200, 300)
        self.draw_connection(600, 100, 600, 300)

    def draw_via(self, x1, y1, x2, y2, tag):
        """Dibuja una vía y la guarda en el diccionario."""
        line = self.canvas.create_line(x1, y1, x2, y2, width=4, fill="gray", tags=tag)
        self.canvas.tag_bind(tag, "<Button-1>", lambda event, t=tag: self.toggle_itinerary(t))
        return {"line": line, "active": False}

    def draw_connection(self, x1, y1, x2, y2):
        """Dibuja una conexión entre dos vías."""
        self.canvas.create_line(x1, y1, x2, y2, width=2, fill="gray", dash=(2, 2))

    def toggle_itinerary(self, tag):
        """Activa o desactiva una vía para el itinerario."""
        via = self.vias[tag]
        via["active"] = not via["active"]
        color = "green" if via["active"] else "gray"
        self.canvas.itemconfig(via["line"], fill=color)

        # Actualiza el itinerario activo
        if via["active"]:
            self.itinerario_activo.append(tag)
        else:
            self.itinerario_activo.remove(tag)

    def create_controls(self):
        """Crea los botones de control."""
        frame = tk.Frame(self.root, bg="black")
        frame.pack(fill=tk.X)

        tk.Button(frame, text="Añadir Tren", command=self.add_train).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame, text="Mover Tren", command=self.move_train).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame, text="Activar Itinerario", command=self.activate_itinerary).pack(side=tk.LEFT, padx=5, pady=5)

    def add_train(self):
        """Añade un tren a una vía de entrada seleccionada."""
        if "entrada-1" in self.itinerario_activo or "entrada-2" in self.itinerario_activo:
            entrada = self.itinerario_activo[0]
            if any(t["via"] == entrada for t in self.trenes):
                messagebox.showerror("Error", "La vía seleccionada ya tiene un tren.")
                return

            x, y = self.get_via_position(entrada)
            tren = self.canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="red")
            self.trenes.append({"tren": tren, "via": entrada})
            messagebox.showinfo("Éxito", f"Tren añadido en {entrada}.")
        else:
            messagebox.showerror("Error", "Seleccione una vía de entrada para añadir el tren.")

    def move_train(self):
        """Mueve un tren siguiendo el itinerario activo."""
        if not self.trenes:
            messagebox.showerror("Error", "No hay trenes para mover.")
            return

        for tren in self.trenes:
            if tren["via"] in self.itinerario_activo:
                # Mueve el tren a la siguiente vía en el itinerario
                current_via = tren["via"]
                current_idx = self.itinerario_activo.index(current_via)
                if current_idx + 1 < len(self.itinerario_activo):
                    next_via = self.itinerario_activo[current_idx + 1]
                    x, y = self.get_via_position(next_via)
                    self.canvas.coords(tren["tren"], x - 10, y - 10, x + 10, y + 10)
                    tren["via"] = next_via
                else:
                    messagebox.showinfo("Info", "El tren ya está al final del itinerario.")
                break
        else:
            messagebox.showerror("Error", "Ningún tren está en la vía seleccionada.")

    def activate_itinerary(self):
        """Activa el itinerario actual y bloquea vías conflictivas."""
        if not self.itinerario_activo:
            messagebox.showerror("Error", "Seleccione un itinerario antes de activarlo.")
            return

        # Bloquear las vías conflictivas
        for tag, via in self.vias.items():
            if tag not in self.itinerario_activo:
                self.canvas.itemconfig(via["line"], fill="red")

        messagebox.showinfo("Éxito", "Itinerario activado.")

    def get_via_position(self, tag):
        """Obtiene la posición de la vía para colocar un tren."""
        coords = self.canvas.coords(self.vias[tag]["line"])
        x = (coords[0] + coords[2]) // 2
        y = (coords[1] + coords[3]) // 2
        return x, y


if __name__ == "__main__":
    root = tk.Tk()
    app = RailwayControl(root)
    root.mainloop()

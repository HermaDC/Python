import tkinter as tk

"""
juego de simulacion de una estacion,
un poco bugeado
"""

# Inicialización de la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Estación - Factor de Circulación")
canvas = tk.Canvas(ventana, width=900, height=600, bg='lightgray')
canvas.pack()

# Variables de control
itinerario = []
tren_pos = None

# Definición de las vías conectadas con bifurcaciones y agujas
vias = {
    "entrada1": canvas.create_line(50, 150, 250, 150, width=5, fill="black"),  # Vía 1 izquierda (entrada)
    "entrada2": canvas.create_line(50, 300, 250, 300, width=5, fill="black"),  # Vía 2 izquierda (entrada)

    # Bifurcaciones de entrada a la estación
    "bifurcacion_izq_via1": canvas.create_line(250, 150, 400, 200, width=5, fill="black"),  # Bifurcación de entrada1
    "bifurcacion_izq_via2": canvas.create_line(250, 300, 400, 200, width=5, fill="black"),  # Bifurcación de entrada2
    "bifurcacion_via_muerta": canvas.create_line(250, 300, 350, 400, width=5, fill="black"),  # Bifurcación hacia vía muerta

    # Vías dentro de la estación
    "estacion_via1": canvas.create_line(400, 150, 600, 150, width=5, fill="black"),  # Vía 1 dentro de la estación
    "estacion_via2": canvas.create_line(400, 200, 600, 200, width=5, fill="black"),  # Vía 2 dentro de la estación
    "estacion_via3": canvas.create_line(400, 250, 600, 250, width=5, fill="black"),  # Vía 3 dentro de la estación

    # Vía muerta
    "via_muerta": canvas.create_line(350, 400, 400, 400, width=5, fill="darkred", dash=(4, 4)),

    # Bifurcaciones de la estación hacia las salidas
    "bifurcacion_der_via1": canvas.create_line(600, 150, 750, 200, width=5, fill="black"),  # Bifurcación de via1
    "bifurcacion_der_via2": canvas.create_line(600, 250, 750, 200, width=5, fill="black"),  # Bifurcación de via3

    # Vías de salida
    "salida1": canvas.create_line(600, 150, 850, 150, width=5, fill="black"),  # Vía 1 derecha (salida)
    "salida2": canvas.create_line(750, 200, 850, 200, width=5, fill="black"),  # Vía 2 derecha (salida)
}

# Estilización de los puntos de control (cantones) en las vías
cantones = {
    "entrada1": canvas.create_polygon(40, 140, 60, 160, 40, 160, fill="gray", tags="entrada1"),
    "entrada2": canvas.create_polygon(40, 290, 60, 310, 40, 310, fill="gray", tags="entrada2"),
    "salida1": canvas.create_polygon(840, 140, 860, 160, 840, 160, fill="gray", tags="salida1"),
    "salida2": canvas.create_polygon(840, 190, 860, 210, 840, 210, fill="gray", tags="salida2"),
    "estacion_via1": canvas.create_polygon(390, 140, 410, 160, 390, 160, fill="gray", tags="estacion_via1"),
    "estacion_via2": canvas.create_polygon(390, 190, 410, 210, 390, 210, fill="gray", tags="estacion_via2"),
    "estacion_via3": canvas.create_polygon(390, 240, 410, 260, 390, 260, fill="gray", tags="estacion_via3"),
    "via_muerta": canvas.create_rectangle(340, 390, 360, 410, fill="gray", tags="via_muerta")
}

# Añadimos andenes visuales en la estación
canvas.create_rectangle(400, 130, 600, 170, fill='gray80', outline='black')  # Andén superior
canvas.create_rectangle(400, 230, 600, 270, fill='gray80', outline='black')  # Andén inferior

# Añadimos algunos rótulos para las vías
canvas.create_text(100, 120, text="Entrada 1", font=("Arial", 10), fill="black")
canvas.create_text(100, 320, text="Entrada 2", font=("Arial", 10), fill="black")
canvas.create_text(800, 120, text="Salida 1", font=("Arial", 10), fill="black")
canvas.create_text(800, 230, text="Salida 2", font=("Arial", 10), fill="black")
canvas.create_text(470, 420, text="Vía Muerta", font=("Arial", 10), fill="darkred")

# Función para establecer el itinerario
def establecer_itinerario(event):
    global itinerario
    canton_clicado = canvas.gettags("current")[0]

    if len(itinerario) < 2:
        canvas.itemconfig(cantones[canton_clicado], fill="blue")
        itinerario.append(canton_clicado)

# Función para mover el tren a través de las vías
def mover_tren():
    global tren_pos, itinerario

    if tren_pos is None and len(itinerario) == 2:
        tren_pos = vias[itinerario[0]]  # Comienza en la vía de entrada seleccionada
        canvas.itemconfig(tren_pos, fill="red")

    # Movimiento por las vías
    if tren_pos in [vias["entrada1"], vias["entrada2"]]:
        canvas.itemconfig(tren_pos, fill="black")
        tren_pos = vias["estacion_via1"] if itinerario[0] == "entrada1" else vias["estacion_via3"]
        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos in [vias["estacion_via1"], vias["estacion_via3"]]:
        canvas.itemconfig(tren_pos, fill="black")
        tren_pos = vias["salida1"] if itinerario[1] == "salida1" else vias["salida2"]
        canvas.itemconfig(tren_pos, fill="red")

    else:
        return  # El tren ha llegado al destino

    ventana.after(1000, mover_tren)

# Función para reiniciar el sistema
def reiniciar():
    global itinerario, tren_pos
    itinerario = []
    tren_pos = None

    # Reiniciar colores de las vías y cantones
    for canton in cantones.values():
        canvas.itemconfig(canton, fill="gray")
    for via in vias.values():
        canvas.itemconfig(via, fill="black")

# Botones para controlar el tren
tk.Button(ventana, text="Mover Tren", command=mover_tren).pack(pady=10)
tk.Button(ventana, text="Reiniciar", command=reiniciar).pack(pady=10)

# Asignar clics a los cantones para seleccionar el itinerario
for tag in cantones.keys():
    canvas.tag_bind(tag, "<Button-1>", establecer_itinerario)

# Ejecutar la ventana principal
ventana.mainloop()

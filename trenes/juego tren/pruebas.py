import tkinter as tk

# Inicialización de la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Mesa de Factor de Circulación con Dos Vías")
canvas = tk.Canvas(ventana, width=1000, height=600, bg='lightgray')
canvas.pack()

# Variables de control
itinerario = []
tren_pos = None

# Definición de las vías conectadas con bifurcaciones y agujas
vias = {
    # Vías de entrada/salida (dos direcciones)
    "entrada1": canvas.create_line(50, 150, 250, 150, width=5, fill="black"),  # Vía de entrada/salida 1
    "entrada2": canvas.create_line(50, 250, 250, 250, width=5, fill="black"),  # Vía de entrada/salida 2

    # Bifurcaciones de entrada a la estación
    "bifurcacion_entrada1_via1": canvas.create_line(250, 150, 400, 150, width=5, fill="black"),  # De entrada1 a vía 1
    "bifurcacion_entrada1_via2": canvas.create_line(250, 150, 400, 250, width=5, fill="black"),  # De entrada1 a vía 2

    "bifurcacion_entrada2_via1": canvas.create_line(250, 250, 400, 150, width=5, fill="black"),  # De entrada2 a vía 1
    "bifurcacion_entrada2_via2": canvas.create_line(250, 250, 400, 250, width=5, fill="black"),  # De entrada2 a vía 2
    "bifurcacion_entrada2_via_muerta": canvas.create_line(250, 250, 350, 350, width=5, fill="black"),  # De entrada2 a vía muerta

    # Vías dentro de la estación
    "estacion_via1": canvas.create_line(400, 150, 600, 150, width=5, fill="black"),  # Vía 1 dentro de la estación
    "estacion_via2": canvas.create_line(400, 250, 600, 250, width=5, fill="black"),  # Vía 2 dentro de la estación

    # Vía muerta
    "via_muerta": canvas.create_line(350, 350, 450, 350, width=5, fill="darkred", dash=(4, 4)),

    # Bifurcaciones de la estación hacia la salida
    "bifurcacion_salida_via1": canvas.create_line(600, 150, 750, 150, width=5, fill="black"),  # Desde vía 1
    "bifurcacion_salida_via2": canvas.create_line(600, 250, 750, 250, width=5, fill="black"),  # Desde vía 2

    # Vías de salida
    "salida1": canvas.create_line(750, 150, 900, 150, width=5, fill="black"),  # Vía de salida 1
    "salida2": canvas.create_line(750, 250, 900, 250, width=5, fill="black"),  # Vía de salida 2
}

# Estilización de los puntos de control (cantones) en las vías
cantones = {
    "entrada1": canvas.create_polygon(40, 140, 60, 160, 40, 160, fill="gray", tags="entrada1"),
    "entrada2": canvas.create_polygon(40, 240, 60, 260, 40, 260, fill="gray", tags="entrada2"),
    "salida1": canvas.create_polygon(890, 140, 910, 160, 890, 160, fill="gray", tags="salida1"),
    "salida2": canvas.create_polygon(890, 240, 910, 260, 890, 260, fill="gray", tags="salida2"),
    "estacion_via1": canvas.create_polygon(390, 140, 410, 160, 390, 160, fill="gray", tags="estacion_via1"),
    "estacion_via2": canvas.create_polygon(390, 240, 410, 260, 390, 260, fill="gray", tags="estacion_via2"),
    "via_muerta": canvas.create_rectangle(340, 340, 360, 360, fill="gray", tags="via_muerta")
}

# Añadimos andenes visuales en la estación
canvas.create_rectangle(400, 130, 600, 170, fill='gray80', outline='black')  # Andén superior (para vía 1)
canvas.create_rectangle(400, 230, 600, 270, fill='gray80', outline='black')  # Andén inferior (para vía 2)

# Añadimos algunos rótulos para las vías
canvas.create_text(100, 130, text="Entrada/Salida 1", font=("Arial", 10), fill="black")
canvas.create_text(100, 270, text="Entrada/Salida 2", font=("Arial", 10), fill="black")
canvas.create_text(830, 130, text="Salida/Entrada 1", font=("Arial", 10), fill="black")
canvas.create_text(830, 270, text="Salida/Entrada 2", font=("Arial", 10), fill="black")
canvas.create_text(470, 120, text="Vía 1", font=("Arial", 10), fill="black")
canvas.create_text(470, 280, text="Vía 2", font=("Arial", 10), fill="black")
canvas.create_text(470, 380, text="Vía Muerta", font=("Arial", 10), fill="darkred")

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

        # Mover aguja en la entrada
        if itinerario[0] == "entrada1":
            if itinerario[1] == "estacion_via1":
                print("Moviendo aguja: Entrada 1 -> Estación Vía 1")
                tren_pos = vias["bifurcacion_entrada1_via1"]
            elif itinerario[1] == "estacion_via2":
                print("Moviendo aguja: Entrada 1 -> Estación Vía 2")
                tren_pos = vias["bifurcacion_entrada1_via2"]
        elif itinerario[0] == "entrada2":
            if itinerario[1] == "estacion_via1":
                print("Moviendo aguja: Entrada 2 -> Estación Vía 1")
                tren_pos = vias["bifurcacion_entrada2_via1"]
            elif itinerario[1] == "estacion_via2":
                print("Moviendo aguja: Entrada 2 -> Estación Vía 2")
                tren_pos = vias["bifurcacion_entrada2_via2"]
            elif itinerario[1] == "via_muerta":
                print("Moviendo aguja: Entrada 2 -> Vía Muerta")
                tren_pos = vias["bifurcacion_entrada2_via_muerta"]

        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos in [vias["bifurcacion_entrada1_via1"], vias["bifurcacion_entrada2_via1"]]:
        canvas.itemconfig(tren_pos, fill="black")
        tren_pos = vias["estacion_via1"]
        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos in [vias["bifurcacion_entrada1_via2"], vias["bifurcacion_entrada2_via2"]]:
        canvas.itemconfig(tren_pos, fill="black")
        tren_pos = vias["estacion_via2"]
        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos == vias["via_muerta"]:
        canvas.itemconfig(tren_pos, fill="black")
        print("El tren ha llegado a la vía muerta.")
        tren_pos = None
        return

    elif tren_pos in [vias["estacion_via1"], vias["estacion_via2"]]:
        canvas.itemconfig(tren_pos, fill="black")

        # Mover aguja para salir de la estación
        if tren_pos == vias["estacion_via1"]:
            print("Moviendo aguja: Estación Vía 1 -> Salida")
            tren_pos = vias["bifurcacion_salida_via1"]
        elif tren_pos == vias["estacion_via2"]:
            print("Moviendo aguja: Estación Vía 2 -> Salida")
            tren_pos = vias["bifurcacion_salida_via2"]

        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos in [vias["bifurcacion_salida_via1"], vias["bifurcacion_salida_via2"]]:
        canvas.itemconfig(tren_pos, fill="black")

        if itinerario[1] == "salida1":
            tren_pos = vias["salida1"]
        elif itinerario[1] == "salida2":
            tren_pos = vias["salida2"]

        canvas.itemconfig(tren_pos, fill="red")

    elif tren_pos in [vias["salida1"], vias["salida2"]]:
        canvas.itemconfig(tren_pos, fill="black")
        tren_pos = None  # El tren ha llegado a su destino
        print("El tren ha llegado a su destino.")
        return

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

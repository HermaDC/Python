import tkinter as tk

"""
Juego con simulacion de itinerrio, 
básico, solo con dos vías
"""

# Inicializar la ventana principal
ventana = tk.Tk()
ventana.title("Simulación Factor de Circulación")
ventana.geometry("600x400")

# Variables para controlar los cantones y el tren
cantones = ["cantón 1", "cantón 2", "bifurcación", "cantón A", "cantón B"]
tren_pos = 0  # Posición del tren en el cantón
itinerario_establecido = False  # Si el itinerario ha sido establecido
vía_destino = None  # Estación seleccionada (A o B)
inicio_itinerario = False  # Para controlar la selección del primer clic (aguja de entrada)
aguja_entrada = None  # Aguja de entrada seleccionada

# Crear el canvas para dibujar las vías y los cantones
canvas = tk.Canvas(ventana, width=600, height=300)
canvas.pack(pady=20)

# Dibujar las vías y los cantones
cantones_vías = [
    canvas.create_line(50, 150, 300, 150, width=3),  # Vía principal
    canvas.create_line(300, 150, 450, 100, width=3),  # Vía A
    canvas.create_line(300, 150, 450, 200, width=3)   # Vía B
]

# Dibujar puntos para simular los cantones
cantones_dibujo = [
    canvas.create_oval(100, 140, 120, 160, fill="gray", tags="cantón_1"),  # cantón 1
    canvas.create_oval(200, 140, 220, 160, fill="gray", tags="cantón_2"),  # cantón 2
    canvas.create_oval(300, 140, 320, 160, fill="gray", tags="bifurcación"),  # bifurcación
    canvas.create_oval(450, 90, 470, 110, fill="gray", tags="cantón_A"),   # cantón A
    canvas.create_oval(450, 190, 470, 210, fill="gray", tags="cantón_B")   # cantón B
]

# Crear una representación visual del tren
tren = canvas.create_rectangle(60, 140, 80, 160, fill="green")

# Función para establecer el itinerario
def establecer_itinerario(inicio, destino):
    global vía_destino, itinerario_establecido, inicio_itinerario, aguja_entrada

    vía_destino = destino
    itinerario_establecido = True

    # Colorear el itinerario en verde
    if destino == "A":
        canvas.itemconfig(cantones_dibujo[0], fill="green")
        canvas.itemconfig(cantones_dibujo[1], fill="green")
        canvas.itemconfig(cantones_dibujo[2], fill="green")
        canvas.itemconfig(cantones_dibujo[3], fill="green")
    elif destino == "B":
        canvas.itemconfig(cantones_dibujo[0], fill="green")
        canvas.itemconfig(cantones_dibujo[1], fill="green")
        canvas.itemconfig(cantones_dibujo[2], fill="green")
        canvas.itemconfig(cantones_dibujo[4], fill="green")
    
    estado_texto.set(f"Itinerario establecido desde {inicio} hacia estación {destino}")

# Función para manejar clics en los cantones
def manejar_clic(event):
    global inicio_itinerario, aguja_entrada, vía_destino

    # Identificar el objeto (cantón) que fue clicado
    cantón_clicado = canvas.find_withtag("current")
    index_cantón = cantones_dibujo.index(cantón_clicado[0])

    if not inicio_itinerario:
        # Seleccionar la aguja de entrada
        if index_cantón == 0 or index_cantón == 1:  # Permitir solo las entradas en cantón 1 o 2
            aguja_entrada = index_cantón
            inicio_itinerario = True
            canvas.itemconfig(cantones_dibujo[aguja_entrada], fill="blue")
            estado_texto.set(f"Aguja de entrada seleccionada: {cantones[aguja_entrada]}")
    else:
        # Establecer la aguja de salida
        if index_cantón == 3:  # Cantón A
            establecer_itinerario(cantones[aguja_entrada], "A")
        elif index_cantón == 4:  # Cantón B
            establecer_itinerario(cantones[aguja_entrada], "B")

        # Reiniciar la selección de itinerarios
        inicio_itinerario = False
        aguja_entrada = None

# Función para mover el tren por el itinerario
def mover_tren():
    global tren_pos

    if tren_pos < len(cantones) - 1 and itinerario_establecido:
        # Liberar el cantón anterior
        if tren_pos > 0:
            canvas.itemconfig(cantones_dibujo[tren_pos - 1], fill="green")  # Liberar el anterior

        tren_pos += 1  # Mover el tren al siguiente cantón
        
        # Mover el tren al siguiente cantón visualmente
        if tren_pos == 1:
            canvas.coords(tren, 160, 140, 180, 160)
        elif tren_pos == 2:
            canvas.coords(tren, 260, 140, 280, 160)
        elif tren_pos == 3:
            if vía_destino == "A":
                canvas.coords(tren, 380, 90, 400, 110)
            else:
                canvas.coords(tren, 380, 190, 400, 210)
        
        # Cambiar el color del cantón actual a rojo (ocupado)
        canvas.itemconfig(cantones_dibujo[tren_pos], fill="red")  # Cantón ocupado
        
        # Si el tren ha llegado a la estación final (cantón A o B), detener el movimiento
        if tren_pos == 3 and vía_destino == "A":
            estado_texto.set("El tren ha llegado a la estación A.")
            return  # Detener el movimiento
        elif tren_pos == 3 and vía_destino == "B":
            estado_texto.set("El tren ha llegado a la estación B.")
            return  # Detener el movimiento
        
        ventana.after(1000, mover_tren)  # Llamar la función recursivamente

# Función para reiniciar el juego
def reiniciar_juego():
    global tren_pos, itinerario_establecido, vía_destino, inicio_itinerario, aguja_entrada
    tren_pos = 0
    itinerario_establecido = False
    vía_destino = None
    inicio_itinerario = False
    aguja_entrada = None
    canvas.coords(tren, 60, 140, 80, 160)
    
    for cantón in cantones_dibujo:
        canvas.itemconfig(cantón, fill="gray")
    
    estado_texto.set("Establece el itinerario seleccionando dos cantones.")

# Crear etiquetas y botones
estado_texto = tk.StringVar()
estado_texto.set("Establece el itinerario seleccionando dos cantones.")

label_estado = tk.Label(ventana, textvariable=estado_texto)
label_estado.pack(pady=10)

boton_mover = tk.Button(ventana, text="Mover Tren", width=15, command=mover_tren)
boton_mover.pack(pady=10)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", width=15, command=reiniciar_juego)
boton_reiniciar.pack(pady=10)

# Asignar clics a los cantones
canvas.tag_bind("cantón_1", "<Button-1>", manejar_clic)
canvas.tag_bind("cantón_2", "<Button-1>", manejar_clic)
canvas.tag_bind("bifurcación", "<Button-1>", manejar_clic)
canvas.tag_bind("cantón_A", "<Button-1>", manejar_clic)
canvas.tag_bind("cantón_B", "<Button-1>", manejar_clic)

# Ejecutar la ventana
ventana.mainloop()

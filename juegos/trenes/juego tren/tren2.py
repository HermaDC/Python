import tkinter as tk
"""
Necesidad de pulsar botones
simula los cantones pero no es inmersivo
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
    canvas.create_oval(100, 140, 120, 160, fill="gray"),  # cantón 1
    canvas.create_oval(200, 140, 220, 160, fill="gray"),  # cantón 2
    canvas.create_oval(300, 140, 320, 160, fill="gray"),  # bifurcación
    canvas.create_oval(450, 90, 470, 110, fill="gray"),   # cantón A
    canvas.create_oval(450, 190, 470, 210, fill="gray")   # cantón B
]

# Crear una representación visual del tren
tren = canvas.create_rectangle(60, 140, 80, 160, fill="green")

# Función para establecer el itinerario
def establecer_itinerario(destino):
    global vía_destino, itinerario_establecido

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
    
    estado_texto.set(f"Itinerario establecido hacia estación {destino}")

# Función para mover el tren por el itinerario
def mover_tren():
    global tren_pos

    if tren_pos < len(cantones) - 1 and itinerario_establecido:
        tren_pos += 1
        
        # Mover el tren al siguiente cantón
        if tren_pos == 1:
            canvas.coords(tren, 160, 140, 180, 160)
        elif tren_pos == 2:
            canvas.coords(tren, 260, 140, 280, 160)
        elif tren_pos == 3:
            if vía_destino == "A":
                canvas.coords(tren, 380, 90, 400, 110)
            else:
                canvas.coords(tren, 380, 190, 400, 210)
        
        # Cambiar el color de los cantones según se ocupan/liberan
        for i in range(len(cantones_dibujo)):
            if i == tren_pos:
                canvas.itemconfig(cantones_dibujo[i], fill="red")  # Cantón ocupado
            else:
                if itinerario_establecido:
                    canvas.itemconfig(cantones_dibujo[i], fill="green")  # Itinerario
                else:
                    canvas.itemconfig(cantones_dibujo[i], fill="gray")   # Liberado

        ventana.after(1000, mover_tren)  # Llamar la función recursivamente

# Función para reiniciar el juego
def reiniciar_juego():
    global tren_pos, itinerario_establecido, vía_destino
    tren_pos = 0
    itinerario_establecido = False
    vía_destino = None
    canvas.coords(tren, 60, 140, 80, 160)
    
    for cantón in cantones_dibujo:
        canvas.itemconfig(cantón, fill="gray")
    
    estado_texto.set("Establece el itinerario y mueve el tren.")

# Crear etiquetas y botones
estado_texto = tk.StringVar()
estado_texto.set("Establece el itinerario y mueve el tren.")

label_estado = tk.Label(ventana, textvariable=estado_texto)
label_estado.pack(pady=10)

boton_a = tk.Button(ventana, text="Itinerario A", width=15, command=lambda: establecer_itinerario("A"))
boton_a.pack(side=tk.LEFT, padx=20)

boton_b = tk.Button(ventana, text="Itinerario B", width=15, command=lambda: establecer_itinerario("B"))
boton_b.pack(side=tk.RIGHT, padx=20)

boton_mover = tk.Button(ventana, text="Mover Tren", width=15, command=mover_tren)
boton_mover.pack(pady=10)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", width=15, command=reiniciar_juego)
boton_reiniciar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()

import tkinter as tk
import random


"""
juego con dos botones,
cada boton manda a una via
muy simple
"""
# Inicializar la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Trenes")
ventana.geometry("600x400")

# Variables de control del juego
destinos = ["A", "B"]
tren_destino = random.choice(destinos)  # Destino inicial del tren
tren_pos_x = 50  # Posición inicial del tren en el eje x
tren_pos_y = 150  # Posición fija del tren en el eje y
movimiento = 5  # Velocidad del tren
itinerario = {"A": False, "B": False}  # Control de los itinerarios elegidos por el jugador

# Variables para la lógica del juego
puntuacion = 0
fallos = 0
juego_activo = True

# Función para mover el tren a lo largo de la vía
def mover_tren():
    global tren_pos_x, tren_destino, puntuacion, fallos, juego_activo

    if tren_pos_x < 300:  # Movimiento horizontal antes de la bifurcación
        tren_pos_x += movimiento
        canvas.coords(tren, tren_pos_x, tren_pos_y, tren_pos_x+30, tren_pos_y+30)
        ventana.after(50, mover_tren)
    else:
        # Llegada a la bifurcación, seguir el itinerario
        if itinerario["A"] and tren_destino == "A":
            estado_texto.set("¡Correcto! El tren sigue el itinerario hacia la estación A.")
            puntuacion += 1
            canvas.coords(tren, 450, tren_pos_y, 480, tren_pos_y+30)
        elif itinerario["B"] and tren_destino == "B":
            estado_texto.set("¡Correcto! El tren sigue el itinerario hacia la estación B.")
            puntuacion += 1
            canvas.coords(tren, 450, tren_pos_y+50, 480, tren_pos_y+80)
        else:
            estado_texto.set(f"¡Error! El tren tenía que ir a la estación {tren_destino}.")
            fallos += 1
            # Mover el tren por la vía incorrecta
            if tren_destino == "A":
                canvas.coords(tren, 450, tren_pos_y+50, 480, tren_pos_y+80)
            else:
                canvas.coords(tren, 450, tren_pos_y, 480, tren_pos_y+30)

        # Actualizar el marcador
        marcador.set(f"Puntuación: {puntuacion} | Errores: {fallos}")

        # Reiniciar el tren después de una pausa
        ventana.after(2000, reiniciar_tren)

# Función para reiniciar el tren
def reiniciar_tren():
    global tren_pos_x, tren_destino, itinerario

    tren_destino = random.choice(destinos)  # Nuevo destino aleatorio
    tren_pos_x = 50  # Restablecer la posición del tren
    canvas.coords(tren, tren_pos_x, tren_pos_y, tren_pos_x+30, tren_pos_y+30)
    estado_texto.set(f"Nuevo tren. Próximo destino: {tren_destino}")
    mover_tren()

# Función para establecer el itinerario
def establecer_itinerario(via):
    global itinerario
    if via == "A":
        itinerario["A"] = True
        itinerario["B"] = False
        canvas.itemconfig(itinerario_linea_a, fill="green")
        canvas.itemconfig(itinerario_linea_b, fill="gray")
        estado_texto.set("Itinerario hacia la estación A establecido.")
    elif via == "B":
        itinerario["A"] = False
        itinerario["B"] = True
        canvas.itemconfig(itinerario_linea_a, fill="gray")
        canvas.itemconfig(itinerario_linea_b, fill="green")
        estado_texto.set("Itinerario hacia la estación B establecido.")

# Crear el lienzo (canvas) para dibujar la vía y el tren
canvas = tk.Canvas(ventana, width=600, height=300)
canvas.pack(pady=20)

# Dibujar la vía principal y las estaciones
canvas.create_line(50, 165, 300, 165, width=3)  # Vía principal antes de la bifurcación
canvas.create_line(300, 165, 450, 115, width=3)  # Vía hacia la estación A
canvas.create_line(300, 165, 450, 215, width=3)  # Vía hacia la estación B

# Dibujar las estaciones
canvas.create_text(480, 115, text="Estación A", font=("Arial", 12))
canvas.create_text(480, 215, text="Estación B", font=("Arial", 12))

# Crear la caja verde que simula el tren
tren = canvas.create_rectangle(tren_pos_x, tren_pos_y, tren_pos_x+30, tren_pos_y+30, fill="green")

# Líneas que indican el itinerario activo
itinerario_linea_a = canvas.create_line(300, 165, 450, 115, width=3, fill="gray")  # Inicialmente apagado
itinerario_linea_b = canvas.create_line(300, 165, 450, 215, width=3, fill="gray")  # Inicialmente apagado

# Crear etiquetas y botones
estado_texto = tk.StringVar()
estado_texto.set(f"¡Bienvenido! Próximo destino: {tren_destino}")

marcador = tk.StringVar()
marcador.set(f"Puntuación: {puntuacion} | Errores: {fallos}")

label_estado = tk.Label(ventana, textvariable=estado_texto)
label_estado.pack(pady=10)

label_marcador = tk.Label(ventana, textvariable=marcador)
label_marcador.pack()

# Botones para elegir el itinerario (establecer la vía)
boton_via_a = tk.Button(ventana, text="Itinerario A", width=15, height=2, command=lambda: establecer_itinerario("A"))
boton_via_a.pack(side=tk.LEFT, padx=20)

boton_via_b = tk.Button(ventana, text="Itinerario B", width=15, height=2, command=lambda: establecer_itinerario("B"))
boton_via_b.pack(side=tk.RIGHT, padx=20)

# Iniciar el juego
mover_tren()

# Ejecutar la ventana
ventana.mainloop()

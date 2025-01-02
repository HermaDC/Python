import pyperclip
from datetime import datetime

# Obtener el año actual
año = str(datetime.now().year)

# Solicitar datos del usuario
apellidos = "DíazCabezas"
nombre = "Miguel"
curso = input("Inserta curso: ").strip()
modulo = input("Inserta el módulo: ").replace(" ", "").strip()
actividad = input("Inserta la actividad: ").strip()

# Formatear la actividad y curso  para que cada palabra comience con mayúscula
actividad_formateada = actividad.title().replace(" ", "")
curso_formateado = curso.title().replace(" ", "")

# Formatear el nombre final
nombre_final = f"{año}{apellidos}{nombre}{curso_formateado}{modulo}{actividad_formateada}"

# Mostrar y copiar el nombre final
print("\nNombre generado:", nombre_final)
pyperclip.copy(nombre_final)
print("El nombre se ha copiado al portapapeles.")

import random

"""citas = {
        "John Lannon": "La vida es lo que pasa mientras estás ocupado haciendo otros planes.",
        "Steve Jobs": "La única forma de hacer un gran trabajo es amar lo que haces.",
        "Dalai Lama": "La felicidad no es algo hecho. Viene de tus propias acciones.",
        "Nelson Mandela": "La educación es el arma más poderosa que puedes usar para cambiar el mundo."
    }

for i in range(0,2):
    print(random.choice(citas))
    print("eso \n")
"""
# Lista de citas de personas famosas
citas2 = [
    {"cita": "La vida es lo que pasa mientras estás ocupado haciendo otros planes.", "autor": "John Lennon"},
    {"cita": "El mayor peligro para la mayoría de nosotros no es que nuestro objetivo sea demasiado alto y no lo alcancemos, sino que sea demasiado bajo y lo consigamos.", "autor": "Michelangelo"},
    {"cita": "El único modo de hacer un gran trabajo es amar lo que haces.", "autor": "Steve Jobs"},
    {"cita": "En el medio de la dificultad yace la oportunidad.", "autor": "Albert Einstein"},
    {"cita": "Tu tiempo es limitado, así que no lo desperdicies viviendo la vida de alguien más.", "autor": "Steve Jobs"},
    {"cita": "La vida es realmente simple, pero insistimos en hacerla complicada.", "autor": "Confucio"},
    {"cita": "La mejor manera de predecir el futuro es inventarlo.", "autor": "Alan Kay"},
    {"cita": "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.", "autor": "Albert Schweitzer"},
    {"cita": "Lo que no te mata te hace más fuerte.", "autor": "Friedrich Nietzsche"},
    {"cita": "No cuentes los días, haz que los días cuenten.", "autor": "Muhammad Ali"},
    {"cita": "La felicidad no es algo hecho. Viene de tus propias acciones.", "autor": "Dalai Lama"},
    {"cita": "La educación es el arma más poderosa que puedes usar para cambiar el mundo.", "autor": "Nelson Mandela"}

]

# Función para generar una cita aleatoria
for i in range(0,3):
    cita_seleccionada = random.choice(citas2)
    print(f'"{cita_seleccionada["cita"]}" - {cita_seleccionada["autor"]}')



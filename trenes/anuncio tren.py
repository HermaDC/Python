# Sinfonía de los trenes
# Compositor: Efraín Barquero

from music import *

# Definir las notas
do = Note("C", 4)
re = Note("D", 4)
mi = Note("E", 4)
fa = Note("F", 4)
sol = Note("G", 4)
la = Note("A", 4)
si = Note("B", 4)

# Crear la melodía
melodia = [sol, sol, sol, sol, fa, mi, fa, mi, re, re, do]

# Crear el objeto de música
musica = Music(melodia, tempo=120)

# Reproducir la música
musica.play()

from itertools import zip_longest
TIPOS = {"arquero": [30, 8], "cuerpo a cuerpo": [15, 12], "duende": [10, 6], "mago": [5, 20], "exp": [1000, 40]}
ENEMIGOS = {"ogro": [30, 6], "elfo": [15, 12], "duende": [10, 6], "troll": [25, 5]}
ENEDIS = list(ENEMIGOS.keys())
NOMBRES = ["Pepe", "Juan", "Jesús", "Felipe", "Rafa", "Mateo", "Fran", "José", "Antonio"]

class Mounstro:
    def __init__(self, nombre, tipo):
        if tipo not in ENEMIGOS:
            raise ValueError(f"Tipo de enemigo no válido: {tipo}")
        self.nombre = nombre
        self.tipo = tipo
        self.vida, self.ataque = ENEMIGOS[tipo]
    
    def atacar(self, objetivo):
        objetivo.vida -= self.ataque
        estado = "ha muerto" if objetivo.vida <= 0 else f"le queda {objetivo.vida} de vida"
        print(f"{self.nombre} ataca a {objetivo.nombre}. {objetivo.nombre} {estado}")

class Jugador:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        objetivo.vida -= self.ataque
        estado = "ha muerto" if objetivo.vida <= 0 else f"le queda {objetivo.vida} de vida"
        print(f"{self.nombre} ataca a {objetivo.nombre}. {objetivo.nombre} {estado}")

class Aliado(Jugador):
    pass

def combate_grupal(aliados, enemigos):
    for ali, ene in zip_longest(aliados, enemigos, fillvalue=None):
        if ene and ali:
            ali.atacar(ene)
            ene.atacar(ali)
        elif ene:
            ene.atacar(aliados[-1])  # Ataca al último aliado
        elif ali:
            ali.atacar(enemigos[-1])  # Ataca al último enemigo

def lucha(jugador, enemigo, aliados=(), otros_enemigos=()):
    print(f"Te enfrentas a un {enemigo.tipo}.")
    while jugador.vida > 0 and enemigo.vida > 0:
        opcion = input("Atacas(a) o no haces nada(b)? ").lower()
        if opcion == "a":
            print("¡Atacas!")
            combate_grupal(aliados, otros_enemigos)
            jugador.atacar(enemigo)
            if enemigo.vida > 0:
                enemigo.atacar(jugador)
            else:
                print(f"¡Has derrotado a {enemigo.nombre}!")
                break
        elif opcion == "b":
            print("Decides no hacer nada.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
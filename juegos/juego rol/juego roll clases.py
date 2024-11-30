from itertools import zip_longest
import random
from rol import *

def tutorial(jugador):
    print("Se te harán preguntas y debes contestar (normalmente se responde con a o b, o sí y no).")

    enemigo_principal = Mounstro(random.choice(NOMBRES), random.choice(ENEDIS))

    enemigo_principal.vida = jugador.ataque + 3
    lucha(jugador, enemigo_principal)
    print(f"Has logrado derrotar a {enemigo_principal.nombre}. Elige tu recompensa:")

    while True:
        opcion = input("1. Poción de vida\n2. Nueva arma\n")
        match opcion.strip():
            case "1":
                print("Obtienes una poción de vida.")
                jugador.vida += 10
                break
            case "2":
                print("Obtienes una mejora en ataque.")
                jugador.ataque += 3
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
    print("Hasta aquí el tutorial. ¡Que te diviertas! \nSi deseas salir pulsa Ctrl+C")

def main():
    print("Bienvenido")
    nombre = input("¿Cuál es tu nombre? ")
    print(f"{nombre}, lo primero es crear tu rol. Aquí tienes una lista de tipos de personaje:\n")

    for i in TIPOS:
        print(f"El rol {i} tiene {TIPOS[i][0]} puntos de vida y {TIPOS[i][1]} puntos de ataque")

    a = input("¿Qué tipo eliges? ").lower()
    while not a or a not in TIPOS:
        print("Debe ser uno de los tipos anteriores.")
        a = input("¿Qué tipo eliges? ").lower()
    
    print("\n¡Pasemos a la acción!")
    print("¿Quieres realizar el tutorial? (sí/no)")
    respuesta = input().strip().lower()
    jugador = Jugador(nombre, a, *TIPOS[a])

    if respuesta == "sí" or respuesta == "si":
        tutorial(jugador)
    else:
        print("¡Has decidido saltarte el tutorial! Comenzando el juego...\n")
    a = input("vas de camino ha una ciudad y te encuntras con un elfo herido, \nque haces, le ayudas(a) o le dejas tirado(b)")
    if a == "a":
        print("Mientras curas al elfo, un orco te intenta atacar pero consigues salvar al elfo, ahora es tu amigo")
        amigo = Aliado(random.choice(NOMBRES), "elfo", ENEMIGOS["elfo"][0],ENEMIGOS["elfo"][1])
        ogro = Mounstro("pedo", random.choice(ENEDIS))
        lucha(jugador, ogro, (amigo,), ())
    raise NotImplementedError
    # Aquí puedes continuar con el juego si el jugador decide saltarse el tutorial
    # El código para el juego real comenzaría aquí, adaptando el código del tutorial si es necesario

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        a = input("\n¿Deseas salir? ").lower()
        if a == "sí" or a == "si" :
            raise SystemExit
        else:
            main()

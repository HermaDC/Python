from re import S
#from numpy import true_divide
import os


print("bienvenido a recorger gustos\n ¿como quieres los sandwich?")
while True:
    name = input("como te llamas")

    queso = input("¿con o sin queso? [C, S]")

    huevo = input("¿con o sin huevo? [C, S]")
    tostado  = input("¿tostado o sin tostar?")
    if os.path.exists("holanoob.txt") == True:
        with open("holanoob.txt", "a") as list_of_cosas:
            list_of_cosas.write("a {} le gusta el sandwich\n".format(name))
            list_of_cosas.write("{} queso\n".format(queso))
            list_of_cosas.write("{} huevo\n".format(huevo))
            list_of_cosas.write("y {}\n".format(tostado))
    else:
        with open("holanoob.txt", "w") as list_of_cosas:
            list_of_cosas.write("a {} le gusta el sandwich\n".format(name))
            list_of_cosas.write("{} queso\n".format(queso))
            list_of_cosas.write("{} huevo\n".format(huevo))
            list_of_cosas.write("y {}\n".format(tostado))
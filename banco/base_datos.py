import sqlite3 as sql 
import os.path


def createDB():
    if os.path.exists("banco_peluchin.db") == False:
        conn = sql.connect("banco_peluchin.db")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE peluches (
            nombre text,
            apellido text,
            ID integer PRIMARY KEY,
            dinero integer
            )"""
        )
        conn.commit()
        conn.close()
        paispeluchin = [("Marina", " ", 1, 5043 ),("Maria Sofia","", 2, 6693), ("Tiger", "Depredador", 3, 143), ("Roco","", 4, 0) ]
        insdatos(paispeluchin) 


def insdato(nombre, apellido, ID=None, Dinero=0):
    conn = sql.connect("banco_peluchin.db")
    cursor = conn.cursor()
    if ID is None:
        instruccion = f"INSERT INTO peluches (nombre, apellido, dinero) VALUES('{nombre}', '{apellido}', {Dinero})"
        #print("none")
    else:
        instruccion = f"INSERT INTO peluches VALUES ('{nombre}', '{apellido}', {ID}, {Dinero})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insdatos(listapeluches):
    conn = sql.connect("banco_peluchin.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO peluches VALUES(?, ?, ?, ?)"
    cursor.executemany(instruccion, listapeluches)
    conn.commit()
    conn.close()

def buscar(filtro):
    conn = sql.connect("banco_peluchin.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM peluches WHERE nombre like'{}'""".format(filtro))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    #print(data)
    try:
        tupla = data[0] #sacar datos de la base de datos
        nombre = tupla[0]
        dinero = int(tupla[3])
        #print(nombre, dinero)
        return nombre, dinero
    except IndexError:
        return None

def realizar(dinero_retirar, persona, din):
    conn = sql.connect("banco_peluchin.db")
    cursor = conn.cursor()
    dinero_total = din + dinero_retirar
    instruccion = """UPDATE peluches SET dinero = {}""".format(dinero_total) + """ WHERE nombre = '{}'""".format(persona)
    cursor.execute(instruccion)
    lista = cursor.fetchall()
    conn.commit()
    conn.close()

createDB()

#variables de prueba
#insdato("pepe", "cara", None, 300)



#bucle continuo
if __name__ == "__main__":
    while True:
        persona = input("elige la persona para ver su cuenta: \n")
        nom, dinero = buscar(persona)
        a =  input("realizar operacion Si/NO: \n")
        if a == "Si":
            b = int(input("cuanto?"))
            realizar(b, nom, dinero)
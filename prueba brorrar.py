import tkinter as tk


def algo(eso):
    algos = str(eso)
    print(algos)
    if algos == "":
        print("es vacio")
    elif algos == " ":
        print("tiene espacio")


raiz2 = tk.Tk()

user_label = tk.Label(raiz2, text="nombre: ")
user_label.grid(row=1, column=1)
user_entra = tk.Entry(raiz2)
user_entra.grid(row=1, column=2)
boton = tk.Button(raiz2, text="eso", command= lambda:[ algo(str(user_entra.get()))])
boton.grid(row=2, column=2)

raiz2.mainloop()
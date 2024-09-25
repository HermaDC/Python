import base_datos as bd
import tkinter as tk

#funciones loginas en base de datos
def crear_cuenta(nombre, apellido="", ID=None, dinero=0):
    valor = bd.buscar(nombre)
    try:
        #print(type(ID))
        Id = int(ID)
    except ValueError:
        #print("error")
        Id = None
    if valor is not None:
        nom, din = valor
        #print("ya existe")

        raiz2 = tk.Tk()

        error = tk.Text(raiz2)
        error.grid(row=1, column=1)
        error.delete(0.0, 100.0)
        error.insert(tk.END, "{}".format("Ya existe ese usuario"))

        cerrar = tk.Button(raiz2, text="cerrar", command= lambda:[raiz2.destroy()])
        cerrar.config(background="red")
        cerrar.grid(row=2, column=1,)

        raiz2.mainloop()



    else:
        bd.insdato(nombre, apellido, Id, dinero)

def consultar(username):

    valor = bd.buscar(username)
    if valor is None:
        raiz4 = tk.Tk()
        error = tk.Text(raiz4)
        error.grid(row=1, column=1)
        error.delete(0.0, 200.0)
        error.insert(tk.END, "{}".format("No existe esa persona"))

        cerrar = tk.Button(raiz4, text="cerrar", command= lambda:[raiz4.destroy()])
        cerrar.config(background="red")
        cerrar.grid(row=2, column=1,)

        raiz4.mainloop()
    else:
        nom, din = valor

        raiz3 = tk.Tk()
        total = str(nom) + "tiene " + str(din) + " ans."
        
        texto = tk.Text(raiz3)
        texto.grid(row=1, column=1)
        texto.delete(0.0, 200.0)
        texto.insert(tk.END, "{}".format(total))

        volver_boton = tk.Button(raiz3, text="volver", command= lambda:[raiz3.destroy()])
        volver_boton.config(background="red")
        volver_boton.grid(row=1, column=1,)

        raiz3.mainloop()

def mover(din_retirar, username):
    #print(din_retirar, username)

    valor = bd.buscar(username)
    if valor is None:
        raiz4 = tk.Tk()
        error = tk.Text(raiz4)
        error.grid(row=1, column=1)
        error.delete(0.0, 200.0)
        error.insert(tk.END, "{}".format("No existe esa persona"))

        cerrar = tk.Button(raiz4, text="cerrar", command= lambda:[raiz4.destroy()])
        cerrar.config(background="red")
        cerrar.grid(row=2, column=1,)

        raiz4.mainloop()
    else:
        nom, din = bd.buscar(username)
        bd.realizar(din_retirar, nom, din)
        #print("hecho..")

def salir():
    raise SystemExit
#funciones de GUI
def crear_cuenta_gui():
    raiz2 = tk.Tk()

    user_label = tk.Label(raiz2, text="nombre: ")
    user_label.grid(row=1, column=1)
    user_entra = tk.Entry(raiz2)
    user_entra.grid(row=1, column=2)

    apll_label = tk.Label(raiz2, text="apellido: ")
    apll_label.grid(row=2, column=1)
    apll_entra = tk.Entry(raiz2)
    apll_entra.grid(row=2, column=2)

    id_label = tk.Label(raiz2, text="id: ")
    id_label.grid(row=3, column=1)
    id_entra = tk.Entry(raiz2)
    id_entra.grid(row=3, column=2)

    dinero_label = tk.Label(raiz2, text="Dinero: ")
    dinero_label.grid(row=4, column=1)
    dinero_entra = tk.Entry(raiz2)
    dinero_entra.grid(row=4, column=2)

    cancelar = tk.Button(raiz2, text="cancelar", command = raiz2.destroy)
    cancelar.config(background="red")
    cancelar.grid(row=5, column=1)

    confirmar = tk.Button(raiz2, text="confirmar", command = lambda:[crear_cuenta(str(user_entra.get()), str(apll_entra.get()),\
        id_entra.get(), int(dinero_entra.get())), raiz2.destroy()])
    confirmar.config(background="green")
    confirmar.grid(row=5, column=2)
    

    raiz2.mainloop()

def mover_gui():
    raiz2 = tk.Tk()

    user_label = tk.Label(raiz2, text="Nombre: ")
    user_label.grid(row=1, column=1)
    user_entra = tk.Entry(raiz2)
    user_entra.grid(row=1, column=2)

    dinero_label = tk.Label(raiz2, text="Dinero a mover: ")
    dinero_label.grid(row=2, column=1)
    dinero_entra = tk.Entry(raiz2)
    dinero_entra.grid(row=2, column=2)

    cancelar = tk.Button(raiz2, text="cancelar", command = raiz2.destroy)
    cancelar.config(background="red")
    cancelar.grid(row=3, column=1)

    confirmar = tk.Button(raiz2, text="confirmar", command = lambda:[mover(int(dinero_entra.get()), str(user_entra.get())), raiz2.destroy()])
    confirmar.config(background="green")
    confirmar.grid(row=3, column=2)

    raiz2.mainloop()

def consultar_gui():
    raiz2 = tk.Tk()

    user_label = tk.Label(raiz2, text="nombre de usuario")
    user_label.grid(row=1, column=1)
    user_entra = tk.Entry(raiz2)
    user_entra.grid(row=1, column=2)

    #usuario = user_entra.get()

    consultar_boton = tk.Button(raiz2, text="Cancelar", command= lambda:[raiz2.destroy()])
    consultar_boton.config(background="red")
    consultar_boton.grid(row=2, column=1)

    cancelar_boton = tk.Button(raiz2, text="Consultar", command= lambda:[consultar(str(user_entra.get()))])
    cancelar_boton.config(background="green")
    cancelar_boton.grid(row=2, column=2)
    
    raiz2.mainloop()

def menu():
    raiz =  tk.Tk()
    raiz.title("Banco peluchin")

    labelC = tk.Button(text="crear cuenta", command= crear_cuenta_gui)
    labelC.grid(row=1,column=1 )
    
    labelR = tk.Button(text="transacccion", command = mover_gui)
    labelR.grid(row=2,column=1 )

    labelI = tk.Button(text="consultar", command = consultar_gui) 
    labelI.grid(row=3,column=1 )
    boton = tk.Button(text="salir", command= salir)
    boton.grid(row=4, column=1)
    boton.config(background="red")

    raiz.mainloop()

menu()
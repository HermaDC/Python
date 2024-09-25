from cryptography.fernet import Fernet
import tkinter as tk
import os 


def genera_clave():
	claveg = Fernet.generate_key()
	if os.path.exists("clave.key") == False:
		with open("clave.key","wb") as archivo_clave:
			archivo_clave.write(claveg)
	else:
		return


def cargar_clave():
	return open("clave.key","rb").read()

def menu():
    raiz = tk.Tk()
    raiz.title("Elige un método de cifrado")

    labelF = tk.Button(text="asimetrico", command=lambda: [raiz.destroy(), menuf()])
    labelF.grid(row=1, column=1)

    labelE = tk.Button(text="espacios", command=lambda: [raiz.destroy(), menuEs()])
    labelE.grid(row=1, column=2)

    raiz.mainloop()

def menuEs():
    raizE = tk.Tk()
    raizE.title("Mensaje secreto")

    
    labelE = tk.Button(text="encriptar", command=lambda: encriptarE(EnMensaj))
    labelE.grid(row=1,column=1 )

    labelD = tk.Button(text="desencriptar", command=lambda: desencriptarE(EnMensaj))
    labelD.grid(row=1,column=3 )


    label = tk.Label(text="Escribe el mensaje")
    label.grid(row=2,column=2)

    EnMensaj = tk.Entry(raizE)
    EnMensaj.config(background="grey")
    EnMensaj.grid(row=3, column=2)
    
    labelS = tk.Button(text="volver", command = lambda: [raizE.destroy(), menu()])
    labelS.config(background="red")
    labelS.grid(row=4,column=2 )

    raizE.mainloop()

def menuf():
    raizF = tk.Tk()
    raizF.title("Mensaje secreto")

    # mensaje = input("escribe el mensaje: ").encode()

    
    labelE = tk.Button(text="encriptar", command= lambda: encriptarF(EnMensaj))
    labelE.grid(row=1,column=1 )

    labelD = tk.Button(text="desencriptar", command = lambda: desencriptarF(EnMensaj))
    labelD.grid(row=1,column=3 )


    label = tk.Label(text="Escribe el mensaje")
    label.grid(row=2,column=2)

    EnMensaj = tk.Entry(raizF)
    EnMensaj.config(background="grey")
    EnMensaj.grid(row=3, column=2)
    
    labelS = tk.Button(text="volver", command = lambda: [raizF.destroy(), menu()])
    labelS.config(background="red")
    labelS.grid(row=4,column=2 )

    raizF.mainloop()

    

def encriptarF(EnMensaj):
    print(EnMensaj)
    mensaje = EnMensaj.get().encode()
    encriptado = f.encrypt(mensaje)

    raiz3 = tk.Tk()
    raiz3.title("Encriptar")
    TextD = tk.Text(raiz3)
    TextD.grid(row=1, column=1)
    
    Botonv = tk.Button(raiz3, text="volver", command=lambda: raiz3.destroy())
    Botonv.config(background="red")
    Botonv.grid(row=2, column=1)

    #TextD.delete(1, 1000)
    TextD.insert(tk.END, encriptado)
    raiz3.mainloop()


def desencriptarF(EnMensaj):
    mensaje = EnMensaj.get().encode()
    desen = f.decrypt(mensaje)
    

    raiz2 = tk.Tk()
    raiz2.title("Desencriptar")
    TextD = tk.Text(raiz2)
    TextD.grid(row=1, column=1)
    
    Botonv = tk.Button(raiz2, text="volver", command= lambda: raiz2.destroy())
    Botonv.config(background="red")
    Botonv.grid(row=2, column=1)

    #TextD.delete(1, 1000)
    TextD.insert(tk.END, desen)
    raiz2.mainloop()

def encriptarE(text):
    encodeText = ""
    text1 = text.get()
    print(text1)
    with open('file.txt', 'w') as f:
        for a in text1.encode('utf-8'):
            bits = format(a, '08b')
            for bit in bits:
                if(bit == '0'):
                    f.write(" ")
                    encodeText += " "
                if(bit == '1'):
                    f.write("\t")
                    encodeText += "\t"
    print("'" + encodeText + "'")

def desencriptarE(text):
    data = text.get().encode()
    decodeText = ""
    for index in range(0, len(data),8):
        letra = ""
        for char in data[index:index+8]:
            if char ==" ":
                letra+='0'
            else:
                letra+='1'
        letra = chr(int(letra, 2))
        decodeText += letra
    print(decodeText)

genera_clave()
clave = cargar_clave()
f = Fernet(clave)
menu()
from cryptography.fernet import Fernet
import os.path

def genera_clave():
	if os.path.exists("clave.key") == False:	
		clave = Fernet.generate_key()
		with open("clave.key","wb") as archivo_clave:
			archivo_clave.write(clave)
	return open("clave.key", "rb").read()



clave = genera_clave()

while True:
	forma = input("que desea encriptar o desencriptar \nE o D: ")
	mensaje = input("inserta mensaje: ")
	mens = mensaje.encode()
	f = Fernet(clave)

	if forma.lower() == "e":
		encriptado = f.encrypt(mens)
		print(encriptado)

	elif forma.lower() == "d":
		desencriptado = f.decrypt(mens)
		print(desencriptado)
	else:
		break

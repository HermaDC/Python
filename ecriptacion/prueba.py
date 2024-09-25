def encode(text):
    with open('file.txt', 'w') as f:
        for a in text.encode('utf-8'):
            bits = format(a, '08b')
            for bit in bits:
                if(bit == '0'):
                    f.write(" ")
                if(bit == '1'):
                    f.write("\t")
def decode():
    data = input("Ingrese el texto a decodificar: ")
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

encode("hola soy miguel")
decode()
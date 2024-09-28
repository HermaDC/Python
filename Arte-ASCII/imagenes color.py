from PIL import Image
from colorama import init, Fore

def escala_de_grises(imagen):
    return imagen.convert('L')

def redimensionar_imagen(imagen, nuevo_ancho=100):
    (ancho, alto) = imagen.size
    aspect_ratio = alto/float(ancho)
    nuevo_alto = int(aspect_ratio * nuevo_ancho)
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))
    return imagen_redimensionada

def pixeles_a_ascii(imagen):
    pixels = imagen.getdata()
    caracteres_ascii = ''.join([Fore.GREEN + '@' if pixel<128 else Fore.WHITE + ' ' for pixel in pixels])
    return caracteres_ascii

def main(ruta_imagen, nuevo_ancho=100):
    try:
        imagen = Image.open(ruta_imagen)
    except Exception as e:
        print(e)
        return
    imagen = escala_de_grises(imagen)
    imagen = redimensionar_imagen(imagen)
    ascii_str = pixeles_a_ascii(imagen)
    img_width = imagen.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    print(ascii_img)

init(autoreset=True)
ruta_imagen = 'C:/Users/diazb/Pictures'
# Cambia esto por la ruta a tu imagen
main(ruta_imagen)

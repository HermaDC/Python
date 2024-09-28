from PIL import Image
import pyperclip


ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    path = input("Introduce la ruta de la imagen: ")
    try:
        image = Image.open(path)
    except:
        print(path, "No es una ruta válida")
        return
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    print(ascii_image)
    pyperclip.copy(ascii_image)

main()
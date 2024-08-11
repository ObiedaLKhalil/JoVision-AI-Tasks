#'L': 8-bit pixels, grayscale.

from PIL import Image

def color_to_black(image_path): 
    RED_WEIGHT = 0.299
    GREEN_WEIGHT = 0.587
    BLUE_WEIGHT = 0.114
    image = Image.open(image_path)
    grayscale_img = Image.new('L', image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            gray = int(RED_WEIGHT * r + GREEN_WEIGHT * g + BLUE_WEIGHT * b)
            grayscale_img.putpixel((x, y), (gray))

    return grayscale_img

grayscale_img = color_to_black('C:\\Users\\obied\\OneDrive\\Desktop\\JoVision-AI-Tasks\\RGBimage.jpg')
grayscale_img.show()
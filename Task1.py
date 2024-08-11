from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Windows
image = Image.open('C:\\Users\\obied\\OneDrive\\Desktop\\JoVision-AI-Tasks\\noPassItem.png')
text = pytesseract.image_to_string(image)

print(text)
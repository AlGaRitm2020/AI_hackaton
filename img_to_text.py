import pytesseract
from PIL import Image

def img_to_text(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(Image.open(img))
    return text

if __name__ == '__main__':
    img_to_text('aah97e00-page02_1.tif')

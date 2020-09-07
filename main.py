import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd=r"C:\laragon\bin\python\python-3.6.1\Scripts\pytesseract.exe"

img=Image.open('./1.jpg')
text=pytesseract.image_to_string(img)
print(text)
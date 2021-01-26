import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2

import numpy as np

import os

img3 = cv2.imread('ban2.png')
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret,thresh3 = cv2.threshold(img3,127,255,cv2.THRESH_BINARY)

text3 = tess.image_to_string(thresh3, lang='ben')
print(text3)

text_file = open("Output.txt", "w", encoding="utf-8")
text_file.write(text3)
text_file.close()

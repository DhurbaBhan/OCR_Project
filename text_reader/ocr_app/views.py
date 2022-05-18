from multiprocessing import context
from django.shortcuts import render
import cv2
from cv2 import adaptiveThreshold
import numpy as np
import pytesseract

# Create your views here.
def button(request):
    return render(request,"index.html")

def output(request):

    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread("C:/Users/DELL/Desktop/photos/longtxt.png")
    # To improve the text detection
    img=cv2.resize(img,None,fx=4,fy=3)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    adaptive_threshold=cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,65,10)
    text = pytesseract.image_to_string(adaptive_threshold)
    print(text)
    context={"text":text}
    #cv2.imshow("gray",gray)
    # cv2.imshow("adaptive",adaptive_threshold)
    # cv2.waitKey(0)

    return render(request,"show.html",context)

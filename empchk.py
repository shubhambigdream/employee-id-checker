import cv2
import pytesseract
from PIL import Image
import os
a=["EMULOO1","EML","001","Smith","Sample","11230123","Jordan","Clarke","2306","9022","0243","0483","Lily","Stewart","5843","2166","4567","8901"]
d={"EMULOO1":"Administrator","EML":"Administrator","001":"Administrator","Smith":"Smith Sample","Sample":"Smith Sample","11230123":"Smith Sample","Jordan":"Jordan Clarke","Clarke":"Jordan Clarke","2306":"Jordan Clarke","Lily":"Lily Stewart","Stewart":"Lily Stewart","5843":"Lily Stewart"}
print("Want to check Employee id from Database:")
print("    ")
print("identification check")

print("    ")

img=Image.open('sample1.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result=pytesseract.image_to_string(img)
b=""
c=0
result=result.split()
for i in result:
    if i in a:
        b=i
        print(d[b])
        c=1
        break
if c is 0:
    print("Employee not found")
    

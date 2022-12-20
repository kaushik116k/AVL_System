import easyocr
import cv2
img = cv2.imread("D://number_plates//number_plates2.jpg")
reader = easyocr.Reader(['en'])
result = reader.readtext(img)
print(result[0][-2])
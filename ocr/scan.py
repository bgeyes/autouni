import cv2
import numpy as np 
import pytesseract
from PIL import Image

img = cv2.imread("gaus.jpg")
retval, threshold = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2  = cv2.threshold(graysc, 200, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(graysc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
retval2, otsu = cv2.threshold(graysc, 12, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
otsu = np.float32(otsu)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst1 = cv2.cornerHarris(otsu,2,3,0.04)

#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)
#dst1 = cv2.dilate(dst1,None)

# Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.01*dst.max()]=[0,0,255]
#img[dst1>0.01*dst1.max()]=[0,0,255]

cv2.imshow("original", gray)
cv2.imshow("new", threshold)
cv2.imshow("new2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("otsu", otsu)


dst = cv2.cornerHarris(gray,2,3,0.01)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

#cv2.imshow('dst',img)
#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()

#cv2.imwrite("otsu2.jpg", otsu)
#cv2.imwrite("gaus2.jpg", gaus)

#print(pytesseract.image_to_string(Image.open('gaus.jpg')))

cv2.waitKey(0)
cv2.destroyAllWindows()

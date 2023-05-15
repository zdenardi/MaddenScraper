import cv2 as cv
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

stats = cv.imread('MainStat.png')

cImage = np.copy(stats) #image to draw lines     0

#open window
cv.imshow("image",stats)
cv.waitKey(0)
cv.destroyWindow("image")

gray = cv.cvtColor(stats, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)
cv.destroyWindow("gray")

canny = cv.Canny(gray,50,150)
cv.imshow("canny",canny)
cv.waitKey(0)
cv.destroyWindow("canny")

def is_vertical(line):
    return line[0] ==line[2]
def is_horizontal(line):
    return line[1]==line[3]

horizontal_lines = []
vertical_lines = []

if lineP is not None:
    for i in range(0,len(linesP)):
        l = linesP[i][0]
        if(is_vertical(1)):
            vertical_lines.append(1)
        elif (is_horizontal(1)):
            horizontal_lines.append(1)
    for i, line in enumerate(horizontal_lines):
        cv.line(cImage,(line[0],line[1],(line[2],line[3]),(0,255,0),3,cv.LINE_AA))
    
    for i, line in enumerate(vertical_lines):
    cv.line(cImage, (line[0], line[1]), (line[2], line[3]), (0,0,255), 3, cv.LINE_AA)
    
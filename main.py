from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imgPath = 'MainStat.png'
img = cv2.imread(imgPath)
pillowImg = Image.open(imgPath)
# text = pytesseract.image_to_string(img)
# print(text)

# def click_event(event,x,y,flags,params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'({x},{y})')
#         #put coords as text on image
#         cv2.putText(img, f'({x},{y})',(x,y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         cv2.circle(img,(x,y),3,(0,255,255),1)

# cv2.namedWindow('Point Coordinates')
# cv2.setMouseCallback('Point Coordinates',click_event)

# #display image
# while True:
#    cv2.imshow('Point Coordinates',img)
#    k = cv2.waitKey(1) & 0xFF
#    if k == 27:
#       break
# cv2.destroyAllWindows() 
left = 154
top = 420
right = 2418
bottom = 1200

x1 = 154
y1 = 601
x2 = 151
y2 = 1220
x3 = 2419
y3 = 1200
x4 = 2418
y4 = 599
# pdf = pytesseract.image_to_pdf_or_hocr('JustStat.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default
box = (left, top, right, bottom)

statBox = pillowImg.crop(box)
stats = pytesseract.image_to_string(statBox)
print(stats)
# statBox.show()
# cv2.waitKey(0)


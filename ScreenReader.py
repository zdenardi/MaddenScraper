import cv2 as cv
import pytesseract
import numpy as np
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

while(True):
    x1 = 1445
    x2 = 1835
    y1 = 152
    y2 = 547
    screen = pyautogui.screenshot()
    # Convert for CV
    screen = np.array(screen)
    # convert RGB to BGR
    screen = cv.cvtColor(screen,cv.COLOR_RGB2BGR)
    gray = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)


    # cv.rectangle(gray, (1445, 152), (2038, 547), (255, 0, 0), 2)
    just_stats = gray[y1:y2, x1:x2]
    text = pytesseract.image_to_string(just_stats)
    print(text)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# Todo - Class this, and make it callable to only call screenshots when I want, i Think adding a break after 23.
# So, get screenshot, crop it, get text, break.
# Then I can go into my controller file, import this. Then scrape the Madden data



# stats = cv.imread(r'StatsScreen.png')
# x1 = 1445
# x2 = 1840
# y1 = 152
# y2 = 547
#
# gray = cv.cvtColor(stats, cv.COLOR_BGR2GRAY)
#
# # cv.rectangle(gray, (1445, 152), (2038, 547) ,(255 , 0, 0), 2)
#
# just_stats = gray[y1:y2,x1:x2]
# #open window
# # cv.imshow("stats", gray)
# # cv.waitKey(0)
# # cv.destroyWindow("stats")
# text = pytesseract.image_to_string(just_stats)
# print(text)
#
#
# cv.imshow("cropped", just_stats)
# cv.waitKey(0)
# cv.destroyWindow('cropped')
#


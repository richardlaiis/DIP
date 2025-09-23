import cv2 as cv
# img = cv.imread("./Ouro_Kronii_Portrait.png")
img = cv.imread("./middle_finger.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0)

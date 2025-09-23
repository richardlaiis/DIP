import numpy as np
import cv2 as cv

img = cv.imread('middle_finger.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

#OR

height, width = img.shape[:2]
print(height, width)
res = cv.resize(img,(width//2, height//2), interpolation = cv.INTER_LINEAR)

cv.imshow("Hi", res)
k = cv.waitKey(0)

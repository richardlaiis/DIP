import cv2 as cv
import numpy as np
try:
    scale = float(input())
except:
    print('Invalid Input: Number is expected')
filename = 'me.jpg'

img = cv.imread(filename)
height, width = img.shape[0], img.shape[1]

height = int(scale * height)
width = int(scale * width)

result = cv.resize(img, (width, height), interpolation = cv.INTER_CUBIC)
# or INTER_LINEAR
cv.imwrite(f'{scale}_{filename}', result)

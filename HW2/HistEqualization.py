import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

assert len(sys.argv) == 2, "The program takes one file as argument!"
assert sys.argv[1].endswith('jpg') or sys.argv[1].endswith('png'), "This is not image file!"

filename = ""

try:
    filename = sys.argv[1]
except:
    print('Please enter filename!')

img = cv.imread(filename)
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
equalized_img = cv.equalizeHist(grey_img)

plt.subplot(2, 2, 1)
plt.hist(grey_img.ravel(),256,[0,256]);
plt.ylabel('count of pixels')
plt.xlabel('intensity')
plt.title('Original Greyscale Image')

plt.subplot(2, 2, 2)
plt.hist(equalized_img.ravel(),256,[0,256]);
plt.ylabel('count of pixels')
plt.xlabel('intensity')
plt.title('Histogram Equalized Image')

grey_img = cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB)
plt.subplot(2, 2, 3)
plt.imshow(grey_img)
plt.axis('off')

equalized_img = cv.cvtColor(equalized_img, cv.COLOR_GRAY2RGB)
plt.subplot(2, 2, 4)
plt.imshow(equalized_img)
plt.axis('off')

plt.tight_layout()
plt.show()
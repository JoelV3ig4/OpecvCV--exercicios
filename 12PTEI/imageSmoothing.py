import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C:\Users\joel2\OneDrive\Desktop\github\OpenCV\12PTEI\Imagens\Noisy Image-2.png')

blur = cv.blur(img,(15, 15))

plt.subplot(121), plt.imshow(img), plt.title('Fake')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title()
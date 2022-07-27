# Fotoforensics-ELA-Python-Script
That's is a useful script for getting analysis the image and get the hidden data from the image &amp; passwords , texts , messages 



Modules Link ==> https://pypi.org/project/opencv-python
Modules Link ==> https://pypi.org/project/numpy/


Basic Usage Guide ==> Just put the img names or path on the script run on the terminal or your console { command promet } cmd :)


import numpy as np 
import cv2 

img1 = cv2.imread("/PATH/")

jpg_quality1 = 95
jpg_quality2 = 90
scale = 15

cv2.imwrite("/PATH/_95_ELA.jpeg", img1, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality1])

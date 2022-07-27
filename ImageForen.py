import numpy as np 
import cv2 

img1 = cv2.imread("selfie.jpeg")

jpg_quality1 = 95
jpg_quality2 = 90
scale = 15

cv2.imwrite("Selfie_95_ELA.jpeg", img1, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality1])

img2 = cv2.imread("Selfie_95_ELA.jpeg")

diff1 = scale * cv2.absdiff(img1,img2)

cv2.imwrite("Selfie_90_ELA.jpeg", img2, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality2])

img3 = cv2.imread("Selfie_90_Ela.jpeg")

diff2 = scale * cv2.absdiff(img2,img3)

cv2.imwrite("Selfie_95_Ela.jpeg", diff1)
cv2.imwrite("Selfie_90_Ela.jpeg", diff2)

cv2.imshow("Result[1]", diff1)
cv2.imshow("Result[2]", diff2)
cv2.waitKey(0)
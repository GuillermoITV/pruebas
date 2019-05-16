import cv2
import numpy as np
image1 = cv2.inread("1.jpg")
image2 = cv2.inread("2.jpg")

difference = cv2.subtract (image1, image2)
result = not np.any(difference) 

if result is True:
	print ("the images are the same")
else:
	cv2.imwrite("result.jpg", difference)
	print ("the images are different")
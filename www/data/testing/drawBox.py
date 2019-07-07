import cv2
import sys
import os

im = cv2.imread(sys.argv[1])
#36.57442428994048, 92.81321787977157, 101.78328557086536, 93.5864237676298
#182638.jpg   147  82 120 166
#202599.jpg   101 101 179 248
#cv2.rectangle(im, (37, 93), (139, 187), (255,0,0), 2)
#202584.jpg    38  30  60  83
#cv2.rectangle(im, (38, 30), (98, 113), (255,0,0), 2)
red = [0,0,255]
im[134, 87] = red
im[132, 92] = red
im[132, 100] = red
im[137, 107] = red
cv2.imwrite("output.jpg", im)

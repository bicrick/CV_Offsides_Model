import numpy as np
import cv2
import math
import json
import sys
import os
import warnings
from vanishingPoints import *
from playerDetection import get_field_positions
from offsidesCalculation import *

#CONFIG
goalDirection = 'left'
curImage = 0

#Dataset Path
dataset_path = '\Dataset\Offside_Images'
cur_path = os.getcwd()


initial_image = cv2.imread(cur_path+dataset_path+"/"+str(curImage)+".jpg")

imageForVanishingPoints = initial_image.copy()

print('Starting Vanishing Point calculation')
vertical_vanishing_point = get_vanishing_point_v(imageForVanishingPoints, goalDirection)
horizontal_vanishing_point = get_vanishing_point_h(imageForVanishingPoints)
print(horizontal_vanishing_point)
print('Finished Vanishing Point calculation')

print('Starting Player Detection and Classification')
red_pos,white_pos,img_final = get_field_positions('Dataset/Offside_Images/',curImage,goalDirection)
# img_color = cv2.cvtColor(img_final,cv2.COLOR_RGB2BGR)
# cv2.imwrite('boxesImage.jpg',img_color)
print('Ending Player Detection')

print('Beginning Offsides Calculations')
#linesImg = drawLines(red_pos,white_pos,vertical_vanishing_point,img_final)
#cv2.imwrite('linesImage.jpg',linesImg)
final = determineOffsides(red_pos,white_pos,vertical_vanishing_point,img_final,goalDirection)
cv2.imwrite('Output/'+str(curImage)+'Final.jpg',final)
print('Ending Ofssides Calculation')
print('Finished')

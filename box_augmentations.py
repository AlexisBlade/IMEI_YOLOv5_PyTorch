import torch
import torchvision.transforms as transforms
import glob
import matplotlib.pyplot as plt
import numpy as np
import torchvision
import time
import albumentations as A
import os
import numpy
import math as m
from torch.utils.data import DataLoader, Dataset
from PIL import Image

# Rotation func
def rotation(angle, point):
    res = [None]*2
    rad = m.radians(angle)
    sin = m.sin(rad)
    cos = m.cos(rad)
    res[0] = (point[0] * cos) + (point[1] * sin)
    res[1] = (-point[0] * sin) + (point[1] * cos)
    return(res)

# Cartesian plane +
def pointMovePlus(point):
    res = [None]*2
    res[0] = point[0] + 0.5
    res[1] = point[1] + 0.5
    return(res)

# Cartesian plane -
def pointMoveMinus(point):
    res = [None]*2
    res[0] = point[0] - 0.5
    res[1] = point[1] - 0.5
    return(res)

box = []

code = open('dooge_s70_jpg.rf.cb4164c55e9752fa2bc96ef9e4e754a8.txt', 'r')
image = open('dooge_s70_jpg.rf.cb4164c55e9752fa2bc96ef9e4e754a8.jpg', 'r')
box = code.read()
box = box.split(" ")

box = [float(x) for x in box] # all numbers to float

box_type_number = box[0] # index of type of bounding box
a_point_x = box[1] # x point
a_point_y = box[2] # y point
box_width = box[3] # width
box_height = box[4] # height


# Find other 3 points
a = [a_point_x, a_point_y] 
b = [a_point_x + box_width, a_point_y]
c = [a_point_x + box_width, a_point_y + box_height]
d = [a_point_x, a_point_y + box_height]

print("-----------------------CURRENT DATA-----------------------")

# Shows Current Data
print('Current x: ' + str(box[1]))
print('Current y: ' + str(box[2]))
print('Current width: ' + str(box[3]))
print('Current height: ' + str(box[4]))

print("-----------------------POINTS-----------------------")

# Shows All Points
print('Point A: ' + str(a))
print('Point B: ' + str(b))
print('Point C: ' + str(c))
print('Point D: ' + str(d))

print("-----------------------ROTATED POINTS-----------------------")

# Rotated Points and New Width/Height
rotated_a = pointMovePlus(rotation(180, pointMoveMinus(a)))
rotated_b = pointMovePlus(rotation(180, pointMoveMinus(b)))
rotated_c = pointMovePlus(rotation(180, pointMoveMinus(c)))
rotated_d = pointMovePlus(rotation(180, pointMoveMinus(d)))
new_Width = rotated_c[0] - rotated_a[0]
new_Height = rotated_c[1] - rotated_a[1]

print('Rotated A: ' + str(rotated_a))
print('Rotated B: ' + str(rotated_b))
print('Rotated C: ' + str(rotated_c))
print('Rotated D: ' + str(rotated_d))
print("Rotated Width: " + str(new_Width))
print("Rotated Height: " + str(new_Height))

print("-----------------------MIN & MAX X/Y-----------------------")

x_rotated_min = min(rotated_a[0], rotated_b[0], rotated_c[0], rotated_d[0])
y_rotated_min = min(rotated_a[1], rotated_b[1], rotated_c[1], rotated_d[1])
x_rotated_max = max(rotated_a[0], rotated_b[0], rotated_c[0], rotated_d[0])
y_rotated_max = max(rotated_a[1], rotated_b[1], rotated_c[1], rotated_d[1])

print('X & Y min: ' + str(x_rotated_min) + ' ' + str(y_rotated_min))
print('X & Y max: ' + str(x_rotated_max) + ' ' + str(y_rotated_max))

a_final = [x_rotated_min, y_rotated_min]
c_final = [x_rotated_max, y_rotated_max]
b_final = [x_rotated_max, y_rotated_min]
d_final = [x_rotated_min, y_rotated_max]

width_final = x_rotated_max-x_rotated_min
heigth_final = y_rotated_max-y_rotated_min

print("-----------------------FINAL-----------------------")

print(a_final)
print(width_final)
print(heigth_final)

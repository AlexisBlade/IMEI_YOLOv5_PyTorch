import torch
import torchvision.transforms as transforms
import glob
import matplotlib.pyplot as plt
import numpy as np
import torchvision
import time
import albumentations as A
import os
from torch.utils.data import DataLoader, Dataset
from PIL import Image

codes_mass = []
images_mass = []

codes = open('codes.txt', 'r')
images = open('images.txt', 'r')

codes_mass = codes.read().splitlines()
images_mass = images.read().splitlines()


for i in range(len(codes_mass)):
    current_code_url = '/train/labels/' + codes_mass[i];
    print('current code ' + str(i) + ': ' + current_code_url)
    #print(codes_mass[i][:-4] + '\n')

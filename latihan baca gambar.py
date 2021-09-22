# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:24:01 2021

@author: baraya
"""

import cv2
from matplotlib import pyplot as plt

image_path = "C:/Users/baraya/Documents/Ozan/Kuliah/Python/ob detect/latihan 1/Untitled.png"

# membaca gambar
gambar = cv2.imread(image_path)
# menampilkan gambar
cv2.imshow('spiderman.png', gambar)
# menyimpan gambar
cv2.imwrite('spiderman_save.png', gambar)

# Menunda windows terdestroy
cv2.waitKey(0)

#Mendestroy windows
cv2.destroyAllWindows()
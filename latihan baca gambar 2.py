# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:11:21 2021

@author: baraya
"""

import cv2
import matplotlib
import matplotlib.pyplot as plt

image_path = "C:/Users/baraya/Documents/Ozan/Kuliah/Python/ob detect/latihan 1/Untitled.png"
plt.style.use('dark_background')

# membaca gambar
gambar = cv2.imread(image_path)
# menampilkan gambar dengan menggunakan matplotlib
plt.imshow(gambar)
plt.xticks([]), plt.yticks([])
plt.show()
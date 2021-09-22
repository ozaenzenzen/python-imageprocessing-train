# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:31:07 2021

@author: baraya
"""

import cv2

# variabel untuk video capture
cap = cv2.VideoCapture(1)

# Fungsi untuk memebuat frame pengaturan pada video
while(True):
    # Membaca video
    ret, frame = cap.read()
    # Menampilkan video
    cv2.imshow('frame', frame)
    # pengaturan frame
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
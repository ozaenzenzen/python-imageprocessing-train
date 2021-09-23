# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:41:48 2021

@author: baraya
"""
import cv2

video_path = "C:/Users/baraya/Documents/Ozan/Media/Video/VID_20201112_172415.mp4"

capture = cv2.VideoCapture(video_path)

while(True):
    ret, frame = capture.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('video', gray)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
    
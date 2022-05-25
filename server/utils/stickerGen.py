# type: ignore
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import dlib
import time

file_dir = os.path.dirname(__file__)

def stickerGen(filePath):
    my_image_path_encode= np.fromfile(filePath, np.uint8)
    img_bgr = cv2.imdecode(my_image_path_encode,cv2.IMREAD_UNCHANGED)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    detector_hog = dlib.get_frontal_face_detector()
    dlib_rects = detector_hog(img_rgb, 1) 

    model_path = file_dir+'/models/shape_predictor_68_face_landmarks.dat'
    landmark_predictor = dlib.shape_predictor(model_path)

    list_landmarks = []

    for dlib_rect in dlib_rects:
        points = landmark_predictor(img_rgb, dlib_rect)
        list_points = list(map(lambda p: (p.x, p.y), points.parts()))
        list_landmarks.append(list_points)

    for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
        x = landmark[30][0]
        y = landmark[30][1] - dlib_rect.height()//2
        w = h = dlib_rect.width()

    sticker_path = file_dir+'/images/king.png'
    img_sticker = cv2.imread(sticker_path) 
    img_sticker = cv2.resize(img_sticker, (w,h))

    refined_x = x - w // 2
    refined_y = y - h

    if refined_x < 0: 
        img_sticker = img_sticker[:, -refined_x:]
        refined_x = 0
    if refined_y < 0:
        img_sticker = img_sticker[-refined_y:, :]
        refined_y = 0

    sticker_area = img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
    img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
        np.where(img_sticker==0,sticker_area,img_sticker).astype(np.uint8)

    cv2.imwrite(filePath, img=img_bgr) 

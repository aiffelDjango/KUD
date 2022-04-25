# Section 1
# 라이브러리 설정
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import dlib

# Section 2
# 사진 설정
def stickerGen(img):
    my_image_path = "C:/Users/kimud/KUD/firstproejct/media/bfImages/"+img
    my_image_path_encode= np.fromfile(my_image_path, np.uint8)
    img_bgr = cv2.imdecode(my_image_path_encode,cv2.IMREAD_UNCHANGED)    # OpenCV로 이미지를 불러옵니다
    img_show = img_bgr.copy()      # 출력용 이미지를 따로 보관합니다

    # Section 3
    # SVG detector를 선언합니다
    detector_hog = dlib.get_frontal_face_detector()

    # Bounding box 추출
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    dlib_rects = detector_hog(img_rgb, 1)   # (image, num of image pyramid)

    # Section 3
    # Bounding box 그리기 
    for dlib_rect in dlib_rects:
        l = dlib_rect.left()
        t = dlib_rect.top()
        r = dlib_rect.right()
        b = dlib_rect.bottom()

        cv2.rectangle(img_show, (l,t), (r,b), (0,255,0), 2, lineType=cv2.LINE_AA)

    img_show_rgb =  cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)
    # plt.imshow(img_show_rgb)
    # plt.show()

    # Section 4
    # LandMark 찍기

    model_path = 'C:/Users/kimud/KUD/firstproejct/static/camera_sticker/models/shape_predictor_68_face_landmarks.dat'
    landmark_predictor = dlib.shape_predictor(model_path)

    list_landmarks = []

    # 얼굴 영역 박스 마다 face landmark를 찾아냅니다
    for dlib_rect in dlib_rects:
        points = landmark_predictor(img_rgb, dlib_rect)
        # face landmark 좌표를 저장해둡니다
        list_points = list(map(lambda p: (p.x, p.y), points.parts()))
        list_landmarks.append(list_points)


    # Section 5
    # LandMark 출력

    for landmark in list_landmarks:
        for point in landmark:
            cv2.circle(img_show, point, 2, (0, 255, 255), -1)

    img_show_rgb = cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)


    # Section 6
    # 스티커 위치 구하기

    for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
        x = landmark[30][0]
        y = landmark[30][1] - dlib_rect.height()//2
        w = h = dlib_rect.width()

    # 스티커 사이즈 조절
    sticker_path = 'C:/Users/kimud/KUD/firstproejct/static/camera_sticker/images/king.png'
    img_sticker = cv2.imread(sticker_path) # 스티커 이미지를 불러옵니다
    img_sticker = cv2.resize(img_sticker, (w,h))

    # 스티커위치 조정 
    refined_x = x - w // 2
    refined_y = y - h

    # 스티커 위치 넘어가면 잘리게 
    if refined_x < 0: 
        img_sticker = img_sticker[:, -refined_x:]
        refined_x = 0
    if refined_y < 0:
        img_sticker = img_sticker[-refined_y:, :]
        refined_y = 0

    # Section 7
    # 사진에 적용후 출력


    sticker_area = img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
    img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
        np.where(img_sticker==0,sticker_area,img_sticker).astype(np.uint8)

    cv2.imwrite("C:/Users/kimud/KUD/firstproejct/media/afImages/"+img, img_bgr)

stickerGen( "Image.png")
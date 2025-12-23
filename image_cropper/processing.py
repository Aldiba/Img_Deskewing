# image_cropper/processing.py

import cv2
import numpy as np

def straighten_and_crop(image_cv, contour):
    """
    根据轮廓旋转图像（微调 +/- 45度），防止翻转。
    """
    rect = cv2.minAreaRect(contour)
    (cx, cy), (w, h), angle = rect

    # 角度规范化，防止180度翻转
    if angle < -45:
        angle += 90
        w, h = h, w
    elif angle > 45:
        angle -= 90
        w, h = h, w

    (h_img, w_img) = image_cv.shape[:2]
    center = (w_img // 2, h_img // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    contour_points = contour.reshape(-1, 1, 2).astype(np.float32)
    rotated_contour_points = cv2.transform(contour_points, M)
    
    x, y, w_crop, h_crop = cv2.boundingRect(rotated_contour_points)

    if w_crop <= 0 or h_crop <= 0:
        return np.full((10, 10, 3), 255, dtype=np.uint8)

    M[0, 2] -= x
    M[1, 2] -= y

    final_image = cv2.warpAffine(
        image_cv, M, (w_crop, h_crop),
        flags=cv2.INTER_CUBIC, 
        borderMode=cv2.BORDER_CONSTANT, 
        borderValue=(255, 255, 255)
    )
    
    return final_image
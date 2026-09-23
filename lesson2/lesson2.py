import cv2
import numpy as np

img = cv2.imread('asd.jpg')

blurred = cv2.GaussianBlur(img, (5,5), sigmaX=1.5) # размытие по гауссу

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # ядро повышения резкости
sharpened = cv2.filter2D(img, -1, kernel)


# Оператор Собеля

grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)


# Алгоритм Кэнни
edges = cv2.Canny(img, 100, 200)
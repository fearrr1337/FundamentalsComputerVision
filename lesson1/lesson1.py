import cv2

img = cv2.imread('asd.jpg') # загрузка изображения

cv2.imshow('Original', img) # отображение

# Ожидание и закрытие окон
cv2.waitKey(0) # 0 - бесконечное ожидание
cv2.destroyAllWindows()
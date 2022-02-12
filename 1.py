import pywhatkit as kit
import cv2
kit.text.to_handwriting("I can writing ", save_to ='1.jpg')
img = cv2.imread('1.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

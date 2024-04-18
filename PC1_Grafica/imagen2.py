import cv2  # opn cv
import pickle # formato para pasar datos
import numpy as np

# estacionamientos = []
# with open('espacios.pkl', 'rb') as file: # esto es con todos los estacionamintos que teniamos
#     estacionamientos = pickle.load(file)
# Load the image
# img = cv2.imread('comedor7 - copia.png')
    # escala de grises, no nos importa los colores de autos
# imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # aplicar una humbralizacion, en este caso adaptativo
#     # más info en https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# imgTH = cv2.adaptiveThreshold(imgBN, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
#     # más info en https://theailearner.com/tag/cv2-medianblur/
#     # filtro pasa baja, dilatar las areas o regiones d ela imagen
# imgMedian = cv2.medianBlur(imgTH, 5)
# kernel = np.ones((5,5), np.int8)
#     # dilatar las áreas o regiones de la imagen
# imgDil = cv2.dilate(imgMedian, kernel)
# num_estacionamiento = 0
# for x, y, w, h in estacionamientos:
#     espacio = imgDil[y:y+h, x:x+w]
#     print(espacio.shape)
#     totales = espacio.shape[0]*espacio.shape[1] # espacio.sum()
#     count = cv2.countNonZero(espacio)
#     print(count, totales, count/totales)
# print(img)
# print(img.shape)

video2 = cv2.VideoCapture('videofb3.mp4')
print(video2.read())
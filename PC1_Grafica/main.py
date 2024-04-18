import cv2  # opn cv
import pickle # formato para pasar datos
import numpy as np

estacionamientos = []
with open('espacios.pkl', 'rb') as file: # esto es con todos los estacionamintos que teniamos
    estacionamientos = pickle.load(file)

# leer el video 
video = cv2.VideoCapture('videofb3.mp4')

while True:
    check, img = video.read()
    # escala de grises, no nos importa los colores de autos
    imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # aplicar una humbralizacion, en este caso adaptativo
    # más info en https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    imgTH = cv2.adaptiveThreshold(imgBN, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    # más info en https://theailearner.com/tag/cv2-medianblur/
    # filtro pasa baja, dilatar las areas o regiones d ela imagen
    imgMedian = cv2.medianBlur(imgTH, 5)
    kernel = np.ones((5,5), np.int8)
    # dilatar las áreas o regiones de la imagen
    imgDil = cv2.dilate(imgMedian, kernel)
    num_estacionamiento = 0
    # w anchi
    # h height
    for x, y, w, h in estacionamientos:
        espacio = imgDil[y:y+h, x:x+w]
        totales = espacio.shape[0]*espacio.shape[1] # len(espacio[0]) # espacio[0].sum()
        count = cv2.countNonZero(espacio)
        # cv2.putText(img, str(count), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        cv2.putText(img, str(count/totales), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) # azul
        # if num_estacionamiento == 0 and count < 11000: # 
        if num_estacionamiento == 0 and count/totales < 0.16: # 
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) # verde
        elif count/totales < 0.17:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) # verde
        num_estacionamiento = num_estacionamiento + 1

    cv2.imshow('video', img)
    # cv2.imshow('video TH', imgTH)
    # cv2.imshow('video Median', imgMedian)
    # cv2.imshow('video Dilatada', imgDil)
    cv2.waitKey(10)
# el estacionamiento completo tiene mas pixeles activos
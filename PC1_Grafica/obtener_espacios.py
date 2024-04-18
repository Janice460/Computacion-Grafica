import cv2
import pickle

# leer una imagen
img = cv2.imread('comedorfb4.png') # leer la imagen en p

# creando una lista
espacios = []

for k in range(11):
    # marcar un rectángulo
    espacio = cv2.selectROI('espacio', img, False)
    cv2.destroyWindow('espacio')
    # añadir a la lista de espacios
    espacios.append(espacio)

    for x, y, w, h in espacios:
        # referencial: ver el rectángulo agregado
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

with open('espacios.pkl','wb') as file:
    # guardar el archivo
    pickle.dump(espacios, file)

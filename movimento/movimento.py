'''
    Programador.......:
    Date..............:
    Observações.......:
'''
import cv2 as cv
import numpy 

Webcam = cv.VideoCapture(0)

if not Webcam.isOpened():
    print('Não foi possível ativar a webcam.')
    exit()

while True:
    retorno, frame = Webcam.read()
    
    if not retorno:
        print('Erro na captura da webcam')
        break

    frameTonsCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    frameContornos = cv.Canny(frameTonsCinza, 100, 200)

    cv.imshow('Imagem Capturada pela webcam', frame)
    cv.imshow('Imagem Tons de cinza', frameTonsCinza)
    cv.imshow('Imagem de contornos', frameContornos)

    if cv.waitKey(1) == ord('q'):
        break

Webcam.release()
cv.destroyAllWindows()

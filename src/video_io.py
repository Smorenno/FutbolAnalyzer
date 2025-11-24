import cv2 as cv2
import os.path


def openVideo(videoRoute):
    if os.path.exists(videoRoute):
        video=cv2.VideoCapture(videoRoute)
        if not video.isOpened():
            raise Exception("No se puede abir el archivo")
        return video
    else:
        raise Exception(f"El archivo no existe: {videoRoute}")
    
def openFrames(videoRoute):
    capturador = openVideo(videoRoute)
    for i in range(int(capturador.get(cv2.CAP_PROP_FRAME_COUNT))):
        ret, frame = capturador.read()
        if not ret:
            break
        yield frame
    capturador.release()
        
            
        











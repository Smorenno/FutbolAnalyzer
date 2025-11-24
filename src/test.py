from detection import detect_players
from video_io import openFrames,openVideo
import cv2

videoRoute="data/input/video.mp4"
for frame in openFrames(videoRoute):
    players = detect_players(frame)
    for x1, y1, x2, y2, conf in players:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1000)  # espera hasta que pulses una tecla
    if key == ord('x'):
        break
cv2.destroyAllWindows()

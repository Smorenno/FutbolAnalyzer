from detection import detect_players
from video_io import openFrames
import cv2
from analytics import add_player_team

videoRoute="data/input/video.mp4"
teamSpain=[]
teamNetherlands=[]
for frame in openFrames(videoRoute):
    players = detect_players(frame)

    # Contadores por frame
    count_spain = 0
    count_netherlands = 0

    for player in players:
        x1, y1, x2, y2, conf = player
        team_predicted = add_player_team(frame, [x1, y1, x2, y2])
         # Elegir color según equipo

        if team_predicted == "Spain":
            color = (0, 255, 0)  # verde
            count_spain += 1
        elif team_predicted == "Netherlands":
            color = (0, 0, 255)  # rojo
            count_netherlands += 1
        else:
            color = (128, 128, 128)  # gris para desconocido
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

    cv2.putText(frame, f"Spain: {count_spain}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, f"Netherlands: {count_netherlands}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1000)  # espera hasta que pulses una tecla
    if key == ord('x'):
        break

cv2.destroyAllWindows()

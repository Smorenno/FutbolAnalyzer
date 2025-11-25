import cv2
teamSpain=[]
teamNetherlands=[]

def add_player_team(frame, box):

	x1, y1, x2, y2 = map(int, box)
	y2_cropped = y1 + int(0.5*(y2 - y1))
	box_cropped = frame[y1:y2_cropped, x1:x2]
	roi_hsv = cv2.cvtColor(box_cropped, cv2.COLOR_BGR2HSV)
	hue_avg = roi_hsv[:,:,0].mean()
	sat_avg = roi_hsv[:,:,1].mean()
	val_avg = roi_hsv[:,:,2].mean()

	# Ajuste para España (camiseta negra)
	if val_avg < 120 and sat_avg < 130:  
		teamSpain.append(box)
		return "Spain"

	# Holanda (camiseta naranja)
	elif 10 <= hue_avg <= 25 and sat_avg > 80 and val_avg > 50:
		teamNetherlands.append(box)
		return "Netherlands"

	else:
		return "Unknown"

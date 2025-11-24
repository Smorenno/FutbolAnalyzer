import torch 
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_players(frame):
    """Detect players in a given frame using YOLOv5 model."""
    players=[]
    results = model(frame)
    boxes = results.xyxy[0]
    for box in boxes:
        #Array que contiene [x1, y1, x2, y2, conf, cls]
        x1, y1, x2, y2, conf, cls = box
        if int(cls)==0 :
            players.append([int(x1), int(y1), int(x2), int(y2), conf])
    return players  




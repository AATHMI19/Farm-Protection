from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import detection

import cv2


model = YOLO("Model/best.pt")

model.predict(source="0", show=True, conf=0.5)
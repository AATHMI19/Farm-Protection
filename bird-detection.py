import serial
import torch
from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("Model/best.pt")

# Define class labels
class_labels = ['Asian_green_bee_eater', 'Cattle_egret', 'Crow', 'Hoopoe', 'Kingfisher', 'Myna', 'Peacock', 'Rosefinch',
                'Schelduck', 'Tailorbird', 'Wagtail']
serial_codes = ['*1', '*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*a', '*b']

# Open serial communication with Arduino
ser = serial.Serial("COM3", 9600)  # Change COM port accordingly

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])  # Get class index
            label = class_labels[cls]
            serial_data = serial_codes[cls]  # Get corresponding serial code

            # Send data to Arduino
            ser.write(serial_data.encode())
            print(f"Detected: {label}, Sent: {serial_data}")

            # Draw bounding box and label
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display frame
    cv2.imshow("Bird Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
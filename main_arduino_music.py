import serial
import torch
from ultralytics import YOLO
import cv2
import time
import pygame  # For playing audio
import random  # To play random sounds for missing classes

# Initialize pygame mixer
pygame.mixer.init()

# Load YOLOv8 model
model = YOLO("Model/best.pt")

# Define class labels
class_labels = ['Asian_green_bee_eater', 'Cattle_egret', 'Crow', 'Hoopoe', 'Kingfisher', 'Myna', 'Peacock', 'Rosefinch',
                'Schelduck', 'Tailorbird', 'Wagtail']
serial_codes = ['*1', '*1', '*1', '*1', '*1', '*1', '*1', '*1', '*1', '*1', '*1']

# List of 7 bird sound files
bird_sounds = ["music/bird1.mp3", "music/bird2.mp3", "music/bird3.mp3",
               "music/bird4.mp3", "music/bird5.mp3", "music/bird6.mp3",
               "music/bird7.mp3"]

# Confidence threshold (80%)
CONFIDENCE_THRESHOLD = 0.5

# Open serial communication with Arduino
ser = serial.Serial("COM3", 9600)  # Change COM port accordingly

url = "http://192.168.43.2:81/stream"

# Open webcam
cap = cv2.VideoCapture(0)

last_play_time = 0  # Track the last time audio was played
audio_delay = 10  # Delay in seconds to prevent mismatches

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame)

    for result in results:
        for box in result.boxes:
            confidence = box.conf[0].item()  # Get confidence score
            if confidence < CONFIDENCE_THRESHOLD:  # Skip detections below 80% confidence
                continue

            cls = int(box.cls[0])  # Get class index
            if cls < len(class_labels):  # Ensure class is within range
                label = class_labels[cls]
                serial_data = serial_codes[cls]  # Get corresponding serial code
            else:  # Handle missing classes
                label = "Unknown Bird"
                serial_data = "*x"  # Default serial code for unknown birds

            # Send data to Arduino
            ser.write(serial_data.encode())
            print(f"Detected: {label} (Confidence: {confidence:.2f}), Sent: {serial_data}")

            # Play appropriate audio if 10 seconds have passed
            current_time = time.time()
            if current_time - last_play_time > audio_delay:
                if cls < len(bird_sounds):  # If class is within known range
                    audio_file = bird_sounds[cls % len(bird_sounds)]  # Select corresponding sound
                else:  # If class is missing, pick a random sound
                    audio_file = random.choice(bird_sounds)

                pygame.mixer.music.load(audio_file)  # Load selected .mp3 file
                pygame.mixer.music.play()  # Play the sound

                last_play_time = current_time  # Update last play time

            # Draw bounding box and label
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} ({confidence:.2f})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display frame
    cv2.imshow("Bird Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()

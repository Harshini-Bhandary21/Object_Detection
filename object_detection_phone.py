import cv2
import torch

url = "http://10.203.219.49:4747/video"
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
cap = cv2.VideoCapture(url)
if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    results = model(frame)
    frame = results.render()[0]
    cv2.imshow("Phone Webcam Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
from ultralytics import YOLO
import cv2

# Step 1: Load YOLO model (pretrained on COCO dataset)
model = YOLO("yolov8n.pt")  # n = nano version (lightweight, faster)

# Step 2: Use your phone camera stream
url = "http://10.203.219.49:4747/video"  # replace with your phone's IP

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Check URL or connection.")
        break

    # Step 3: Perform detection
    results = model(frame)

    # Step 4: Draw boxes and labels on the image
    annotated_frame = results[0].plot()

    # Step 5: Display result
    cv2.imshow("Object Detection (Phone Camera)", annotated_frame)

    # Quit when you press 'q'
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

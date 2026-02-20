from ultralytics import YOLO
import cv2
import time

# Load trained model
model = YOLO("runs/detect/train9/weights/best.pt")
cap = cv2.VideoCapture(0)

target_fps = 2
frame_time = 1 / target_fps

while True:
    start = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (416, 416))

    results = model(frame, imgsz=416)

    annotated_frame = results[0].plot()

    fps = 1 / (time.time() - start)

    cv2.putText(annotated_frame, f"FPS: {int(fps)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Real-Time Pothole Detection", annotated_frame)

    elapsed = time.time() - start
    if elapsed < frame_time:
        time.sleep(frame_time - elapsed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
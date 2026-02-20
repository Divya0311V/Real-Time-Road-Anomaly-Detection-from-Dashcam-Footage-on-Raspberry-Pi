import cv2
import time
import csv

cap = cv2.VideoCapture(0)

log_file = open("anomaly_log.csv", "a", newline="")
csv_writer = csv.writer(log_file)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add timestamp
    timestamp = time.strftime("%H:%M:%S")
    cv2.putText(frame, timestamp, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Dashcam Simulation", frame)

    key = cv2.waitKey(1)

    # Press 'd' to simulate detection
    if key == ord('d'):
        print("Anomaly Detected!")
        csv_writer.writerow([timestamp, "Pothole", 0.85])
        cv2.imwrite(f"frame_{timestamp}.jpg", frame)

    # Press 'q' to quit
    if key == ord('q'):
        break

cap.release()
log_file.close()
cv2.destroyAllWindows()

from ultralytics import YOLO

# Load base YOLOv5s
model = YOLO("yolov5s.pt")

# Train on pothole dataset
model.train(
    data="Pothole_Dataset/data.yaml",
    epochs=10,
    imgsz=640,
    batch=16
)

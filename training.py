from ultralytics import YOLO

# yolo model creation
model = YOLO("yolo-weights/yolov8l.pt")
model.train(data=r"D:\HOPE\Projects\Helmet_detection\Helmet_detection_with_number_plate\data\coco128.yaml", imgsz=320, batch=4, epochs=20, workers=0)

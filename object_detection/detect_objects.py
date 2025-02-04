import torch
import cv2
import os
import json
import sqlite3
from pathlib import Path
from yolov5 import detect  # Import YOLO detection script

# Load the YOLOv5 model (pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Directory containing images to process
IMAGE_DIR = "images/"
RESULTS_DIR = "results/"
DB_PATH = "object_detection.db"

# Ensure the results directory exists
Path(RESULTS_DIR).mkdir(parents=True, exist_ok=True)

def detect_objects(image_path):
    """Perform object detection on an image and store results."""
    img = cv2.imread(image_path)
    results = model(image_path)  # Run YOLO model
    detections = results.pandas().xyxy[0]  # Get detection results

    detected_objects = []
    for _, row in detections.iterrows():
        obj = {
            "class": row["name"],
            "confidence": row["confidence"],
            "x_min": int(row["xmin"]),
            "y_min": int(row["ymin"]),
            "x_max": int(row["xmax"]),
            "y_max": int(row["ymax"])
        }
        detected_objects.append(obj)

    return detected_objects

def store_results(image_name, detections):
    """Store object detection results in SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS detections (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        image_name TEXT,
                        detected_data TEXT)''')

    cursor.execute("INSERT INTO detections (image_name, detected_data) VALUES (?, ?)",
                   (image_name, json.dumps(detections)))
    conn.commit()
    conn.close()

# Process all images in the directory
for img_file in os.listdir(IMAGE_DIR):
    img_path = os.path.join(IMAGE_DIR, img_file)
    detections = detect_objects(img_path)
    store_results(img_file, detections)
    print(f"Processed {img_file}: {len(detections)} objects detected.")

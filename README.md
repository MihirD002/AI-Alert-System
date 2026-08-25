# AI Alert System

A comprehensive computer vision project designed to detect traffic violations by identifying helmets, vehicles, and license plates using deep learning models. This system leverages YOLOv8 for real-time object detection and tracking to enforce road safety regulations.

## 🎯 Project Overview

The AI Alert System is a backend project that combines multiple AI models to:
- Detect vehicles in traffic footage
- Identify riders without helmets
- Recognize license plates
- Track vehicles across frames
- Generate alerts for safety violations

This is an ideal solution for traffic enforcement, highway monitoring, and road safety applications.

## ✨ Features

- **Vehicle Detection**: Uses YOLOv8 (COCO model) to detect cars, motorcycles, and buses
- **Helmet Detection**: Custom-trained YOLOv8 model to detect helmets and identify riders without helmets
- **License Plate Recognition**: Detects and extracts license plate information
- **Object Tracking**: Implements SORT algorithm for consistent vehicle tracking across frames
- **OCR Support**: Integrates EasyOCR for license plate text recognition
- **CSV Reporting**: Exports detection results to CSV format for analysis
- **Video Processing**: Processes video files frame-by-frame for detection and analysis

## 🛠️ Tech Stack

- **Backend**: Python
- **Frontend**: HTML, CSS, JavaScript
- **Deep Learning Framework**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Data Processing**: Pandas, NumPy, SciPy
- **OCR**: EasyOCR
- **Tracking**: SORT (Simple Online and Realtime Tracking)

## 📁 Project Structure

```
AI-Alert-System/
├── main3.py                 # Primary detection and tracking script
├── util.py                  # Utility functions (bbox processing, OCR, CSV writing)
├── predict.py               # Prediction helper functions
├── add_missing_data.py      # Data preprocessing script
├── video_to_image.py        # Video frame extraction utility
├── visualize.py             # Visualization and result analysis
├── config.yaml              # Model and dataset configuration
├── config2.yaml             # Alternative configuration
├── requirements.txt         # Python dependencies
├── yolov8n.pt              # Pre-trained YOLOv8 nano model weights
├── runs/                    # Trained model outputs and checkpoints
├── models/                  # Custom trained models
├── ai_alert_system/         # Python package directory
├── index.html               # Main web interface
├── working.html             # Working page
├── tryourmodel.html         # Model testing interface
└── assets/                  # CSS and JavaScript files
```

## 🧠 Models Used

### 1. YOLOv8 COCO (Vehicle Detection)
- Pre-trained model: `yolov8n.pt` (nano version)
- Detects: cars, motorcycles, buses, and other vehicles
- Classes: 80 COCO classes

### 2. Custom License Plate Detector
- Location: `./runs/detect/train2/weights/best.pt`
- Trained on custom dataset
- Detects: license plates, helmets, and riders

## 📊 Key Functions

### Vehicle Detection
```python
coco_model = YOLO('yolov8n.pt')
detections = coco_model(frame)[0]
```

### License Plate Processing
```python
license_plate_detector = YOLO('./runs/detect/train2/weights/best.pt')
license_plates = license_plate_detector(frame)[0]
```

### Object Tracking
```python
from sort.sort import Sort
mot_tracker = Sort()
track_ids = mot_tracker.update(detections)
```

### License Plate OCR
```python
license_plate_text, confidence = read_license_plate(license_plate_crop_thresh)
```

## 🔍 Detection Pipeline

1. **Frame Reading**: Extract frames from video file
2. **Vehicle Detection**: Identify vehicles using YOLOv8 COCO model
3. **Vehicle Tracking**: Maintain consistent IDs across frames using SORT
4. **License Plate Detection**: Detect license plate regions
5. **Helmet Detection**: Identify helmet presence/absence
6. **Proximity Analysis**: Check if rider is near their license plate
7. **OCR Recognition**: Extract license plate text
8. **Alert Generation**: Flag violations (no helmet with nearby plate)
9. **Data Export**: Write results to CSV

## ⚠️ Safety Violations Detected

- **No Helmet**: Rider detected without helmet near license plate
- **Proximity Threshold**: Customizable threshold (default: 10000 pixels)

## 🎨 Web Interface

The project includes a web-based interface for:
- Uploading and testing videos
- Viewing detection results
- Analyzing model performance
- Visualizing tracked objects

Access the web interface through:
- `index.html` - Main dashboard
- `tryourmodel.html` - Interactive model testing

## 📈 Results Analysis

Results are exported to CSV files with comprehensive detection data.

Each record contains:
- Frame number
- Vehicle tracking ID
- Bounding box coordinates
- Confidence scores
- License plate text
- Helmet status

**Repository**: [AI-Alert-System](https://github.com/MihirD002/AI-Alert-System)  
**Project Type**: BE Project 2024

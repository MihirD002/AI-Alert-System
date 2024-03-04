from ultralytics import YOLO
import cv2

import util
from sort.sort import *
from util import get_car, read_license_plate, write_csv, calculate_bbox_distance

proximity_threshold = 10000
results = {}
tanvi = []
mot_tracker = Sort()

# load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('./runs/detect/train2/weights/best.pt')

# load video
cap = cv2.VideoCapture('./sample 16.mp4')
vehicles = [3, 4]

# read frames
frame_nmr = -1
ret = True
while ret:
    frame_nmr += 1
    ret, frame = cap.read()
    if ret:
        results[frame_nmr] = {}
        # detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append(
                    [x1, y1, x2, y2, score])

        # track vehicles
        track_ids = mot_tracker.update(np.asarray(detections_))
        # implementing our model (helmet + license plate)
        license_plates = license_plate_detector(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            xyz = []
            xyz.append(int(class_id))

            # assign license plate to car
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(
                license_plate, track_ids)

            if car_id != -1:

                # crop license plate
                license_plate_crop = frame[int(
                    y1):int(y2), int(x1): int(x2), :]

                # process license plate
                license_plate_crop_gray = cv2.cvtColor(
                    license_plate_crop, cv2.COLOR_BGR2GRAY)
                _, license_plate_crop_thresh = cv2.threshold(
                    license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
                # continue  # Skip if not a relevant class

            # cv2.imshow('original_crop', license_plate_crop)
            # cv2.imshow('threshold', license_plate_crop_thresh)
            # cv2.waitKey(500)

                # read license plate number
            license_plate_text, license_plate_text_score = read_license_plate(
                license_plate_crop_thresh)

            if license_plate_text is not None:
                results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                              'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                'text': license_plate_text,
                                                                'bbox_score': score,
                                                                'text_score': license_plate_text_score,
                                                                'class_name': xyz
                                                                }
                                              }
                if class_id == 0:  # no_helmet
                    results[frame_nmr][car_id]['no_helmet'] = {'bbox': [x1, y1, x2, y2]
                                                               }
                    print("hello")
                 # Check proximity between number plate and rider's bounding box
                    rider_bbox = results[frame_nmr][car_id]['car']['bbox']
                    distance_license_plate_rider = calculate_bbox_distance(
                        license_plate, rider_bbox)
                    print("yo")
                    if distance_license_plate_rider < proximity_threshold:
                        print(
                            f"Frame {frame_nmr}: Rider {car_id} without helmet has a nearby license plate.")

                elif class_id == 1:  # helmet
                    results[frame_nmr][car_id]['helmet'] = {'bbox': [x1, y1, x2, y2]
                                                            }

# write results
write_csv(results, './newcode_22-2-24.csv')

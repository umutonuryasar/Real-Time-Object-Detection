import cv2
import numpy as np
from ultralytics import YOLO
from .utils import read_class_names

# Constants
video_file_path = "data/sample_video.mp4"
yolo_weights_path = "data/yolo-Weights/yolov8n.pt"
class_names_file = "data/classes.txt"

def main():
    # Open the video file
    cap = cv2.VideoCapture(video_file_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Load YOLO model
    model = YOLO(yolo_weights_path)
    class_names = read_class_names(class_names_file)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Perform object detection
        results = model(frame, stream=True)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Display confidence and class name
                confidence = np.round(box.conf[0], decimals=2)
                cls = int(box.cls[0])
                class_name = class_names[cls]

                text = f"{class_name}: {confidence:.2f}"
                org = (x1, y1 - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.5
                color = (0, 255, 0)
                thickness = 1

                cv2.putText(frame, text, org, font, font_scale, color, thickness)

        # Display the frame
        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

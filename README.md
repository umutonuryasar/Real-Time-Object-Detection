# Real-Time Object Detection

This project demonstrates real-time object detection using the YOLO (You Only Look Once) model. It allows you to perform object detection on a video file and draw bounding boxes around detected objects with their class labels and confidence scores.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [License](#license)

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/umutonuryasar/Real-Time-Object-Detection.git
   cd Real-Time-Object-Detection

2. Install the required Python packages using pip:
    
    ```bash
    pip install -r requirements.txt

## Usage

1. Make sure you have your video file (sample_video.mp4) and class names file (classes.txt) in the data/ directory. You can customize these files as needed.

2. Run the object detection script from the project root:
    
    ```bash
    python main.py

3. The object detection results will be displayed in a 'Object Detection' window. Press 'q' to exit the application.

## Project Structure

The project follows this directory structure:

```
Real-Time-Object-Detection/
│
├── data/
│   ├── sample_video.mp4
│   ├── classes.txt
│   └── yolo-Weights/
│       └── yolov8n.pt
│
├── src/
│   ├── __init__.py
│   ├── object_detection.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── main.py
```

- data/: Contains video and class names files.
- src/: Contains the project source code.
- requirements.txt: Lists project dependencies.
- main.py: Entry point for the project.

## Requirements

- Python 3.x
- OpenCV (opencv-python)
- Ultralytics (ultralytics)

You can install the required packages using pip as mentioned in the installation steps.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
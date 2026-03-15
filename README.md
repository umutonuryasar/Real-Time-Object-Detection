# Real-Time Object Detection

Real-time object detection pipeline using YOLOv8, built with Python and OpenCV. Processes video streams with per-frame inference, bounding box rendering, and confidence-thresholded class filtering.

**Stack:** Python · YOLOv8 (Ultralytics) · OpenCV · PyTorch

---

## Overview

This project implements a real-time detection pipeline around YOLOv8n — the nano variant of the YOLOv8 family, optimized for low-latency inference. The architecture follows a single-stage detection approach: a shared backbone extracts multi-scale features, a neck aggregates them via PANet-style fusion, and decoupled heads produce class and box predictions independently.

Key design decisions:

- **YOLOv8n** selected for real-time performance on CPU/GPU without sacrificing meaningful accuracy on standard classes
- **Decoupled heads** (separate classification and regression branches) improve training stability compared to coupled head designs in earlier YOLO versions
- **Confidence thresholding** applied post-inference to filter low-quality detections before rendering

---

## Architecture Notes

YOLOv8 uses a CSPDarknet-based backbone with C2f modules (Cross Stage Partial with two bottlenecks), which improves gradient flow compared to the C3 modules in YOLOv5. The neck uses a BiFPN-inspired feature pyramid for multi-scale detection — critical for handling objects at varying scales in a single forward pass.

This project uses the `yolov8n.pt` pretrained checkpoint (COCO-trained, 80 classes, ~3.2M parameters) for zero-shot inference on standard object categories.

---

## Project Structure

```
Real-Time-Object-Detection/
│
├── data/
│   ├── sample_video.mp4      # Input video
│   ├── classes.txt           # Class label mapping
│   └── yolo-Weights/
│       └── yolov8n.pt        # Pretrained YOLOv8n checkpoint
│
├── src/
│   ├── __init__.py
│   ├── object_detection.py   # Core inference loop
│   └── utils.py              # Bounding box rendering, label formatting
│
├── requirements.txt
├── main.py                   # Entry point
└── README.md
```

---

## Installation

```bash
git clone https://github.com/umutonuryasar/Real-Time-Object-Detection.git
cd Real-Time-Object-Detection
pip install -r requirements.txt
```

**Requirements:** Python 3.x · OpenCV (`opencv-python`) · Ultralytics (`ultralytics`)

---

## Usage

Place your video file at `data/sample_video.mp4`, then:

```bash
python main.py
```

Detections render in a live window. Press `q` to exit.

---

## Relation to Current Work

This project serves as a practical baseline for understanding single-stage detection pipelines. Current research extends this direction toward **transformer-based detectors** (RT-DETR) and **knowledge distillation** for improving the speed-accuracy trade-off — work ongoing as part of Stanford CS229.

---

## License

MIT — see [LICENSE](LICENSE)

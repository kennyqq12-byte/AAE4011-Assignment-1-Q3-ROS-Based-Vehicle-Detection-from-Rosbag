# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** [LaiKiUen] | **Student ID:** [25031657d] | **Date:** [17/3/2026]

---

## 1. Overview

*This project implements a real-time vehicle detection pipeline within the ROS Noetic environment. It processes a compressed image stream from a provided .bag file and utilizes a deep learning model to identify and label vehicles in a dynamic urban setting.*

## 2. Detection Method *(Q3.1 — 2 marks)*

*I chose the YOLOv5s (Small) architecture for this task. As an AAE student, I prioritized this model because it offers an optimal balance between inference speed and detection accuracy. YOLOv5's single-stage detection approach is particularly suited for UAS (Unmanned Aerial Systems) applications where real-time processing and low latency are critical for obstacle avoidance and surveillance.*

## 3. Repository Structure
```text
catkin_ws/
├── 2026-02-02-17-57-27.bag       # Rosbag file in workspace root
└── src/
    └── vehicle_detector/
        ├── CMakeLists.txt
        ├── package.xml
        └── scripts/
            ├── detector_node.py    # Main detection node
            ├── test_yolo.py        # Verification script
            └── yolov5s.pt          # YOLOv5 weight file
```

## 4. Prerequisites

OS: Ubuntu 20.04 LTS (WSL2)

ROS Version: Noetic Ninjemys

Python Version: 3.8.10

Key Libraries: torch==1.13.1, ultralytics, opencv-python, numpy.

## 5. How to Run *(Q3.1 — 2 marks)*

This section outlines the procedure to deploy the detection pipeline. Ensure my ROS Noetic environment is properly sourced before proceeding.

5.1 Workspace Initialization
Clone this repository into your catkin_ws/src folder, then build the workspace:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

5.2 Dependency Installation
The pipeline requires PyTorch and the Ultralytics engine. Install them using the following commands:
```bash
# Install core AI libraries
python3 -m pip install --user torch torchvision ultralytics
# Install OpenCV for image processing
python3 -m pip install --user opencv-python
```

5.3 Data Preparation
Place the provided rosbag file (2026-02-02-17-57-27.bag) directly into my ~/catkin_ws/ directory as specified in the repository structure.

5.4 Execution
To run the system, I need to open three separate terminal tabs:

1.Terminal 1 (Master): Start the ROS core.
```bash
roscore
```

2.Terminal 2 (Detector): Run the Python detection node.
```bash
chmod +x ~/catkin_ws/src/vehicle_detector/scripts/detector_node.py
python3 ~/catkin_ws/src/vehicle_detector/scripts/detector_node.py
```

3.Terminal 3 (Playback): Play the rosbag data.
```bash
rosbag play ~/catkin_ws/2026-02-02-17-57-27.bag
```

## 6. Sample Results

### 6.1 Image Extraction Summary

| Parameter | Value |
| :--- | :--- |
| **Topic Name** | `/hikcamera/image_2/compressed` |
| **Resolution** | 1280 x 720 (HD) |
| **Total Frames** | 1,142 frames |
| **Duration** | 114 seconds (1:54) |
| **Message Type** | `sensor_msgs/CompressedImage` |

Average Confidence: 0.85+ for cars in clear view.

Processing Speed: 15–20 FPS (CPU Inference).

Detection Classes: Car, Bus, Truck (COCO indices: 2, 5, 7).

Sample Screenshort
<img width="2183" height="1309" alt="螢幕擷取畫面 2026-03-16 030957" src="https://github.com/user-attachments/assets/6fe6421c-b171-4966-84f8-a77a341ffea7" />

## 7. Video Demonstration *(Q3.2 — 5 marks)*

**Video Link:** [YouTube (Unlisted)](https://youtu.be/yKaNZLUrX8o)

Startup: Showing how to source the workspace and launch the detector_node.py script.

Detection in Action: A screen recording of the YOLOv5 window identifying cars and trucks from the rosbag data.

Quick Summary: A brief look at the bounding boxes and confidence scores to prove the system works in real-time.

## 8. Reflection & Critical Analysis *(Q3.3 — 8 marks, 300–500 words)*

### (a) What Did You Learn? *(2 marks)*

*I gained hands-on experience in ROS-Python integration, specifically how to handle CompressedImage messages and convert them for use with deep learning frameworks. I also learned the importance of dependency management when working with different Python environments (System vs. Local) in Linux.*

### (b) How Did You Use AI Tools? *(2 marks)*

*I utilized AI assistants specifically for system-level troubleshooting rather than just code generation.

Practical Application: During development, I faced a critical ModuleNotFoundError where the ROS environment couldn't locate my installed torch library. The AI helped me diagnose this as a Python path conflict within WSL2. Following its advice, I implemented a manual path injection using sys.path.insert(0, user_site_packages) in my script, which successfully bridged the gap between my local pip installations and the ROS runtime.

Critique: While the AI provided rapid solutions for Python syntax, I found it often suggested generic Windows commands. I had to strictly filter its output to ensure compatibility with ROS Noetic's Python 3.8 environment, demonstrating that engineering judgment remains essential when using AI tools.*

### (c) How to Improve Accuracy? *(2 marks)*

*Low-Light Enhancement: Since car cams often operate at night or in tunnels, adding an image pre-processing layer (like Contrast Limited Adaptive Histogram Equalization) would help YOLO detect vehicles better in low-light conditions.

Lane-Specific ROI: By defining a "Region of Interest" (ROI) to focus only on the road lanes rather than the sky or sidewalks, we can reduce false positives from parked cars and improve the precision of detecting moving vehicles in front.

### (d) Real-World Challenges *(2 marks)*

*Vibration and Motion Blur: In a real moving car, road bumps and high speeds cause camera vibration. This blur can make it hard for the model to maintain a steady "lock" on vehicles, leading to flickering bounding boxes.

Lighting Conditions: Shadows and glare in urban environments can lower confidence scores. Implementing dynamic image pre-processing would be necessary for reliable 24/7 operation.*

import torch
print("--- Starting Test ---")
print("Loading YOLOv5s from Torch Hub...")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, trust_repo=True)
print("--- Success! Model is ready ---")

import sys
import os

# Fix path issue: Ensure ROS can find locally installed Python packages
user_site_packages = os.path.expanduser('~/.local/lib/python3.8/site-packages')
if user_site_packages not in sys.path:
    sys.path.insert(0, user_site_packages)

import rospy
import cv2
import torch
import numpy as np
from sensor_msgs.msg import CompressedImage

class YOLOv5Detector:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('yolov5_detector_node')
        
        # Load YOLOv5s model from Torch Hub
        rospy.loginfo("Loading YOLOv5s model...")
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        
        # Filter for car, bus, and truck classes only
        self.model.classes = [2, 5, 7] 
        
        # Subscribe to compressed image topic
        self.subscriber = rospy.Subscriber("/hikcamera/image_2/compressed", CompressedImage, self.callback)
        rospy.loginfo("YOLOv5 Detector is Online!")

    def callback(self, ros_data):
        # Decode compressed image to OpenCV format
        np_arr = np.frombuffer(ros_data.data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Perform AI inference
        results = self.model(img)

        # Render bounding boxes onto the image
        result_img = np.squeeze(results.render())

        # Display result in a window
        cv2.imshow("AAE4011 YOLOv5 Detection", result_img)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rospy.signal_shutdown("User quit")

if __name__ == '__main__':
    try:
        detector = YOLOv5Detector()
        rospy.spin() # Keep node running
    except Exception as e:
        print(e)
    cv2.destroyAllWindows()
    

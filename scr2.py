from datetime import datetime
import cv2
import sys

import Stitch

camera_list = ["/dev/v4l/by-id/usb-046d_Logitech_BRIO_7A5136C9-video-index0",
               "/dev/v4l/by-id/usb-046d_Logitech_BRIO_824DE5A3-video-index0",
               "/dev/v4l/by-id/usb-046d_Logitech_BRIO_D08617B3-video-index0",
               "/dev/v4l/by-id/usb-046d_Logitech_BRIO_E64237B1-video-index0"]


cam1 = cv2.VideoCapture(camera_list[0])
cam2 = cv2.VideoCapture(camera_list[1])
cam3 = cv2.VideoCapture(camera_list[2])
cam4 = cv2.VideoCapture(camera_list[3])

_, img1 = cam1.read()
_, img2 = cam2.read()
_, img3 = cam3.read()
_, img4 = cam4.read()

Stitch.stitch(img1,img2,img3,img4, filename=datetime.now().strftime("%H%M%S.jpg"))
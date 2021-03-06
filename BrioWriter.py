from datetime import datetime
import cv2
import numpy as np


class BrioWriter():

    def __init__(self):
        self.camera_list = ["/dev/v4l/by-id/usb-046d_Logitech_BRIO_19A4D2EC-video-index0",
                            "/dev/v4l/by-id/usb-046d_Logitech_BRIO_D08617B3-video-index0",
                            "/dev/v4l/by-id/usb-046d_Logitech_BRIO_E64237B1-video-index0",
                            "/dev/v4l/by-id/usb-046d_Logitech_BRIO_98FB31C0-video-index0"]

        self.cam = cv2.VideoCapture()
    
    def stable_cap(self, cam):
        x = 0
        img = None
        while 1:
            _, img = cam.read()
            x+=1
            if x>10:
                break
        return img

    def stitch(self, img1, img2, img3, img4):
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]

        h3, w3 = img3.shape[:2]
        h4, w4 = img4.shape[:2]

        r1 = np.zeros((max(h1, h2), w1 + w2, 3), dtype=np.uint8)
        r1[:, :] = (255, 255, 255)

        r2 = np.zeros((max(h3, h4), w3 + w4, 3), dtype=np.uint8)
        r2[:, :] = (255, 255, 255)

        r1[:h1, :w1, :3] = img1
        r1[:h2, w1:w1 + w2, :3] = img2

        r2[:h3, :w3, :3] = img3
        r2[:h4, w3:w3 + w4, :3] = img4

        h1, w1 = r1.shape[:2]
        h2, w2 = r2.shape[:2]

        res = np.zeros((h1 + h2, max(w1, w2), 3), dtype=np.uint8)
        res[:, :] = (255, 255, 255)

        res[:h1, :w1, :3] = r1
        res[h1:h1 + h2, :w2, :3] = r2

        return res

    def write_images(self):
        self.cam.open(self.camera_list[0], cv2.CAP_V4L2)
        self.cam.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
        img1 = self.stable_cap(self.cam)


        self.cam.open(self.camera_list[1], cv2.CAP_V4L2)
        self.cam.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
        img2 = self.stable_cap(self.cam)


        self.cam.open(self.camera_list[2], cv2.CAP_V4L2)
        self.cam.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
        img3 = self.stable_cap(self.cam)

        self.cam.open(self.camera_list[3], cv2.CAP_V4L2)
        self.cam.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

        img4 = self.stable_cap(self.cam)

        res = self.stitch(img1, img2, img3, img4)

        try:
            print(res.shape)
            file_name = datetime.now().strftime("%Y%m%d%H%M%S.jpg")
            cv2.imwrite("./images/"+file_name, res)
            print("./images/"+file_name, "File written successfully")
            return file_name + "written successfully"
        except Exception as e:
            print(e)
            print("File Not written")
            return "Exception:" + e

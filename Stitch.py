#!/usr/bin/env python

"""Stitch.py: Combine images."""

__author__ = "Rajesh Pachaikani"
__version__ = "0.0.1"
__email__ = "rajesh@makeintow.in"

import glob
import cv2
import numpy as np

def get_available_cameras():
    cam_list = glob.glob("/dev/video*")
    return cam_list


def stitch(img1, img2, img3, img4, filename: str):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    h3, w3 = img3.shape[:2]
    h4, w4 = img4.shape[:2]

    r1 = np.zeros((max(h1, h2), w1+w2, 3), dtype=np.uint8)
    r1[:, :] = (255, 255, 255)

    r2 = np.zeros((max(h3, h4), w3+w4, 3), dtype=np.uint8)
    r2[:, :] = (255, 255, 255)

    r1[:h1, :w1, :3] = img1
    r1[:h2, w1:w1+w2, :3] = img2

    r2[:h3, :w3, :3] = img3
    r2[:h4, w3:w3+w4, :3] = img4

    h1, w1 = r1.shape[:2]
    h2, w2 = r2.shape[:2]

    res = np.zeros((h1+h2, max(w1, w2), 3), dtype=np.uint8)
    res[:, :] = (255, 255, 255)

    res[:h1, :w1, :3] = r1
    res[h1:h1+h2, :w2, :3] = r2

    try:
        print(res.shape)
        cv2.imwrite(filename, res)
        print(str(filename),"File written successfully")
    except Exception as e:
        print(e)
        print("File Not written")

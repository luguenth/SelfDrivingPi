from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time

def get_filtered_contours(img, min, max, thresh):
    return filter_contours(
        get_contours(img, thresh),
        min,
        max)


def filter_contours(contours, min, max):
    Areacontours = list()
    for contour in contours:
        area = cv2.contourArea(contour,1)*-1
        if (area > min and area < max):
            Areacontours.append(contour)
    return Areacontours

def get_contours(img, thresh, mode = 1):
    #imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img, thresh, 255, mode)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def nothing(x):
    pass

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# initialize the camera and grab a reference to the raw camera capture
res_x = 320
res = (res_x, int(res_x*0.75))
camera = PiCamera()
camera.resolution = res
camera.framerate = 30
camera.shutter_speed=100000
rawCapture = PiRGBArray(camera, size=res)
thresh = 100

for image_cam in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Capture frame-by-frame
    frame = image_cam.array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #chg_perspective = rotateImage(frame, -90)
    #image = np.zeros((700, 700, 3), np.uint8)
    #src = np.array([[0,226],[558,226],[145,139],[400,139]],np.float32)
    #dst = np.array([[147-50,315],[407-50,315],[145-50,139],[400-50,139]],np.float32)

    #M = cv2.getPerspectiveTransform(src, dst)
    #warp = cv2.warpPerspective(frame.copy(), M, (480, 360))
    # Our operations on the frame come here
    contours = get_filtered_contours(frame, 0, 9999, thresh)
    cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    # Display the resulting frame
    frame = rotateImage(frame, -180)
    cv2.imshow('frame',frame)
    cv2.createTrackbar('thresh','frame',0,255,nothing)
    thresh = cv2.getTrackbarPos('thresh','frame')
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()

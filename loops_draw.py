from matplotlib import pyplot as plt
import cv2
from roipoly import RoiPoly
import numpy as np

cap = cv2.VideoCapture(0)
_, img = cap.read()
fh, fw, _ = img.shape
img = cv2.resize(img, (fw, fh))
area = img

while True:
    area = cv2.resize(area, (fw, fh))
    fig = plt.figure()
    plt.imshow(area, interpolation='nearest')
    plt.title('draw zone 1')
    plt.show(block=False)
    roi1 = RoiPoly(color='b', fig=fig)
    roi11 = roi1.get_roi_coordinates()
    # Show the image with the first ROI
    fig = plt.figure()
    plt.imshow(img, interpolation='nearest')
    roi1.display_roi()
    plt.title('Zone 1')
    plt.show()
    break

rois11 = np.array(roi11)
roiss11 = rois11.astype(int)
fig = plt.figure()
plt.imshow(area, interpolation='nearest')
roi1.display_roi()
file = open("loop6.txt", "w+")
rois11 = np.array(roi11)
np.savetxt('loop6.txt', rois11, fmt="%i")
file.close()

#############################################################################################################
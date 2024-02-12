import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, img = cap.read()
fh, fw, _ = img.shape
img = cv2.resize(img, (fw, fh))

file = open("loop1.txt", "r")
roiss11 = np.loadtxt("loop1.txt", dtype=int)
file.close()
mask1 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask1, [roiss11], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask1 = cv2.resize(mask1, (fw, fh), cv2.INTER_NEAREST)
#cv2.imshow('mask1', mask1)

file = open("loop2.txt", "r")
roiss22 = np.loadtxt("loop2.txt", dtype=int)
file.close()
mask2 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask2, [roiss22], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask2 = cv2.resize(mask2, (fw, fh), cv2.INTER_NEAREST)
#cv2.imshow('mask2', mask2)

file = open("loop3.txt", "r")
roiss33 = np.loadtxt("loop3.txt", dtype=int)
file.close()
mask3 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask3, [roiss33], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask3 = cv2.resize(mask3, (fw, fh), cv2.INTER_NEAREST)
#cv2.imshow('mask3', mask3)

file = open("loop4.txt", "r")
roiss44 = np.loadtxt("loop4.txt", dtype=int)
file.close()
mask4 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask4, [roiss44], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask4 = cv2.resize(mask4, (fw, fh), cv2.INTER_NEAREST)
#cv2.imshow('mask3', mask3)

file = open("loop5.txt", "r")
roiss55 = np.loadtxt("loop5.txt", dtype=int)
file.close()
mask5 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask5, [roiss55], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask5 = cv2.resize(mask5, (fw, fh), cv2.INTER_NEAREST)
#cv2.imshow('mask3', mask3)

file = open("loop6.txt", "r")
roiss66 = np.loadtxt("loop6.txt", dtype=int)
file.close()
mask6 = np.zeros((fh, fw), dtype=np.uint8)
cv2.drawContours(mask6, [roiss66], -1, (255, 255, 255), -1, cv2.LINE_AA)
mask6 = cv2.resize(mask6, (fw, fh), cv2.INTER_NEAREST)

#############################################################################################################
prototxt = 'MobileNetSSD_deploy.prototxt.txt'
model = 'MobileNetSSD_deploy.caffemodel'

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
net = cv2.dnn.readNetFromCaffe(prototxt, model)

while True:
    _, frame = cap.read()
    (fH, fW) = frame.shape[:2]
    frame = cv2.resize(frame, (fW, fH))
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    res3 = cv2.bitwise_and(frame, frame, mask=mask3)
    res4 = cv2.bitwise_and(frame, frame, mask=mask4)
    res5 = cv2.bitwise_and(frame, frame, mask=mask5)
    res6 = cv2.bitwise_and(frame, frame, mask=mask6)

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    blob1 = cv2.dnn.blobFromImage(cv2.resize(res1, (300, 300)), 0.007843, (300, 300), 127.5)
    blob2 = cv2.dnn.blobFromImage(cv2.resize(res2, (300, 300)), 0.007843, (300, 300), 127.5)
    blob3 = cv2.dnn.blobFromImage(cv2.resize(res3, (300, 300)), 0.007843, (300, 300), 127.5)
    blob4 = cv2.dnn.blobFromImage(cv2.resize(res4, (300, 300)), 0.007843, (300, 300), 127.5)
    blob5 = cv2.dnn.blobFromImage(cv2.resize(res5, (300, 300)), 0.007843, (300, 300), 127.5)
    blob6 = cv2.dnn.blobFromImage(cv2.resize(res6, (300, 300)), 0.007843, (300, 300), 127.5)


    net.setInput(blob1)
    detections1 = net.forward()
    if detections1 is not None:
        for i in np.arange(0, detections1.shape[2]):
            confidence = detections1[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx1 = int(detections1[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections1[0, 0, i, 3:7] * dims
            (startX1, startY1, endX1, endY1) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx1], confidence * 100)
            y = startY1 - 15 if startY1 - 15 > 15 else startY1 + 15
            if CLASSES[idx1] == "car" or CLASSES[idx1] == "bus" or CLASSES[idx1] == "motorbike" or CLASSES[idx1] == "bottle":
                cv2.putText(frame, label, (startX1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx1], 2)
                cv2.rectangle(frame, (startX1, startY1), (endX1, endY1), COLORS[idx1], 2)
                cv2.rectangle(res1, (startX1, startY1), (endX1, endY1), COLORS[idx1], 2)

    net.setInput(blob2)
    detections2 = net.forward()
    if detections2 is not None:
        for i in np.arange(0, detections2.shape[2]):
            confidence = detections2[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx2 = int(detections2[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections2[0, 0, i, 3:7] * dims
            (startX2, startY2, endX2, endY2) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx2], confidence * 100)
            y = startY2 - 15 if startY2 - 15 > 15 else startY2 + 15
            if CLASSES[idx2] == "car" or CLASSES[idx2] == "bus" or CLASSES[idx2] == "motorbike" or CLASSES[
                idx2] == "bottle":
                cv2.putText(frame, label, (startX2, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx2], 2)
                cv2.rectangle(frame, (startX2, startY2), (endX2, endY2), COLORS[idx2], 2)
                cv2.rectangle(res2, (startX2, startY2), (endX2, endY2), COLORS[idx2], 2)

    net.setInput(blob3)
    detections3 = net.forward()
    if detections3 is not None:
        for i in np.arange(0, detections3.shape[2]):
            confidence = detections3[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx3 = int(detections3[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections3[0, 0, i, 3:7] * dims
            (startX3, startY3, endX3, endY3) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx3], confidence * 100)
            y = startY3 - 15 if startY3 - 15 > 15 else startY3 + 15
            if CLASSES[idx3] == "car" or CLASSES[idx3] == "bus" or CLASSES[idx3] == "motorbike" or CLASSES[
                idx3] == "bottle":
                cv2.putText(frame, label, (startX3, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx3], 2)
                cv2.rectangle(frame, (startX3, startY3), (endX3, endY3), COLORS[idx3], 2)
                cv2.rectangle(res3, (startX3, startY3), (endX3, endY3), COLORS[idx3], 2)

    net.setInput(blob4)
    detections4 = net.forward()
    if detections4 is not None:
        for i in np.arange(0, detections4.shape[2]):
            confidence = detections4[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx4 = int(detections4[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections4[0, 0, i, 3:7] * dims
            (startX4, startY4, endX4, endY4) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx4], confidence * 100)
            y = startY4 - 15 if startY4 - 15 > 15 else startY4 + 15
            if CLASSES[idx4] == "car" or CLASSES[idx4] == "bus" or CLASSES[idx4] == "motorbike" or CLASSES[
                idx4] == "bottle":
                cv2.putText(frame, label, (startX4, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx4], 2)
                cv2.rectangle(frame, (startX4, startY4), (endX4, endY4), COLORS[idx4], 2)
                cv2.rectangle(res3, (startX4, startY4), (endX4, endY4), COLORS[idx4], 2)

    net.setInput(blob5)
    detections5 = net.forward()
    if detections5 is not None:
        for i in np.arange(0, detections5.shape[2]):
            confidence = detections5[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx5 = int(detections5[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections5[0, 0, i, 3:7] * dims
            (startX5, startY5, endX5, endY5) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx5], confidence * 100)
            y = startY5 - 15 if startY5 - 15 > 15 else startY5 + 15
            if CLASSES[idx5] == "car" or CLASSES[idx5] == "bus" or CLASSES[idx5] == "motorbike" or CLASSES[
                idx5] == "bottle":
                cv2.putText(frame, label, (startX5, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx5], 2)
                cv2.rectangle(frame, (startX5, startY5), (endX5, endY5), COLORS[idx5], 2)
                cv2.rectangle(res5, (startX5, startY5), (endX5, endY5), COLORS[idx5], 2)

    net.setInput(blob6)
    detections6 = net.forward()
    if detections6 is not None:
        for i in np.arange(0, detections6.shape[2]):
            confidence = detections6[0, 0, i, 2]
            if confidence < 0.2:
                continue
            idx6 = int(detections6[0, 0, i, 1])
            dims = np.array([fW, fH, fW, fH])
            box = detections6[0, 0, i, 3:7] * dims
            (startX6, startY6, endX6, endY6) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx6], confidence * 100)
            y = startY6 - 15 if startY6 - 15 > 15 else startY6 + 15
            if CLASSES[idx6] == "car" or CLASSES[idx6] == "bus" or CLASSES[idx6] == "motorbike" or CLASSES[
                idx6] == "bottle":
                cv2.putText(frame, label, (startX6, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx6], 2)
                cv2.rectangle(frame, (startX6, startY6), (endX6, endY6), COLORS[idx6], 2)
                cv2.rectangle(res6, (startX6, startY6), (endX6, endY6), COLORS[idx6], 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Slot1", res1)
    cv2.imshow("Slot2", res2)
    cv2.imshow("Slot3", res3)
    cv2.imshow("Slot4", res4)
    cv2.imshow("Slot5", res5)
    cv2.imshow("Slot6", res6)


    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.stop()

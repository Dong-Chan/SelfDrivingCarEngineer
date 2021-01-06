import cv2
import time

import sys

# Prepare the hog(Histogram of Oriented Gradients) detector to detect pedestrians
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_pedestrians_hog(file, stride, scale, hitThreshold, finalThreshold):
    start = time.time()
    original = cv2.imread(file)
    hog_image = original.copy()

    (boxes, weights) = hog.detectMultiScale(hog_image, winStride=(stride, stride), padding=(0,0), scale=scale, hitThreshold=hitThreshold, finalThreshold=finalThreshold)

    # Adds info
    for idx, (x, y, w, h) in enumerate(boxes):
        cv2.putText(hog_image, '%.2f' % weights[idx], (x, y + h - 5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
        cv2.rectangle(hog_image, (x, y), (x + w, y + h), (255, 255, 255), 2)

    parameters = str(stride) + "_" + str(scale) + "_H_" + str(hitThreshold) + "_" + str(finalThreshold) + "_"
    cv2.imwrite("out_hog/hog_" + parameters + file, hog_image)
    end = time.time()
    print(stride, scale, "Time: ", end - start, "Thresholds", hitThreshold, finalThreshold, "Boxes", len(boxes))

# Shows some combinations, the precision and the computation time
detect_pedestrians_hog("ped.jpg", 2, 1.05, 0, 1)
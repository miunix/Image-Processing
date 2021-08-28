import cv2
import math
import numpy as np
import time
import os
import imutils

from constants import *
from itertools import chain

LABELING = open(YOLOV3_LABELS_PATH).read().strip().split('\n')

np.random.seed(42)
COLOURS = np.random.randint(0, 255, size=(len(LABELING), 3), dtype='uint8')

print('Loading YOLO from disk.')

neural_net = cv2.dnn.readNetFromDarknet(YOLOV3_CFG_PATH, YOLOV3_WEIGHTS_PATH)
layernames = neural_net.getLayerNames()
layernames = [layernames[i[0] - 1]for i in neural_net.getUnconnectedOutLayers()]

vs = cv2.VideoCapture(VIDEO_PATH)
writing = None
(WT, HT) = (None, None)

try:
    if(imutils.is_cv2()):
        prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT
    else:
        prop = cv2.CAP_PROP_FRAME_COUNT
    total = int(vs.get(prop))
    print('The total number of frames identified is: ',total)
except Exception as e:
    print(e)
    total = -1

while True:
    (grabbed, framing) = vs.read()

    if not grabbed:
        break
    
    if WT is None or HT is None:
        HT, WT = (framing.shape[0], framing.shape[1])

    theblobb = cv2.dnn.blobFromImage(framing, 1 / 255.0, (416, 416), crop=False, swapRB=True)
    neural_net.setInput(theblobb)

    start_time = time.time()
    layer_outputs = neural_net.forward(layernames)
    end_time = time.time()
    
    boxes = []
    confidence = []
    classIDs = []
    lines = []
    box_centers = []

    for output in layer_outputs:
        for detection in output:
            
            scores = detection[5:]
            classID = np.argmax(scores)
            confi = scores[classID]
            
            if confi >  0.5 and classID == 0:
                box = detection[0:4] * np.array([WT, HT, WT, HT])
                (centerX, centerY, wdt, hgt) = box.astype('int')
                
                x = int(centerX - (wdt / 2))
                y = int(centerY - (hgt / 2))
                
                box_centers = [centerX, centerY]

                boxes.append([x, y, int(wdt), int(hgt)])
                confidence.append(float(confi))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidence, 0.5, 0.3)
    
    if len(idxs) > 0:
        atrisk = []
        count = 0
        
        for i in idxs.flatten():
            
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            centeriX = boxes[i][0] + (boxes[i][2] // 2)
            centeriY = boxes[i][1] + (boxes[i][3] // 2)

            color = [int(c) for c in COLOURS[classIDs[i]]]
            text = '{}: {:.4f}'.format(LABELING[classIDs[i]], confidence[i])

            idxs_copy = list(idxs.flatten())
            idxs_copy.remove(i)

            for j in np.array(idxs_copy):
                centerjX = boxes[j][0] + (boxes[j][2] // 2)
                centerjY = boxes[j][1] + (boxes[j][3] // 2)

                distance = math.sqrt(math.pow(centerjX - centeriX, 2) + math.pow(centerjY - centeriY, 2))

                if distance <= SAFE_DISTANCE:
                    cv2.line(framing, (boxes[i][0] + (boxes[i][2] // 2), boxes[i][1]  + (boxes[i][3] // 2)), (boxes[j][0] + (boxes[j][2] // 2), boxes[j][1] + (boxes[j][3] //2)), (0, 0, 255), 2)
                    atrisk.append([centerjX, centerjY])
                    atrisk.append([centeriX, centeriY])

            if centeriX in chain(*atrisk) and centeriY in chain(*atrisk):
                count += 1
                cv2.rectangle(framing, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                cv2.rectangle(framing, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(framing, text, (x, y - 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, color, 2)
            cv2.rectangle(framing, (50, 50), (500, 90), (0, 0, 0), -1)
            cv2.putText(framing, 'Number of individuals at risk: {}'.format(count), (70, 70), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 3)            


    if writing is None:

        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        writing = cv2.VideoWriter(OUTPUT_PATH, fourcc, 30,(framing.shape[1], framing.shape[0]),True)

        if total > 0:
            elap = (end_time - start_time)
            print('It took {:.4f} seconds to complete a single framing.'.format(elap))
            print('The total time to finish is estimated to be {:.4f} seconds.'.format(elap * total))

    writing.write(framing)

print('Finished processing the video.')
writing.release()
vs.release()                                
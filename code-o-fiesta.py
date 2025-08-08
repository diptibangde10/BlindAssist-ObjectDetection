import cv2  
import pyttsx3

text_speech= pyttsx3.init()  


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

classNames= []
classFile = "coco.names"
with open(classFile,'rt') as f: 
    classNames =f.read().rstrip('\n').split('\n')
    
 # Replace the scissors class with the cell phone class and others top
scissors_index = classNames.index('scissors')
classNames[scissors_index] = 'cell phone'

handbag_index = classNames.index('handbag')
classNames[handbag_index] = 'Bag'

snowboard_index = classNames.index('snowboard')
classNames[snowboard_index] = 'tie'

toilet_index = classNames.index('toilet')
classNames[toilet_index] = 'chair'

sink_index = classNames.index('sink')
classNames[sink_index] = 'moniter'

vase_index = classNames.index('vase')
classNames[vase_index] = 'keyboard'

# Save the updated classNames list to the classNames.txt file
with open('classNames.txt', 'wt') as f:
    f.write('\n'.join(classNames))

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)

net.setInputSize (320,320)
net.setInputScale(1.0/ 127.5) 
net.setInputMean ((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
     success,img=cap.read()
     classIds, confs, bbox = net.detect(img, confThreshold=0.5)
     print(classIds, bbox)
     
     if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img, classNames[classId-1].upper(), (box [0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255.0),2) 
          
            # Speak out the detected class name
            answer = classNames[classId-1]
            newVoiceRate =40
            text_speech.setProperty('rate',newVoiceRate)
            text_speech.say(answer)
            text_speech.runAndWait()
     cv2.imshow("output", img)
     cv2.waitKey(1)
import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(img)
    print(results.multi_hand_landmarks)                 #Gets the location of hand landmark
    if results.multi_hand_landmarks:
        for handLmks in results.multi_hand_landmarks:   #traverses through all the hand points in the result
            for id, lm in enumerate(handLmks.landmark):
                #lm.x, lm.y, lm.z gives the ratio of the image respect to pixel height and width
                h, w, c = img.shape
                #next line finds the pixel height and width of the image
                cx, cy = int(lm.x * w), int(lm.y *h)
                print(id, cx, cy)
                if id == 0:
                    cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)      #draws a circle at a specific landmark location
            mpDraw.draw_landmarks(img, handLmks, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()                                 #calculates the FPS
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (125, 155, 255), 3)            
    
    cv.imshow("WebCam", img)
    cv.waitKey(1)
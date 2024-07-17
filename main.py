import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
import mediapipe

cap = cv2.VideoCapture(0)  # This is initializing the camera
cap.set(3, 640)  # Here we are setting a fixed size (width to 640) in every case be it with a pc or webcam
cap.set(3, 480)  # Setting a fixed height

detector = HandDetector(maxHands=1)  # This helps detect the hand

timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, player]

while True:
    imgBG = cv2.imread("Resources/BG.png")  # This reads the BG.png image in our resources
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0), None, 0.585, 0.585)  # Resizing the image to fit our desired position 0n the
# imgBG
    imgScaled = imgScaled[:,240:640]  # Here we are cropping the image to fit exactly on the BG.
    # Find Hands
    hands, img = detector.findHands(imgScaled)

    if startGame:
        playerMove = None
        if stateResult is False: # This means that we haven't reached at the end of the game
            timer = time.time() - initialTime  # This gives us the time of which the game has been active since when started
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN,  6, (255, 0, 255), 4)  # Puts the timer on the imgBG on the specified position

            if timer > 3:
                stateResult = True
                timer = 0

                # Then check the hands
                if hands:
                    hand = hands[0]  # If the hands are detected, take the first hand that was detected
                    fingers = detector.fingersUp(hand)  # Shows which fingers are up with 1 representing up in the array otherwise 0

                    if fingers == [0, 0, 0, 0, 0]:  # Rock
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:  # Paper
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:  # Scissors
                        playerMove = 3

                    randomNumber = random.randint(1, 3)  # randint gives all inclusive ranges i.e, 1, 2, and 3
                    imgAI = cv2.imread(f"Resources/{randomNumber}.png", cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))  # layering imgAI on the imgBG on the specified position

                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1
                else:
                    print("Hand not found")

    imgBG[232:653, 795:1195] = imgScaled  # This is layering our webcam image on the background image since it is
# like a matrix

    if stateResult:  # This keeps the imgAI always displayed at the end of the game after having chosen
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))  # layering imgAI on the imgBG on the specified position

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),6)  # Puts the timer on the imgBG on the specified position
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),6)  # Puts the timer on the imgBG on the specified position

    #cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    #cv2.imshow("Scaled", imgScaled)
    key = cv2.waitKey(1)  # This is the delay
    if key == ord("s"):  # Game starts when the S key is clicked
        startGame = True
        initialTime = time.time()  # This gives us the time at which the s key was clicked (i.e, the time the game was started)
        stateResult = False
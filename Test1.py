# installing important libraries
#from sre_constants import SUCCESS
import cv2
from cvzone.HandTrackingModule import HandDetector
import sys
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import pointer, cast
from comtypes import CLSCTX_ALL
import mediapipe as mp


# Setting frames for webcamq
w_cam, h_cam = 640, 480  # frame dimensions
#############################

cap = cv2.VideoCapture(0)  # captures video from inbuilt(0) camera
cap.set(3, w_cam)
cap.set(4, h_cam)
handt = HandDetector(detectionCon=0.7, minTrackCon=0.6)

while True:
    success, img = cap.read()  # Reads camera using cap variable img saves the image
    hand, img = handt.findHands(img)
    # print(hand)
    # print(success)

    if len(hand) == 1:
        hand1 = hand[0]
        lmList1 = hand1['lmList']
        fingers1 = handt.fingersUp(hand1)
        # print(fingers1)

        pos_x = lmList1[0][0]
        pos_y = lmList1[0][1]


        x1, y1 = lmList1[1][0], lmList1[1][1]
        x1, y3 = lmList1[3][0], lmList1[3][1]
        x4, y4 = lmList1[4][0], lmList1[4][1]
        x5, y5 = lmList1[5][0], lmList1[5][1]
        x6, y6 = lmList1[6][0], lmList1[6][1]
        x7, y7 = lmList1[7][0], lmList1[7][1]
        x8, y8 = lmList1[8][0], lmList1[8][1]
        x9, y9 = lmList1[9][0], lmList1[9][1]
        x10, y10 = lmList1[10][0], lmList1[10][1]
        x11, y11 = lmList1[11][0], lmList1[11][1]
        x12, y12 = lmList1[12][0], lmList1[12][1]
        x14, y14 = lmList1[14][0], lmList1[14][1]
        x15, y15 = lmList1[15][0], lmList1[15][1]
        x16, y16 = lmList1[16][0], lmList1[16][1]
        x20, y20 = lmList1[20][0], lmList1[20][1]

        base= math.hypot((x9-x12), (y9-y9)) 
        perpendicular=math.hypot((x12-x12),(y9-y12)) 
        hypotenuse=math.hypot((x9-x12),(y9-y12))

        if hypotenuse!=0: 
            p_ratio_h=perpendicular/hypotenuse
            theta=(math.asin(p_ratio_h))*(180/math.pi)
        
        # cv2.putText(img, f'{(base)} Base', (30,30),
        #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        # cv2.putText(img,f'{(hypotenuse)} Hypo', (60,60),
        #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        # cv2.putText(img, f'{(perpendicular)} Perp', (75,75),
        #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        # cv2.putText(img, f'{(theta)} Theta', (90,90),
        #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)


        
        lent1 = math.hypot((x12-x8), (y12-y8)) #distance between 12 and 8
        lent2 = math.hypot((x11-x7), (y11-y7)) #distance between 11 and 7
        lent3 = math.hypot((x10-x6), (y10-y6)) #distance between 10 and 6

        lent4 = math.hypot((x8-x8), (y8-y5)) #distance between 8 and 1 for G 
        lent5 = math.hypot((x4-x8), (y4-y4)) #distance between 4 and 1 base
        lent6 = math.hypot((x8-x1), (y8-y1)) #distance between  and 1 Hypo

        # print(lent4)

        theta1=150
        if lent6!=0:
            b_ratio_h=lent5/lent6
            if b_ratio_h<=1:
                theta1=(math.acos(b_ratio_h))*(180/math.pi)


        x8midx12=(x8+x12)/2
        y8midy12=(y8+y12)/2

        lent6 = math.hypot((x8-x4), (y8-y4)) #distance between 4 and 8         

        # cv2.line(img,(x8midx12,50),(x8midx12,h_cam-50),(0,0,0),5)

        # print(lent1)
        # print(lent2)
        # print(lent3)

        # cv2.line(img,(x9,y9),(x12,y12),(0,0,0),5)
        # cv2.line(img,(x9,y9),(x12,y9),(0,0,0),5)
        # cv2.line(img,(x12,y12),(x12,y9),(0,0,0),5)

        # print(y4-y8)
        # print(y8)



# *********** All Down **********************************
        if (fingers1[0:] == [0, 0, 0, 0, 0]):

            # # ********** For Q ***********
            # if y4>y8 and y4>y12 and y4>y16 and y4>y20 and x4>x8 and x4>x20:
            #     cv2.putText(img, f'Q', ((pos_x-50), (pos_y+50)),
            #             cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For E ***********
            if y4>y8 and y4>y12 and y4>y16 and y4>y20:
                cv2.putText(img, f'E', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

                    # ********** For O ***********
            elif (lent6<25):
                cv2.putText(img, f'O', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                        

            # ********** For M ***********
            elif x15>x4 and x4<x14:
                cv2.putText(img, f'M', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)           

            # ********** For N ***********
            elif x10>x4 and x4>x14 and y10<y4:
                cv2.putText(img, f'N', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For S ***********
            elif ((y3<y7 and y3>y6) and (y4<y11 and y4>y10)):
                cv2.putText(img, f'S', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For T ***********
            elif x6>x4 and x10>x14:
                cv2.putText(img, f'T', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            
            

            



# *********** Index Up and Maybe Thumb **********************************
        elif (fingers1[0]==1 or fingers1[0]==0) and fingers1[1]==1 and fingers1[2:] == [0, 0, 0]:

            

            # ********** For X ***********
            if x8>x7 and x7>x6 and y8>y7:
                cv2.putText(img, f'X', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For L ***********
            elif (theta1==90 or theta1-30<=90) and fingers1[0]==1:
                cv2.putText(img, f'L', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For G ***********
            elif y4>y8 and y4>y12 and y4>y16 and y4>y20 and x4<x6:
                cv2.putText(img, f'G', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3) 

            # ********** For P ***********
            elif y10>y4 and y4>y6:
                cv2.putText(img, f'P', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For D ***********
            elif fingers1[0]==0:
                cv2.putText(img, f'D', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        

        # ********** For C ***********
        elif y4>y8 and y4>y12 and y4>y16 and y4>y20 and x4-30<=x20 and x4+30>=x20 and lent6>35:
                cv2.putText(img, f'C', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

# *********** Only Thumb Up **********************************
        elif fingers1[0]==1 and fingers1[1:] == [0, 0, 0, 0]:

            # ********** For A ***********
            cv2.putText(img, f'A', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

   

        # ********** For G ***********
        elif lent4<=5:
                cv2.putText(img, f'G', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        




# *********** Only Little Finger Up **********************************
        elif fingers1[4] == 1 and fingers1[0:4] == [0, 0, 0, 0]:

            # ********** For I ***********
            cv2.putText(img, f'I', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)



# *********** Thumb and Little Fingers Up **********************************
        elif fingers1[0] == 1 and fingers1[4] == 1 and fingers1[1:4] == [0, 0, 0]:

            # ********** For Y ***********
            cv2.putText(img, f'Y', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)



# *********** Index, Middle and Ring Fingers Up **********************************
        elif fingers1[0] == 0 and fingers1[1] == 1 and fingers1[2] == 1 and fingers1[3] == 1 and fingers1[4] == 0:

            # ********** For W ***********
            cv2.putText(img, f'W', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)



# *********** All Fingers Up except thumb**********************************
        elif fingers1[0] == 0 and fingers1[1:5] == [1,1,1,1]:
            # ********** For B ***********
            cv2.putText(img, f'B', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)



# *********** Middle, Ring, Little Fingers Up**********************************
        elif fingers1[0] == 0 and fingers1[1]==0 and fingers1[2:5] == [1,1,1]:
            # ********** For F ***********
            cv2.putText(img, f'F', ((pos_x-50), (pos_y+50)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)



# *********** Index and Middle Fingers Up **********************************
        elif fingers1[0] == 0 and fingers1[1] == 1 and fingers1[2] == 1 and fingers1[3] == 0 and fingers1[4] == 0:
            

            # ********** For K ***********
            if (x6>x4 and x4>x10):
                cv2.putText(img, f'K', ((pos_x-50), (pos_y+50)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                            
            # ********** For V ***********
            elif lent1 > 45:
                cv2.putText(img, f'V', ((pos_x-50), (pos_y+50)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For R ***********
            elif x8<x8midx12 and x12>x8midx12:
                cv2.putText(img, f'R', ((pos_x-50), (pos_y+50)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For H ***********
            elif theta<50:
                cv2.putText(img, f'H', ((pos_x-50), (pos_y+50)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

            # ********** For U ***********
            elif ((((perpendicular-5)<hypotenuse) or perpendicular==hypotenuse) and ((theta==90) or (theta>80))):
                cv2.putText(img, f'U', ((pos_x-50), (pos_y+50)),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
                        
            




    cv2.imshow("Raghav", img)

    if cv2.waitKey(1) == ord('q'):  # Press q to end the code
        print('exit')
        sys.exit(0)

    # cv2.waitKey(1)
# """[{'lmList': [[163, 381], [210, 364], [246, 330], [264, 295], [274, 266], [219, 272], [237, 230], [248, 204], [257, 181], [194, 264], [205, 215], [213, 182], [220, 155], [170, 266], [175, 218], [183, 187], [192, 161], [144, 274], [138, 236], [138, 209], [141, 183]], 'bbox': (138, 155, 136, 226), 'center': (206, 268), 'type': 'Right'}]"""

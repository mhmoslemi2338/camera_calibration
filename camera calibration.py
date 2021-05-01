import cv2
import numpy as np 




###### import the given images #######
images_bgr=[]
images=[]
for i in range(20):
    if(i<9): name='im0'+str(i+1)+'.jpg'
    else: name='im'+str(i+1)+'.jpg'
    tmp=cv2.imread(name,cv2.IMREAD_COLOR)
    images_bgr.append(tmp)
    tmp=cv2.cvtColor(tmp,cv2.COLOR_BGR2GRAY)
    images.append(tmp)
    
    
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)



board=(6,9) ### size of chest board

##### cordinate of a chessboar in world coordinates ####

objectp3d= np.zeros((1, board[0] * board[1], 3), np.float32)
enum=0
for j in range(board[1]):
    for i in range(board[0]):
        #print(row)
        objectp3d[0][enum]=(i,j,0)
        enum+=1


##### find coordinate of corners in each image in both world and image coordination #####
pnt3D=[]
pnt2D=[]
for i,row in enumerate(images):
    res , corner=cv2.findChessboardCorners(row,board,cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    pnt3D.append(objectp3d)
    corner2 = cv2.cornerSubPix(row, corner, (11,11),(-1,-1), criteria)
    pnt2D.append(corner2)
    
    

##### calibrate with img 1-20
_, camera_matrix, distortion_coef, _ , _ = cv2.calibrateCamera(pnt3D[0:10], pnt2D[0:10], images[19].shape[::-1], None, None)
file1 = open("result.txt","w")
file1.write(" Camera matrix:\n")
file1.write(str(camera_matrix))
file1.write("\n\n\n distortion_coefortion coefficient:\n")
file1.write(str(distortion_coef))
file1.close()
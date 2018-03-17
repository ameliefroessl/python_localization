import cv2 
import time


cap = cv2.VideoCapture(0)

#while (True):
ret, frame1 = cap.read()

time.sleep(1)

ret, frame2 = cap.read()



cv2.imshow("image1", frame1)
cv2.imshow("image2", frame2)


kp2, st, err = cv2.calcOpticalFlowPyrLK(frame1,frame2)

cv2.waitKey(0)



'''

	fast = cv2.FastFeatureDetector()

	# find and draw the keypoints
	#kp = fast.detect(frame,None)
	#img2 = cv2.drawKeypoints(frame, kp, color=(255,0,0))

	#cv2.imshow("frame", img2)

	# Print all default params
	print "Threshold: ", fast.getInt('threshold')
	print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
	#print "neighborhood: ", fast.getInt('type')
	#print "Total Keypoints with nonmaxSuppression: ", len(kp)

	

	# Disable nonmaxSuppression
	fast.setBool('nonmaxSuppression',0)
	kp = fast.detect(frame,None)

	print "Total Keypoints without nonmaxSuppression: ", len(kp)

	img3 = cv2.drawKeypoints(frame, kp, color=(255,0,0))

	cv2.imshow('fast_false.png',img3)
	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
'''
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
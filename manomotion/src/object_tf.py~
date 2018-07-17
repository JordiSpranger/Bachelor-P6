#!/usr/bin/env python
#from __future__ import print_function

#import roslib
import sys 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import cv, cv2, cv_bridge
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
import tf
import tf2_ros
import geometry_msgs.msg

###kinect##
def _init_(): 
	rospy.init_node("get_xyz")

	global pc_sub
	pc_sub = rospy.Subscriber("/camera/depth/points", PointCloud2 , pc_callback)

	global object_location
	object_location = [1, 0, 0]

	global rate	
	rate = rospy.Rate(60)

	global object_x_y_pixel
	object_x_y_pixel = [206, 243]

	global center_pixel
	center_pixel = [1, 1]
	

def br_object(x, y, z):
    	br = tf2_ros.TransformBroadcaster()
    	t = geometry_msgs.msg.TransformStamped()

    	t.header.stamp = rospy.Time.now()
    	t.header.frame_id = "camera_link"
    	t.child_frame_id = "object"
    	t.transform.translation.x = x
    	t.transform.translation.y = y
    	t.transform.translation.z = z
    	q = tf.transformations.quaternion_from_euler(0, 0, 0)
    	t.transform.rotation.x = 0
    	t.transform.rotation.y = 0
    	t.transform.rotation.z = 0
    	t.transform.rotation.w = 1

    	br.sendTransform(t)


def pc_callback(data):
	global center_pixel
	global object_location
    	gen = pc2.read_points(data, field_names='x y z', skip_nans=False, uvs=[(center_pixel[0], center_pixel[1])])
    	for i in gen:
		global object_location
        	object_location = i
		

    
  




###rgb###

class image_converter:

  def __init__(self):
#    self.image_pub = rospy.Publisher("image_topic_2",Image) #self is the placeholder for the object name

    self.bridge = CvBridge() #cvBridge is a method in the class
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

# Method for retrieving the center of the object
    def draw_contours(self,mask):
     cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     cnts= cnts[0]
     for c in cnts:
      
	# compute the center of the contour. Filter objects by area.
      M = cv2.moments(c)
      if M["m00"] != 0 and M["m00"] >800:
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	global center_pixel
	center_pixel = [cX, cY] #used to publish it in ros 
        print ("area of the blob",M['m00'])
	print(center_pixel, "center pixel")

	
	# draw the contour and center of the shape on the image
	cv2.drawContours(copy_cv_image, [c], -1, (0, 255, 0), 1)
	cv2.circle(copy_cv_image, (cX, cY), 2, (0, 0, 0), -1)
	cv2.putText(copy_cv_image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
      else:
	center_pixel = []

    (rows,cols,channels) = cv_image.shape
    copy_cv_image=cv_image.copy()


  #Colour segmentation
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    hsv_blue = cv2.cvtColor(cv_image.copy(), cv2.COLOR_BGR2HSV)  
    
    mask_OrangeBall =cv2.inRange(hsv, np.array([10,125,120]), np.array([19,255,255]))		
    mask_BlueCylinder=cv2.inRange(hsv_blue, np.array([99,90,90]), np.array([133,255,255]))
   
    #draw_contours(self, mask_OrangeBall)    #if you want to detect the orange then uncommend
    draw_contours(self,  mask_BlueCylinder)


  #Display images
    cv2.imshow("Initial image",cv_image)
    cv2.imshow("Result of colour segmentation",copy_cv_image)
    cv2.waitKey(1)

#    try:
       #transform cv2 image back to ros format to be published
#      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "8"))
#    except CvBridgeError as e:
#      print(e)
    print "object_location", object_location 
    br_object(object_location[0],object_location[1],object_location[2])
def main(args):
  ic = image_converter()



###Main Code###


_init_()


while __name__ == '__main__':

	try: 
		image_converter()
		main(sys.argv)
		print "object_location", object_location, center_pixel
		
		
		rospy.sleep(10)
		#rospy.spin()
	except KeyboardInterrupt:
		print("Shut Down.")
		cv2.destroyAllWindows()
		break
		
	
	
    		

    
    


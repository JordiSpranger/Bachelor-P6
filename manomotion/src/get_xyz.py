#!/usr/bin/env python
import rospy
import cv, cv2, cv_bridge
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
import tf
import tf2_ros
import geometry_msgs.msg

def _init_(): 
	rospy.init_node("get_xyz")

	global pc_sub
	pc_sub = rospy.Subscriber("/camera/depth/points", PointCloud2 , pc_callback)

	global object_location
	object_location = []

	global rate	
	rate = rospy.Rate(60)

	global object_x_y_pixel
	object_x_y_pixel = [1, 1]

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
	global object_location
    	gen = pc2.read_points(data, field_names='x y z', skip_nans=False, uvs=[(object_x_y_pixel[0], object_x_y_pixel[1])])
    	for i in gen:
        	opject_location = i
		
	


def main():
    br_object(object_location[0],object_location[1],object_location[2])
    rospy.sleep(0.05)
    #while not rospy.is_shutdown():
        #rate

############Definitions End########################

print("Now Starting the Service")

_init_()

while __name__ == "__main__":

	try:
		print object_location , " ", len(object_location)
		if len(object_location) == 3:
			print object_location
			main()
       
    	except KeyboardInterrupt:
        	raise
		
















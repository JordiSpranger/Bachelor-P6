#!/usr/bin/env python  
import rospy
import tf


if __name__ == '__main__':
    	rospy.init_node('tf_ra_listener')
	
    	listener = tf.TransformListener()



    	#listener.waitForTransform('/world', '/ra_ee_link', rospy.Time(), rospy.Duration(4.0))
    
        
     	now = rospy.Time.now()
	rospy.sleep(0.01)
     	listener.waitForTransform('/world', '/ra_ee_link', now, rospy.Duration(4.0))
	
     	(trans,rot) = listener.lookupTransform('/world', '/ra_ee_link', rospy.Time(0)) 
     	print trans, rot


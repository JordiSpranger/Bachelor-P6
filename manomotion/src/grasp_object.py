#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def init():
	
	global robot
	robot = moveit_commander.RobotCommander()

	global group
	group = moveit_commander.MoveGroupCommander("right_arm")

 
	
	global starting_pose
	starting_pose = geometry_msgs.msg.Pose()	
	starting_pose.position.x = 0.0
	starting_pose.position.y = 0.85
	starting_pose.position.z = 0.30
	starting_pose.orientation.w = 0.707
	starting_pose.orientation.x = 0.0
	starting_pose.orientation.y = 0.0
	starting_pose.orientation.z = 0.707

	execute_pose(starting_pose)
	rospy.sleep(5)

def pose_from_array(pose):
	pose_target = geometry_msgs.msg.Pose()	
	pose_target.position.x = pose[0]
	pose_target.position.y = pose[1]
	pose_target.position.z = pose[2]
	pose_target.orientation.w = pose[3]
	pose_target.orientation.x = pose[4]
	pose_target.orientation.y = pose[5]
	pose_target.orientation.z = pose[6]
	return pose_target

def execute_pose(pose):
	group.set_pose_target(pose)
	plan1 = group.plan()
	group.execute(plan1, wait = False)




global trans,rot
trans = []

if __name__ == '__main__':
    	rospy.init_node('turtle_tf_listener')
	init()
    	print("started")
    	listener = tf.TransformListener()

    	rate = rospy.Rate(10.0)
    	while not rospy.is_shutdown():
		if trans != []:
			break
        	try:
            		(trans,rot) = listener.lookupTransform('/world', '/object', rospy.Time(0))	
	    		print trans, rot
        	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            		continue

    
	
        	rate.sleep()
    
	
	pose = [trans[0]+0.0, trans[1]-0.1, trans[2]+0.1, 0.707, 0.0, 0.0, 0.707]
	#pose = [-0.3797980785369873, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0]
	print "pose", pose
	pose = pose_from_array(pose)
	
	execute_pose(pose)
	

















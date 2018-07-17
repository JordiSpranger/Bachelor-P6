#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def init():
	rospy.init_node('bachelor_arm', anonymous=True)
	

	global group
	group = moveit_commander.MoveGroupCommander("right_arm")


	
	global starting_pose
	starting_pose = geometry_msgs.msg.Pose()	
	starting_pose.position.x = 0.5
	starting_pose.position.y = 0.0
	starting_pose.position.z = 0.5
	starting_pose.orientation.x = 0
	starting_pose.orientation.y = 0
	starting_pose.orientation.z = 0
	starting_pose.orientation.w = 1
	
	#execute_pose(starting_pose)

	
	

def execute_pose(pose):
	group.set_pose_target(pose)
	plan1 = group.plan()
	group.execute(plan1, wait = False)
 

init()
starting_state = group.get_current_pose().pose


execute_pose(starting_pose)

	

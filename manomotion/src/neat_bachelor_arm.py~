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
	
	global robot
	robot = moveit_commander.RobotCommander()

	global group
	group = moveit_commander.MoveGroupCommander("right_arm")

    	global hand_subs
    	hand_subs = rospy.Subscriber("chatter", String, phone_callback)
    	rospy.sleep(1)
	
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

	global moving_threshold
	moving_threshold = [0, 0, 0]

	global check
	check = [2000, 2000, 2000]


def phone_callback(data):
	global phone_info
	phone_info = [float(i) for i in data.data.split('_')]
	
	


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
 

init()
starting_state = pose_from_array([0.0, 0.85, 0.30, 0.707, 0.0, 0.0, 0.707]) #group.get_current_pose().pose


while True: 


	moving_threshold = [check[0]-phone_info[2], check[1]-phone_info[3], check[2]-phone_info[4]]
	 	
 	print("moving_threshold", moving_threshold)
	rospy.sleep(0.3)
	if max(moving_threshold) > 0.05 or min(moving_threshold) < -0.05: #only executes if the hand moved beyond treshold
	
		starting_state.position.x = starting_pose.position.x + phone_info[2] * 2.5
		starting_state.position.y = starting_pose.position.y + phone_info[3] * 2.5
		starting_state.position.z =  phone_info[4] * 0.66
		starting_state.orientation.w = starting_pose.orientation.w 
		starting_state.orientation.x = starting_pose.orientation.x 
		starting_state.orientation.y = starting_pose.orientation.y 
		starting_state.orientation.z = starting_pose.orientation.z 
		check = [phone_info[2], phone_info[3], phone_info[4] ]

	



		print(starting_state)
		execute_pose(starting_state)
		print robot.get_group_names()

	
























	

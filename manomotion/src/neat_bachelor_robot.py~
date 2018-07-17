#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def init():
	rospy.init_node('bachelor_hand', anonymous=True)
	
	global robot
	robot = moveit_commander.RobotCommander()

	global group
	group = moveit_commander.MoveGroupCommander("right_hand")

    	global hand_subs
    	hand_subs = rospy.Subscriber("chatter", String, phone_callback)
    	rospy.sleep(1)
	
	global starting_pose
	starting_pose = 	       {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
	'rh_FFJ1': 0.4, 'rh_FFJ2': 0.4, 'rh_FFJ3': 0.4, 'rh_FFJ4': 0.0,
	'rh_MFJ1': 0.4, 'rh_MFJ2': 0.4, 'rh_MFJ3': 0.4, 'rh_MFJ4': 0.0, 
	'rh_RFJ1': 0.4, 'rh_RFJ2': 0.4, 'rh_RFJ3': 0.4, 'rh_RFJ4': 0.0,
	'rh_LFJ1': 0.4, 'rh_LFJ2': 0.4, 'rh_LFJ3': 0.4, 'rh_LFJ4': 0.0, 'rh_LFJ5': 0.0,
 	'rh_THJ1': 0.0, 'rh_THJ2': 0.0, 'rh_THJ3': 0.0, 'rh_THJ4': 0.0, 'rh_THJ5': 0.0}

	#execute_pose(starting_pose)


def phone_callback(data):
	global phone_info
	phone_info = [float(i) for i in data.data.split('_')]
	#phone = data.data.split('_')
	


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
        

def hand_joints(phone_info):
	if int(phone_info[1]) != -1:
		p = float(phone_info[1])
		t = (p/13) * 1.4
		l = p/13 * 0.4 - 0.2
		print(p,t)

		joints = {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
		'rh_FFJ1': t, 'rh_FFJ2': t, 'rh_FFJ3': 0.0, 'rh_FFJ4': 0.0,
		'rh_MFJ1': t, 'rh_MFJ2': t, 'rh_MFJ3': 0.0, 'rh_MFJ4': 0.0, 
		'rh_RFJ1': 0.0, 'rh_RFJ2': 0.0, 'rh_RFJ3': 0.0, 'rh_RFJ4': 0.0,
		'rh_LFJ1': 0.0, 'rh_LFJ2': 0.0, 'rh_LFJ3': 0.0, 'rh_LFJ4': 0.0, 'rh_LFJ5': 0.0,
	 	'rh_THJ1': 0.0, 'rh_THJ2': 0.0, 'rh_THJ3': 0.0, 'rh_THJ4': 0.0, 'rh_THJ5': 0.0}

		return joints
	else:  
		return starting_pose

def execute_hand(joints):
	group.set_joint_value_target(joints)
	plan1 = group.plan()
	group.execute(plan1, wait = False)






init()
starting_state = group.get_current_joint_values()


while True: 
	print phone_info
	goal = hand_joints(phone_info)
	execute_hand(goal)

#print phone_info
#goal = hand_joints(phone_info)
#execute_hand(starting_pose)






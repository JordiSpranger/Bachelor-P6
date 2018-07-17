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
	
	global phone_info
	phone_info = [0,0,0,0,0]
	
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

	global check #a variable to check if the new state of the hand is different to the old one  
	check = 0 

	global before #a variable to check if the new state of the hand is different to the old one  
	before = 20 

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
	if int(phone_info[1]) != -2: #change to -1 to activate this block of code
		p = float(phone_info[1])
		t = (p/13) * 1.0
		s_FFJ1 = (p/13) * 1.57
		s_FFJ2 = (p/13) * 1.57
		s_FFJ3 = (p/13) * 1.57
		s_FFJ4 = (p/13) * 0
		s_THJ4 = (p/13) * 1.21
		s_THJ5 = (p/13) * 0.169
		s_THJ1 = (p/13) * 0.52
		s_THJ2 = (p/13) * 0.60
		s_THJ3 = (p/13) * 0
		s_LFJ2 = (p/13) * 1.57
		s_LFJ3 = (p/13) * 1.57
		s_LFJ1 = (p/13) * 1.57 
		s_LFJ4 = (p/13) * 0
		s_LFJ5 = (p/13) * 0
		s_RFJ4 = (p/13) * 0
		s_RFJ1 = (p/13) * 1.57
		s_RFJ2 = (p/13) * 1.57
		s_RFJ3 = (p/13) * 1.57
		s_MFJ1 = (p/13) * 1.57
		s_MFJ3 = (p/13) * 1.57
		s_MFJ2 = (p/13) * 1.57
		s_MFJ4 = (p/13) * 0
		
		l = p/13 * 0.4 - 0.2
		print(p,t)

		joints = {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
		'rh_FFJ1': s_FFJ1, 'rh_FFJ2': s_FFJ2, 'rh_FFJ3': s_FFJ3, 'rh_FFJ4': s_FFJ4,
		'rh_MFJ1': s_MFJ1, 'rh_MFJ2': s_MFJ2, 'rh_MFJ3': s_MFJ3, 'rh_MFJ4': s_MFJ4, 
		'rh_RFJ1': s_RFJ1, 'rh_RFJ2': s_RFJ2, 'rh_RFJ3': s_RFJ3, 'rh_RFJ4': s_RFJ4,
		'rh_LFJ1': s_LFJ1, 'rh_LFJ2': s_LFJ2, 'rh_LFJ3': s_LFJ3, 'rh_LFJ4': s_LFJ4, 'rh_LFJ5': s_LFJ5,
	 	'rh_THJ1': s_THJ1, 'rh_THJ2': s_THJ2, 'rh_THJ3': s_THJ3, 'rh_THJ4': s_THJ4, 'rh_THJ5': s_THJ5}

		return joints

	if int(phone_info[1]) in [0, 1, 2, 3, 4]:
		p = 0
		t = (p/13) * 1.0
		s_FFJ1 = (p/13) * 1.57
		s_FFJ2 = (p/13) * 1.57
		s_FFJ3 = (p/13) * 1.57
		s_FFJ4 = (p/13) * 0
		s_THJ4 = (p/13) * 1.21
		s_THJ5 = (p/13) * 0.169
		s_THJ1 = (p/13) * 0.52
		s_THJ2 = (p/13) * 0.60
		s_THJ3 = (p/13) * 0
		s_LFJ2 = (p/13) * 1.57
		s_LFJ3 = (p/13) * 1.57
		s_LFJ1 = (p/13) * 1.57 
		s_LFJ4 = (p/13) * 0
		s_LFJ5 = (p/13) * 0
		s_RFJ4 = (p/13) * 0
		s_RFJ1 = (p/13) * 1.57
		s_RFJ2 = (p/13) * 1.57
		s_RFJ3 = (p/13) * 1.57
		s_MFJ1 = (p/13) * 1.57
		s_MFJ3 = (p/13) * 1.57
		s_MFJ2 = (p/13) * 1.57
		s_MFJ4 = (p/13) * 0
		
		l = p/13 * 0.4 - 0.2
		print(p,t)

		joints = {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
		'rh_FFJ1': s_FFJ1, 'rh_FFJ2': s_FFJ2, 'rh_FFJ3': s_FFJ3, 'rh_FFJ4': s_FFJ4,
		'rh_MFJ1': s_MFJ1, 'rh_MFJ2': s_MFJ2, 'rh_MFJ3': s_MFJ3, 'rh_MFJ4': s_MFJ4, 
		'rh_RFJ1': s_RFJ1, 'rh_RFJ2': s_RFJ2, 'rh_RFJ3': s_RFJ3, 'rh_RFJ4': s_RFJ4,
		'rh_LFJ1': s_LFJ1, 'rh_LFJ2': s_LFJ2, 'rh_LFJ3': s_LFJ3, 'rh_LFJ4': s_LFJ4, 'rh_LFJ5': s_LFJ5,
	 	'rh_THJ1': s_THJ1, 'rh_THJ2': s_THJ2, 'rh_THJ3': s_THJ3, 'rh_THJ4': s_THJ4, 'rh_THJ5': s_THJ5}
		check = 1
		return joints

	if int(phone_info[1]) in [5, 6, 7, 8, 9]:
		p = 7
		t = (p/13) * 1.0
		s_FFJ1 = (p/13) * 1.57
		s_FFJ2 = (p/13) * 1.57
		s_FFJ3 = (p/13) * 1.57
		s_FFJ4 = (p/13) * 0
		s_THJ4 = (p/13) * 0 #1.21
		s_THJ5 = (p/13) * 0 #0.169
		s_THJ1 = (p/13) * 0 #0.52
		s_THJ2 = (p/13) * 0 #0.60
		s_THJ3 = (p/13) * 0
		s_LFJ2 = (p/13) * 1.57
		s_LFJ3 = (p/13) * 1.57
		s_LFJ1 = (p/13) * 1.57 
		s_LFJ4 = (p/13) * 0
		s_LFJ5 = (p/13) * 0
		s_RFJ4 = (p/13) * 0
		s_RFJ1 = (p/13) * 1.57
		s_RFJ2 = (p/13) * 1.57
		s_RFJ3 = (p/13) * 1.57
		s_MFJ1 = (p/13) * 1.57
		s_MFJ3 = (p/13) * 1.57
		s_MFJ2 = (p/13) * 1.57
		s_MFJ4 = (p/13) * 0
		
		l = p/13 * 0.4 - 0.2
		print(p,t)

		joints = {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
		'rh_FFJ1': s_FFJ1, 'rh_FFJ2': s_FFJ2, 'rh_FFJ3': s_FFJ3, 'rh_FFJ4': s_FFJ4,
		'rh_MFJ1': s_MFJ1, 'rh_MFJ2': s_MFJ2, 'rh_MFJ3': s_MFJ3, 'rh_MFJ4': s_MFJ4, 
		'rh_RFJ1': s_RFJ1, 'rh_RFJ2': s_RFJ2, 'rh_RFJ3': s_RFJ3, 'rh_RFJ4': s_RFJ4,
		'rh_LFJ1': s_LFJ1, 'rh_LFJ2': s_LFJ2, 'rh_LFJ3': s_LFJ3, 'rh_LFJ4': s_LFJ4, 'rh_LFJ5': s_LFJ5,
	 	'rh_THJ1': s_THJ1, 'rh_THJ2': s_THJ2, 'rh_THJ3': s_THJ3, 'rh_THJ4': s_THJ4, 'rh_THJ5': s_THJ5}
		check = 2
		return joints

	if int(phone_info[1]) in [ 10, 11, 12, 13]:
		p = 13
		t = (p/13) * 1.0
		s_FFJ1 = (p/13) * 1.57
		s_FFJ2 = (p/13) * 1.57
		s_FFJ3 = (p/13) * 1.57
		s_FFJ4 = (p/13) * 0
		s_THJ4 = (p/13) * 1.20
		s_THJ5 = (p/13) * 0.165
		s_THJ1 = (p/13) * 0.44
		s_THJ2 = (p/13) * 0.58
		s_THJ3 = (p/13) * 0
		s_LFJ2 = (p/13) * 1.57
		s_LFJ3 = (p/13) * 1.57
		s_LFJ1 = (p/13) * 1.57 
		s_LFJ4 = (p/13) * 0
		s_LFJ5 = (p/13) * 0
		s_RFJ4 = (p/13) * 0
		s_RFJ1 = (p/13) * 1.57
		s_RFJ2 = (p/13) * 1.57
		s_RFJ3 = (p/13) * 1.57
		s_MFJ1 = (p/13) * 1.57
		s_MFJ3 = (p/13) * 1.57
		s_MFJ2 = (p/13) * 1.57
		s_MFJ4 = (p/13) * 0
		
		l = p/13 * 0.4 - 0.2
		print(p,t)

		joints = {'rh_WRJ1': 0.0, 'rh_WRJ2': 0.0, 
		'rh_FFJ1': s_FFJ1, 'rh_FFJ2': s_FFJ2, 'rh_FFJ3': s_FFJ3, 'rh_FFJ4': s_FFJ4,
		'rh_MFJ1': s_MFJ1, 'rh_MFJ2': s_MFJ2, 'rh_MFJ3': s_MFJ3, 'rh_MFJ4': s_MFJ4, 
		'rh_RFJ1': s_RFJ1, 'rh_RFJ2': s_RFJ2, 'rh_RFJ3': s_RFJ3, 'rh_RFJ4': s_RFJ4,
		'rh_LFJ1': s_LFJ1, 'rh_LFJ2': s_LFJ2, 'rh_LFJ3': s_LFJ3, 'rh_LFJ4': s_LFJ4, 'rh_LFJ5': s_LFJ5,
	 	'rh_THJ1': s_THJ1, 'rh_THJ2': s_THJ2, 'rh_THJ3': s_THJ3, 'rh_THJ4': s_THJ4, 'rh_THJ5': s_THJ5}
		check = 3
		return joints






	else:  
		return starting_pose


#Hand joints position 
#{'rh_FFJ1': 1.569540639339455, 'rh_FFJ2': 1.5714334844353877, 'rh_FFJ3': 1.5707240787095396, 'rh_FFJ4': 0.0001594941027143193, 'rh_THJ4': 1.21513795695272, 'rh_THJ5': 0.16993734665610383, 'rh_THJ1': 0.5200827788963318, 'rh_THJ2': 0.6099031144336458, 'rh_THJ3': -0.00012077800400778216, 'rh_LFJ2': 1.5705136825689943, 'rh_LFJ3': 1.570713268058773, 'rh_LFJ1': 1.570422729064279, 'rh_LFJ4': 0.0003035566923950128, 'rh_LFJ5': 2.4241720574025294e-05, 'rh_RFJ4': -0.00017526523283439843, 'rh_RFJ1': 1.5714935210706233, 'rh_RFJ2': 1.5704807587441314, 'rh_RFJ3': 1.5708021093566904, 'rh_MFJ1': 1.5710375040489817, 'rh_MFJ3': 1.5708225805226963, 'rh_MFJ2': 1.5706209683855192, 'rh_MFJ4': 0.00015025850269267949}

#{'rh_FFJ1': -0.0002652857054723512, 'rh_FFJ2': 0.0046041206325240225, 'rh_FFJ3': 0.0005307224555375356, 'rh_FFJ4': -0.0002392770545771583, 'rh_THJ4': -0.021311038299501206, 'rh_THJ5': 0.00017269703196198805, 'rh_THJ1': -0.00012177035847127371, 'rh_THJ2': -0.00015537146524025047, 'rh_THJ3': -0.00023957454155087987, 'rh_LFJ2': 0.004163483971506565, 'rh_LFJ3': 7.60686877141481e-05, 'rh_LFJ1': -0.018638447291349003, 'rh_LFJ4': 0.0006677605514466833, 'rh_LFJ5': 0.0003662920220248722, 'rh_RFJ4': 0.00025053406712771675, 'rh_RFJ1': 0.005180790812336689, 'rh_RFJ2': -0.001517246909821246, 'rh_RFJ3': 5.594431398403543e-05, 'rh_MFJ1': -0.00677157091833358, 'rh_MFJ3': 9.612080926668654e-05, 'rh_MFJ2': 0.00698386237141424, 'rh_MFJ4': -3.0561646647164764e-05}


def execute_hand(joints):
	group.set_joint_value_target(joints)
	plan1 = group.plan()
	group.execute(plan1, wait = True)






init()
starting_state = group.get_current_joint_values()


while True:
	rospy.sleep(0.1)
	if phone_info[1] in [0, 1, 2, 3, 4]:
		check = 1	
		
	if phone_info[1] in [5, 6, 7, 8, 9]:
		check = 2

	if phone_info[1] in [10, 11, 12, 13]:
		check = 3

	print check, before
	if check != before:
	
		print phone_info
		goal = hand_joints(phone_info)
		execute_hand(goal)
		before = check 

#print phone_info
#goal = hand_joints(phone_info)
#execute_hand(starting_pose)






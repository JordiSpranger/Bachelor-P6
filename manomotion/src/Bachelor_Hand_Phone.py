#!/usr/bin/env python

# Example use of handfinder for a 5 fingered hand. The serial number and hand parameters
# are read and it is detected whether the hand is left or right and if there are tactiles present.
# The correct prefix and parameters are then configured.

import sys
import rospy
from sr_robot_commander.sr_hand_commander import SrHandCommander
from sr_utilities.hand_finder import HandFinder
from std_msgs.msg import String
import time 
import math

#global a 
#global n 
 
a = 1
n = 2



def callback(data):
    
	global s
	s=data.data
	#rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
		    
	#s = s.split[1]	
	#print "s", s 
	#print "n", n
	#position_1 = {'rh_LFJ1': (n/13 * 2.00), 'rh_LFJ2': (n/13 * 2.00), 'rh_LFJ3': (n/13 * 13)}
	#bla = {s , n}
	#print "bla", bla
	#print "position_1" , position_1 
	#hand_commander.move_to_joint_value_target(position_1)

#def pose(x):
	#position_1 = {'rh_LFJ1': x/13*1.55, 'rh_LFJ2': x/13*1.55, 'rh_LFJ3': x/13*1.00}
	#pose = {'rh_MFJ4': (x*0.625 - 0.3125),'rh_MFJ3': (x*1.32) ,'rh_FFJ4': (x*(-0.038)) ,'rh_MFJ0': (x*0.7) ,'rh_MFJ0': (x*0.69) ,'rh_LFJ0': (x*1.01)  ,'rh_LFJ5': (x*0.0057)  ,'rh_THJ4': (x*1.038) ,'rh_THJ5': (x*0.25) ,'rh_THJ2': (x*(-0.0466)) ,'rh_THJ3': (x*1.55) ,'rh_LFJ3': (x*1.55) ,'rh_THJ1': (x*(-0.012)) ,'rh_LFJ4': (x*0.0090) ,'rh_THJ1': (x*(-0.012)) ,'rh_RFJ3': x*1.53 ,'rh_RFJ0': x*1.146  ,'rh_RFJ4': x*0.00619 ,'rh_FFJ3': x*1}

#	pose = {'rh_FFJ1': x*1.55}
#	return pose 
	

def listener():
    
	# In ROS, nodes are uniquely named. If two nodes with the same
	# name are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('chatter', String, callback)
	#print "this only loops"
	    
	# spin() simply keeps python from exiting until this node is stopped
	#rospy.spin()

while __name__ == '__main__':
	if a == 1: 
		global s
		s = "1_-1"
		#rospy.init_node("basic_hand_examples", anonymous=True)
		rospy.init_node('listener', anonymous=True)
		hand_finder = HandFinder()
		hand_parameters = hand_finder.get_hand_parameters()
		hand_serial = hand_parameters.mapping.keys()[0]
		hand_commander = SrHandCommander(hand_parameters=hand_parameters,hand_serial=hand_serial)
		hand_mapping = hand_parameters.mapping[hand_serial]
		joints = hand_finder.get_hand_joints()[hand_mapping]
		a = 2
		print("hallo")
	
	else:	
		if a == 2: 
			listener()
			#print "s below", s
			time.sleep(1)
			
		else: 
			listener()
			
			print "s below 2", s
			if str(type(s)) == "<type 'str'>":	 
				if len(s) > 3:
					print "s below split" , s.split('_')[1]
					s = s.split('_')[1]
					s = int(s)
					p = float(s)
					if s > -1:
						p = p/13 * 1.5   
						print "0.5 p", p 
						pose = {'rh_FFJ1': p, 'rh_MFJ1': p, 'rh_RFJ1': p, 'rh_LFJ1': p }
						print "pose", pose 
						hand_commander.move_to_joint_value_target(pose)	
				
						#print "done"
			time.sleep(0.01)
		a = 3
		
		



    
    




#position_1 = {'rh_LFJ1': n, 'rh_LFJ2': n, 'rh_LFJ3': n}
#hand_commander.move_to_joint_value_target(position_1)

#position_1 = {'rh_LFJ1': j, 'rh_LFJ2': j, 'rh_LFJ3': j}
#hand_commander.move_to_joint_value_target(position_1)

#while True:

	#position_1 = {'rh_LFJ1': 1.0, 'rh_LFJ2': 1.0, 'rh_LFJ3': 1.0}
	#hand_commander.move_to_joint_value_target(position_1)

	#position_1 = {'rh_LFJ1': 0.0, 'rh_LFJ2': 0.0, 'rh_LFJ3': 0.0}
	#hand_commander.move_to_joint_value_target(position_1)

	#position_2 = {'rh_RFJ1': 0.9, 'rh_RFJ2': 0.9, 'rh_RFJ3': 0.9}
	#hand_commander.move_to_joint_value_target(position_2)

	#position_2 = {'rh_RFJ1': 0.0, 'rh_RFJ2': 0.0, 'rh_RFJ3': 0.0}
	#hand_commander.move_to_joint_value_target(position_2)

	#position_3 = {'rh_MFJ1': 0.9, 'rh_MFJ2': 0.9, 'rh_MFJ3': 0.9}
	#hand_commander.move_to_joint_value_target(position_3)

	#position_3 = {'rh_MFJ1': 0.0, 'rh_MFJ2': 0.0, 'rh_MFJ3': 0.0}
	#hand_commander.move_to_joint_value_target(position_3)

	#position_4 = {'rh_FFJ1': 0.9, 'rh_FFJ2': 0.9, 'rh_FFJ3': 0.9}
	#hand_commander.move_to_joint_value_target(position_4)

	#position_4 = {'rh_FFJ1': 0.0, 'rh_FFJ2': 0.0, 'rh_FFJ3': 0.0}
	#hand_commander.move_to_joint_value_target(position_4)

	#position_5 = {'rh_THJ1': 0.9, 'rh_THJ2': 0.5, 'rh_THJ3': 0.2, 'rh_THJ4': 0.4, 'rh_THJ5': 0.0}
	#hand_commander.move_to_joint_value_target(position_5)

	#position_5 = {'rh_THJ1': 0.0, 'rh_THJ2': 0.0, 'rh_THJ3': -0.2, 'rh_THJ4': 0.0, 'rh_THJ5': 0.3}
	#hand_commander.move_to_joint_value_target(position_5)	





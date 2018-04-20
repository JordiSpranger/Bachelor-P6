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
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sr_robot_commander.sr_arm_commander import SrArmCommander
from sr_robot_commander.sr_arm_commander import *

#global a 
#global n 
 
a = 1
n = 2






def callback(data):
    
	global s
	s=data.data


def listener():
    
	# In ROS, nodes are uniquely named. If two nodes with the same
	# name are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('listener2', anonymous=True)
	rospy.Subscriber('chatter', String, callback)
	#print "this only loops"
	    
	# spin() simply keeps python from exiting until this node is stopped
	#rospy.spin()

while __name__ == '__main__':
	if a == 1: 
		global s
		s = "1_-1"
		#rospy.init_node("basic_hand_examples", anonymous=True)
		rospy.init_node('listener2', anonymous=True)
		arm_commander = SrArmCommander(set_ground=False)
		reference_frame = arm_commander.get_pose_reference_frame()
		#hand_finder = HandFinder()
		#hand_parameters = hand_finder.get_hand_parameters()
		#hand_serial = hand_parameters.mapping.keys()[0]
		#hand_commander = SrHandCommander(hand_parameters=hand_parameters,hand_serial=hand_serial)
		#hand_mapping = hand_parameters.mapping[hand_serial]
		#joints = hand_finder.get_hand_joints()[hand_mapping]
		print "this", #SrArmCommander.get_end_effector_pose_from_state()		
		a = 2
		print("Setup Done.")
	
	else:	
		if a == 2: 
			listener()
			#print "s below", s
			time.sleep(1)
			new_pose = [0.5, 0.5, 0.5, 0, 0, 0]
			arm_commander.move_to_pose_target(new_pose)
			
		else: 
			listener()
			
			#print "s below 2", s
			if str(type(s)) == "<type 'str'>":	 
				if len(s) > 4:
					#print "s below split" , s, s.split('_')
					
					#s = int(s)
					#p = float(s)
					if s > -1:
						s = s.split('_')
						x = s[2]
						y = s[3]
						z = s[4]
						print "x:", x, "y:", y, "z:", z
						if (KeyboardInterrupt):
							#new_pose = [x, y, z, x_quart, y_quart, z_quart, w_quat]   	#quaternions
							#new_pose = [x, y, z, x_rot, y_rot, z_rot] 			#euler
							
							new_pose = [0.5 + float(y), 0.5 + float(x), 1.0 - float(z), 0, 0, 0] 		#only x, y , z 
							arm_commander.move_to_pose_target(new_pose)
							time.sleep(1)

						#p = p/13 * 1.5   
						#print "0.5 p", p 
						#pose = {'rh_FFJ1': p, 'rh_MFJ1': p, 'rh_RFJ1': p, 'rh_LFJ1': p }
						#print "pose", pose 
						#hand_commander.move_to_joint_value_target(pose)
						# Planning to a cartesian co-ordinate goal
						#position_2 = [0.5, 0.3, 1.2]
						#print("Planning the move to the second position:\n" + str(position_2) + "\n")
						#arm_commander.plan_to_position_target(position_2)
						#print("Finished planning, moving the arm now.")
						#arm_commander.execute()	
				
						#print "done"
			time.sleep(0.1)
		a = 3
		

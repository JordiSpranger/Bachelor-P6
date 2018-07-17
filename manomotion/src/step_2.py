#!/usr/bin/env python


#this script 
#next script is teaching the DMP

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
import numpy 
from copy import deepcopy
import tf

def init():
	rospy.init_node('replay_arm', anonymous=True)
	
	global robot
	robot = moveit_commander.RobotCommander()

	global group
	group = moveit_commander.MoveGroupCommander("right_arm")

	global waypoints
	waypoints = []

	global dmp_info_velocities
	dmp_info_velocities = []

	global dmp_info_positions
	dmp_info_positions = []
	
	global dmp_info_accelerations
	dmp_info_accelerations = []

	global dmp_info_effort
	dmp_info_effort = []

	global dmp_info_time_seconds
	dmp_info_time_seconds = []

	global dmp_info_time_nano_seconds
	dmp_info_time_nano_seconds = []

	global starting_pose_euler
	starting_pose_euler = tf.transformations.quaternion_from_euler(0,0, 1.57)
	starting_pose_euler = [0.0, 0.0, 0.707, 0.707]


	global starting_pose
	starting_pose = geometry_msgs.msg.Pose()	
	starting_pose.position.x = 0.0
	starting_pose.position.y = 0.75
	starting_pose.position.z = 0.5
	
	starting_pose.orientation.x = starting_pose_euler[0]
	starting_pose.orientation.y = starting_pose_euler[1]
	starting_pose.orientation.z = starting_pose_euler[2]
	starting_pose.orientation.w = starting_pose_euler[3]

	execute_pose(starting_pose)

	
	


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
	plan2 = group.plan()
	group.execute(plan2, wait = False)

def traj_plan_captured(filename):
	
	data = numpy.load(filename) 

	waypoints.append(copy.deepcopy(starting_pose))
	
	for i in data: 
		next_pose = geometry_msgs.msg.Pose()	
		next_pose.position.x = starting_pose.position.x + i[2]
		next_pose.position.y = starting_pose.position.y + i[3]
		next_pose.position.z = starting_pose.position.z - i[4] + 0.4
		
		next_pose.orientation.x = starting_pose_euler[0]
		next_pose.orientation.y = starting_pose_euler[1]
		next_pose.orientation.z = starting_pose_euler[2]
		next_pose.orientation.w = starting_pose_euler[3]

		waypoints.append(copy.deepcopy(next_pose))


		

if __name__ == "__main__":

	init()
	rospy.sleep(2)
	group.set_pose_target(starting_pose)
	starting_state = group.get_current_pose().pose
	waypoints.append(group.get_current_pose().pose)

	traj_plan_captured('waypoints.npy')

	
	(plan1, fraction) = group.compute_cartesian_path(
		                     waypoints,   # waypoints to follow
		                     0.05,        # eef_step
		                     0.0)         # jump_threshold

	#print plan1 , "plan1"
	print "============ Waiting while RVIZ displays plan..."
	#rospy.sleep(5)

	print "plan1", type(plan1)
	for i in plan1.joint_trajectory.points:
		dmp_info_positions.append(i.positions)
		dmp_info_velocities.append(i.velocities)	
		dmp_info_accelerations.append(i.accelerations)
		dmp_info_effort.append(i.effort)
		dmp_info_time_seconds.append(i.time_from_start.secs)
		dmp_info_time_nano_seconds.append(i.time_from_start.nsecs)
	
	#saving the trajectory information for dmp"
	numpy.save('position', dmp_info_positions)
	numpy.save('velocities', dmp_info_velocities)
	numpy.save('accelerations', dmp_info_accelerations)
	numpy.save('time_from_start_seconds', dmp_info_time_seconds)
	numpy.save('effort', dmp_info_effort)
	numpy.save('time_from_start_secs', dmp_info_time_seconds)
	numpy.save('time_from_start_nsecs', dmp_info_time_nano_seconds)
	print "Success. Closing Now."

	print "Now Replaying Trajectory."

	group.execute(plan1, wait = False)
	














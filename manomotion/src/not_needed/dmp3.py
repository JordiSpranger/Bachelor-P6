#!/usr/bin/env python
import roslib; 
roslib.load_manifest('dmp')
import rospy 
import numpy as np
#from dmp import *
from dmp.srv import *
from dmp.msg import *
from moveit_msgs.msg import RobotState, PositionIKRequest
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def _init_():
	global dmp
	dmp = np.load('taught_dmp.npy')

	global resp
	resp = np.load('taught_dmp.npy')

 	makeSetActiveRequest(dmp.dmp_list)
	
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
	starting_pose.position.y = 0.5
	starting_pose.position.z = 0.5
	starting_pose.orientation.w = 1.0
	starting_pose.orientation.x = 0.0
	starting_pose.orientation.y = 0.0
	starting_pose.orientation.z = 0.0

	execute_pose(starting_pose)

def get_current_joint_state():
	return group.get_current_state()
	

def execute_pose(pose):
	group.set_pose_target(pose)
	plan1 = group.plan()
	group.execute(plan1, wait = False)
 
 #Set a DMP as active for planning
def makeSetActiveRequest(dmp_list):
     	try:
         	sad = rospy.ServiceProxy('set_active_dmp', SetActiveDMP)
         	sad(dmp_list)
     	except rospy.ServiceException, e:
         	print "Service call failed: %s"%e
 
 
 #Generate a plan from a DMP
def makePlanRequest(x_0, x_dot_0, t_0, goal, goal_thresh, 
                     seg_length, tau, dt, integrate_iter):
     	print "Starting DMP planning..."
     	rospy.wait_for_service('get_dmp_plan')
     	try:
         	gdp = rospy.ServiceProxy('get_dmp_plan', GetDMPPlan)
         	resp = gdp(x_0, x_dot_0, t_0, goal, goal_thresh, 
                    	seg_length, tau, dt, integrate_iter)
     	except rospy.ServiceException, e:
         	print "Service call failed: %s"%e
     	print "DMP planning done"   
             
     	return resp;

def ik_joints_arm():
	message = PositionIKRequest
	message.group_name = "right_arm"
	


#Set it as the active DMP

if __name__ == '__main__':
	
	_init_()
 
     	#Now, generate a plan
     	x_0 = [0.0, 0.0, 0.0]          #Plan starting at a different point than demo 
     	x_dot_0 = [0.0, 0.0, 0.0]   
     	t_0 = 0                
     	goal = [8.0, 7.0, 1.0]#Plan to a different goal than demo
     	goal_thresh = [0.1, 0.1, 0.1]
     	seg_length = -1          #Plan until convergence to goal
     	tau = 2 * resp.tau       #Desired plan should take twice as long as demo
     	dt = 1.0
     	integrate_iter = 5       #dt is rather large, so this is > 1  
     	plan = makePlanRequest(x_0, x_dot_0, t_0, goal, goal_thresh, 
                            seg_length, tau, dt, integrate_iter)

     	print plan, type(plan)

	print get_current_joint_state()










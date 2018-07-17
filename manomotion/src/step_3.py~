#!/usr/bin/env python
import roslib; 
roslib.load_manifest('dmp')
import rospy 
import numpy as np
#from dmp import *
from dmp.srv import *
from dmp.msg import *
import pickle

import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String

def global_vars():
	global waypoints_from_phone
	waypoints_from_phone = []

	global get_x_y_z
	get_x_y_z = []

	global group
	group = moveit_commander.MoveGroupCommander("right_arm")


	global starting_pose
	starting_pose = geometry_msgs.msg.Pose()	
	starting_pose.position.x = 0.0
	starting_pose.position.y = 0.5
	starting_pose.position.z = 0.5
	starting_pose.orientation.w = 0.0
	starting_pose.orientation.x = 0.707
	starting_pose.orientation.y = 0.0
	starting_pose.orientation.z = 0.707


#Learn a DMP from demonstration data
def makeLFDRequest(dims, traj, dt, K_gain, 
                    D_gain, num_bases):
     demotraj = DMPTraj()
         
     for i in range(len(traj)):
         pt = DMPPoint();
         pt.positions = traj[i]
         demotraj.points.append(pt)
         demotraj.times.append(dt*i)
             
     k_gains = [K_gain]*dims
     d_gains = [D_gain]*dims
         
     print "Starting LfD..."
     rospy.wait_for_service('learn_dmp_from_demo')
     try:
         lfd = rospy.ServiceProxy('learn_dmp_from_demo', LearnDMPFromDemo)
         resp = lfd(demotraj, k_gains, d_gains, num_bases)
     except rospy.ServiceException, e:
         print "Service call failed: %s"%e
     print "LfD done"    
             
     return resp;
 
 
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






def traj_plan_captured(filename):
	
	data = numpy.load(filename) 

	for i in data: 
		next_pose = geometry_msgs.msg.Pose()	
		next_pose.position.x = 0.0 + i[2]
		next_pose.position.y = 0.5 + i[3]
		next_pose.position.z = 0.5 + i[4]
		next_pose.orientation.w = 0.707
		next_pose.orientation.x = 0.0
		next_pose.orientation.y = 0.0
		next_pose.orientation.z = 0.707

		waypoints.append(copy.deepcopy(next_pose))

def position_vector(filename):
	
	data = numpy.load(filename) 

	for i in data: 
		next_pose = []	
		next_pose[0] = 0.0 + i[2]
		next_pose[1] = 0.5 + i[3]
		next_pose[2] = 0.5 + i[4]
		next_pose[3] = 0.707
		next_pose[4] = 0.0
		next_pose[5] = 0.0
		next_pose[6] = 0.707

		waypoints_from_phone.append(next_pose)

def getting_x_y_z():
	global get_x_y_z
	local = np.load('waypoints.npy')
	for i in local:
		local2 = [i[2],i[3],i[4], 0, 0, 0, 1]
		get_x_y_z.append(local2)
		print local2
	return get_x_y_z

def execute_pose(pose):
	group.set_pose_target(pose)
	plan1 = group.plan()
	group.execute(plan1, wait = False)



##Main Code##

if __name__ == '__main__':

	global_vars()
	rospy.init_node('dmp_tutorial_node')

	execute_pose(starting_pose) 
		
	#Create a DMP from a 3-D trajectory
	dims = 7                
	dt = 1.0                
	K = 100                 
	D = 2.0 * np.sqrt(K)      
	num_bases = 4          
	traj = getting_x_y_z()
	print traj
	resp = makeLFDRequest(dims, traj, dt, K, D, num_bases)
	resp
	#rospy.sleep(5)
	#np.save('taught_dmp', resp)
	#print type(resp)
	#print dir(resp)
	#Pickle saves an object (in this case resp)
	# open the file for writing
	#fileObject = open("taught_dmp",'wb') 
	# this writes the object a to the
	# file named 'testfile'
	#pickle.dump(resp , fileObject)   

	np.save('resp.dmp_list', resp.dmp_list)
	np.save('resp.tau', resp.tau)
	#dmp = np.load('dmp.npy')
	 



























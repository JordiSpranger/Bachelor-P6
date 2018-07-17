#!/usr/bin/env python

import numpy as np
import sys
import rospy
#import moveit_commander
#import moveit_msgs.msg
#import geometry_msgs.msg
from std_msgs.msg import String
import pygame


###########################Definitions################################

def init():
	rospy.init_node('bachelor_hand', anonymous=True)
	
	pygame.init()
	screen = pygame.display.set_mode((512,384))

    	global hand_subs
    	hand_subs = rospy.Subscriber("chatter", String, phone_callback)
    	rospy.sleep(1)
	
	global phone_recording
	phone_recording = []



	

def phone_callback(data):
	global phone_info
	phone_info = [float(i) for i in data.data.split('_')]
	#phone = data.data.split('_')
	

def wait_key_pressed():
	while True:
	    # get events and (somewhere in background) update list
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()

	    # get current list.
	    pressed = pygame.key.get_pressed()
	    if pressed[pygame.K_UP]:
		
		print("UP")
		break

def is_key_pressed():
	
	    # get events and (somewhere in background) update list
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()

	    # get current list.
	    pressed = pygame.key.get_pressed()

	    return(pressed[pygame.K_UP])
	    if pressed[pygame.K_UP]:
		print("UP")
				
		
	    
	    

###########################Code Execution################################
		
if __name__ == '__main__': 

	init()
	wait_key_pressed()
	rospy.sleep(1)
	print("start recording")

	print is_key_pressed(), "is Arrow-UP key pressed?"
	rospy.sleep(1)
	print is_key_pressed(), "is Arrow-UP key pressed?"
	rospy.sleep(1)

	#recording the phone_info#
	while is_key_pressed() == 0: 
		print(is_key_pressed())
		rospy.sleep(0.05)
		global phone_recording
		global phone_info
		phone_recording.append(phone_info)

	#save phone_recodring in a numpy format#
	np.save('waypoints', phone_recording)


	print("Done. Closing now.")



		









#!/usr/bin/env python

import pygame
import rospy   

pygame.init()
screen = pygame.display.set_mode((512,384))

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
	rospy.sleep(0.25)

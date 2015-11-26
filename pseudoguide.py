#!/usr/bin/python
# This is a pseudo-code outline of the code running the seeing-guide-khan
# Author: Thomas Schluszas <tms2874@vt.edu>

#imports
#input how far ahead you would like khan to go
#set up khan coordinate system and set goal in that coordinate system
#establish straight line path (should be along y-axis of internal grid)
#begin moving towards goal (at a set speed, is 1 ft/s good?)
#use quadrature encoder to keep track of position in grid
#if obstacle is detected (what is a safe distance, 18 inches?):
	#produce obstacle sound
	#mark location of khan where obstacle was detected
	#check for obstacles on either side, turn in other direction if 1 side has obstacles, else pick a random side
	#currently assuming for simplicity: obstacles are not huge or irregularly shaped and using only 90 degree turns is acceptable (due to time/sensor limitations)
	#follow wall of obstacle until we hit original path again (y-axis)
	#if we are farther than original detection point: produce failure sound and stop
	#if we are closer than original detection point: turn towards goal and continue along path
#produce sound when goal is reached
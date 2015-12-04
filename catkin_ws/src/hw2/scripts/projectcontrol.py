#!/usr/bin/python
#This Node is intended to make Khan move forward until it detects a wall, and then make it stop.
#Author: Thomas Schluszas <tms2874@vt.edu>

#imports
import rospy
from geometry_msgs import Twist
from ros_msgs import Range


def callback(rangereading):
	#if we detect anything
	if rangereading <= 0.5:
		#stop
		rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
		#quit program so we don't continue on
		quit()
 
 #main function
def move():
	#initialize node
	rospy.init_node('move', anonymous=True)
	#send a command to move it forward
	rostopic pub /cmd_vel geometry_msgs/Twist -- '[0.5, 0, 0]' '[0, 0, 0]'
	#subscribe to topic /range
	rospy.Subscriber('/range', Range, callback)
	#continunally re-loop and keep looking for /range signals
	rospy.spin()

 if __name__ == '__main__':
  try:
    move()
  except rospy.ROSInterruptException:
    pass
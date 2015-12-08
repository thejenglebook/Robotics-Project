#!/usr/bin/python
#This Node is intended to make Khan move forward until it detects a wall, and then make it stop.
#Author: Thomas Schluszas <tms2874@vt.edu>

#imports
import rospy
from geometry_msgs import Twist
from ros_msgs import Range
from sensor_msgs.msg import JointState

#initialize movement variable & velcommand as a Twist message
move = True
velcommand = Twist()


def callback(rangereading):
	#if we detect anything (/range reports in cm)
	if rangereading <= 50:
		#stop
		move = False
	else:
		#keep moving
		move = True
		
 
 #main function
def move():
	global pub
	#initialize node
	rospy.init_node('move', anonymous=True)
	#send a command to move it forward
	if move == True:
		velcommand.linear.x = 0.005
		#subscribe to topic /range
	else if move == False:
		#stop
		celcommand.linear.x = 0
	#publish velocity command
	pub.publish(velcommand)
	#read range value
	rospy.Subscriber('/range', Range, callback)
	#continunally re-loop and keep looking for /range signals
	rospy.spin()

 if __name__ == '__main__':
  try:
    move()
  except rospy.ROSInterruptException:
    pass
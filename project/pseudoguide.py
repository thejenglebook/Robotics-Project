#!/usr/bin/python
# This is a pseudo-code outline of the code running the seeing-guide-khan
# Author: Thomas Schluszas <tms2874@vt.edu>

#CURRENT ASSUMPTIONS: 
	#KHAN IS INITIALLY DIRECTLY FACING ITS INITIAL GOAL
	#OBSTACLES ARE NOT EXCEPTIONALLY LARGE OR IRREGULARALY SHAPED
	#OBSTACLES ARE NOT CONFIGURED IN SUCH A WAY THAT KHAN WILL TRAVEL PAST THE GOAL

#CURRENT PROBLEMS:
	#I DO NOT KNOW HOW TO TURN EXACTLY 90 DEGREES
	#IMPORTS NEED FILLING
	#TURN PSEUDO INTO ACTUAL CODE (LINES THAT HAVE !!! AT BEGINNING: QUADRATURE POSITIONING, SENSING, TURNING, PRODUCING SOUNDS)
	#NEED TO ADD DISTANCE TRAVELING FOR OUTSIDE CORNERS
	#POSSIBLY NEED TO WORK AROUND SOME OF THE SIMPLIFYING ASSUMPTIONS
	#MAYBE NEED TO ADD RANGES FOR POSITION REQUIREMENTS (E.G. +- 0.25 METERS?)

#imports
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from khan_msgs.msg import Quadrature
from rosgraph_msgs import Clock
from sensor_msgs.msg import Odometry

#will need randomizing import?
#will need quadrature/sensor reading imports

#keeps track of direction facing when turning left
def turnleft(xdirect, ydirect):
	!!! ROTATE LEFT
	if ydirect == 1 and xdirect == 0:
		ydirect = 0
		xdirect = -1
	else if ydirect == -1 and xdirect == 0:
		ydirect = 0
		xdirect = 1
	else if ydirect == 0 and xdirect == -1:
		ydirect = -1
		xdirect = 0
	else if ydirect == 0 and xdirect == 1:
		ydirect = 1
		xdirect = 0
	#returns direction values
	return (xdirect, ydirect)

#keeps track of direction when turning right
def turnright(xdirect, ydirect):
	!!! ROTATE RIGHT
	if ydirect == 1 and xdirect == 0:
		ydirect = 0
		xdirect = 1
	else if ydirect == -1 and xdirect == 0:
		ydirect = 0
		xdirect = -1
	else if ydirect == 0 and xdirect == -1:
		ydirect = 1
		xdirect = 0
	else if ydirect == 0 and xdirect == 1:
		ydirect = -1
		xdirect = 0
	#returns direction values
	return (xdirect, ydirect)


#essentially a wall-following function until khan has returned to original planned path
def avoidleft(xgoal, yobstacle, xdirect, ydirect, xpos, ypos, sensorbound, stop):
	#turn left
	xdirect, ydirect = turnleft(xdirect, ydirect)

	#ensure initial movement, and end of function when we return to path line
	turncount = 0
	while (turncount == 0) or (xpos != xgoal):
		#movement + encoder readings
		rostopic pub /cmd_vel geometry_msgs/Twist -- '[0.5, 0, 0]' '[0, 0, 0]'
		!!! ypos = ypos + ydirect * DELTA POSITION
		!!! xpos = xpos + xdirect * DELTA POSITION

		#sensor readings
		!!! sensor1dist = READING FROM LEFT SIDE
		!!! sensor2dist = READING FROM FRONT 
		!!! sensor3dist = READING FROM RIGHT SIDE

		#turn right when obstacle is no longer on the right
		if sensor3dist >= sensorbound:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			#turn right
			xdirect, ydirect = turnright(xdirect, ydirect)
			turncount = turncount + 1
			#continue on

		#turn left if running into an inner corner
		if sensor2dist <= sensorbound:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			#turn left
			xdirect, ydirect = turnleft(xdirect, ydirect)
			turncount = turncount + 1
			#continue on

	#checks for return to path line
	if xpos == xgoal:
		#failure conditions
		if (ypos > ygoal) or (ypos <= yobstacle):
			stop = True
		#success conditions
		else
		xdirect, ydirect = turnleft(xdirect, ydirect)
		
		#returns
		return(xdirect, ydirect, xpos, ypos, stop)

	#essentially a wall-following function until khan has returned to original planned path (same as avoidleft, but to the right!)
def avoidright(xgoal, yobstacle, xdirect, ydirect, xpos, ypos, sensorbound, stop):
	#turn right
	xdirect, ydirect = turnright(xdirect, ydirect)

	#ensure initial movement, and end of function when we return to path line
	turncount = 0
	while (turncount == 0) or (xpos != xgoal):
		#movement + encoder readings
		rostopic pub /cmd_vel geometry_msgs/Twist -- '[0.5, 0, 0]' '[0, 0, 0]'
		!!! ypos = ypos + ydirect * DELTA POSITION
		!!! xpos = xpos + xdirect * DELTA POSITION

		#sensor readings
		!!! sensor1dist = READING FROM LEFT SIDE
		!!! sensor2dist = READING FROM FRONT 
		!!! sensor3dist = READING FROM RIGHT SIDE

		#turn right when obstacle is no longer on the left
		if sensor3dist >= sensorbound:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			#turn left
			xdirect, ydirect = turnleft(xdirect, ydirect)
			turncount = turncount + 1
			#continue on

		#turn left if running into an inner corner
		if sensor2dist <= sensorbound:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			#turn right
			xdirect, ydirect = turnright(xdirect, ydirect)
			turncount = turncount + 1
			#continue on

	#checks for return to path line
	if xpos == xgoal:
		#failure conditions
		if (ypos > ygoal) or (ypos <= yobstacle):
			stop = True
		#success conditions
		else
		xdirect, ydirect = turnright(xdirect, ydirect)
		
		#returns
		return(xdirect, ydirect, xpos, ypos, stop)



#moves forward anc calls other functions in case of obstacle
def main():
	rospy.init_node('main', anonymous=True)
	#input how far ahead you would like khan to go
	goal = input('How many meters would you like KHAN to travel?')
	#set up khan coordinate system
	xpos = 0
	ypos = 0
	xgoal = 0
	ygoal = goal

	#variables that will keep track of direction-facing
	xdirect = 0 #not facing a side at beginning, will be -1 if facing left or 1 if facing right
	ydirect = 1 #front-facing at beginning, will be -1 if facing reverse, will be 0 if facing a side

	#other variables
	speed = 0.5 #arbitrary speed at 0.5 m/s
	sensorbound = 0.5 #arbitrary setting, sensor readings will be relevant at 0.5 meters
	stop = False #variable that allows for immediate stopping of program in case of failure

	#straight line path should be along y-axis of internal grid
	#begin moving towards goal (at a set speed, is .5 m/s good?)
	while (ypos != ygoal):
		rostopic pub /cmd_vel geometry_msgs/Twist -- '[0.5, 0, 0]' '[0, 0, 0]'
		#position is read from the encoder-reading node
		!!! ypos = ypos + ydirect * DELTA POSITION FROM ENCODER NODE, SUBSCRIBED
		!!! xpos = xpos + xdirect * DELTA POSITION

		#all sensor readings are subscribed from another node
		!!! sensor1dist = READING FROM LEFT SIDE
		!!! sensor2dist = READING FROM FRONT 
		!!! sensor3dist = READING FROM RIGHT SIDE 

		#goal is reached, stop and produce success sound + message
		if ypos == ygoal:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			!!! PRODUCE SUCCESS SOUND
			print('Goal has been reached.')
			quit()

		#object detection at 1 meter in front of khan 
		if sensor2dist <= sensorbound:
			#stop
			rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
			#mark spot where obstacle was detected
			yobstacle = ypos
			!!! PRODUCE OBSTACLE SOUND

			#turn to a random side
			!!! rand = RANDOMLY PICK 1 OR 2
			
			#avoid functions kick in until khan returns back to the original path (y-axis)
			if rand == 1:
				 xdirect, ydirect, xpos, ypos, stop = avoidleft(xgoal, yobstacle, xdirect, ydirect, xpos, ypos, sensorbound, stop)

			else if rand == 2:
				xdirect, ydirect, xpos, ypos, stop = avoidright(xgoal, yobstacle, xdirect, ydirect, xpos, ypos, sensorbound, stop)

				#ends program if avoid functions determine a failure
			if stop == True:
				!!! PRODUCE FAILURE SOUND
				print('Goal has not been reached.')
				quit()

if __name__ == '__main__':
  try:
    motorcommand()
  except rospy.ROSInterruptException:
    pass
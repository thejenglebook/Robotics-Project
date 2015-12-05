#!/usr/bin/python
# This is a ROS node designed to command the motors of KHAN and read the corresponding encoder data
# Author: Thomas Schluszas <tms2874@vt.edu>

# Imports
#commented out unecessary imports since we are not implementing encoder
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import String
#from khan_msgs.msg import Quadrature
#from rosgraph_msgs import Clock
#import quadrature
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
#from math import pi


#quad = quadrature.QuadratureEstimator(1000.0/3)
#frontleft
GPIO.setup("P9_12", GPIO.OUT)
PIO.setup("P9_11", GPIO.OUT)
#front right
GPIO.setup("P8_09", GPIO.OUT)
PIO.setup("P8_08", GPIO.OUT)
#leftencoder
#GPIO.setup("P9_23", GPIO.IN)
#GPIO.setup("P9_24", GPIO.IN)
#GPIO.add_event_detect("P9_23", GPIO.BOTH)
#GPIO.add_event_detect("P9_24", GPIO.BOTH)

#I AM PRINTING COMMANDS INSTEAD OF EXECUTING THEM, FOR DEMONSTRATION

#controls front left wheel
def frontleft(flcmd):
  #Top speed at 100 duty is 900 rad/s (unrealistic, but from the data sheet). Because I can't test speeds, I'll assume speed varies linearly with duty
  if abs(flcmd.velocity[0]) >= 900:
  	duty = 100
  else:
  	duty = 100 * abs(flcmd.velocity[0]) / 900
  PWM.start("P9_14", duty)
  if flcmd.velocity[0] > 0:
    #counterclockwise motion
    GPIO.output("P9_12", GPIO.HIGH)
    GPIO.ouptut("P9_11", GPIO.LOW)
  if flcmd.velocity[0] < 0:
    #clockwise motion
    GPIO.output("P9_12", GPIO.LOW)
    GPIO.output("P9_11", GPIO.HIGH)


#controls front left wheel
def frontright(frcmd):
  #Top speed at 100 duty is 900 rad/s (unrealistic, but from the data sheet). Because I can't test speeds, I'll assume speed varies linearly with duty
  if abs(frcmd.velocity[0]) >= 900:
  	duty = 100
  else:
  	duty = 100 * abs(frcmd.velocity[0]) / 900
  PWM.start("P8_13", duty)
  if frcmd.velocity[0] > 0:
    #counterclockwise motion
    GPIO.output("P8_09", GPIO.HIGH)
    GPIO.ouptut("P8_08", GPIO.LOW)
  if frcmd.velocity[0] < 0:
    #clockwise motion
    GPIO.output("P8_09", GPIO.LOW)
    GPIO.output("P8_08", GPIO.HIGH)



#FOLLOWING FUNCTION TAKES ENCODER DATA AND PUBLISHES JOINTSTATE, COMMENTED OUT BECAUSE I CANNOT GET ENCODER DATA WITHOUT FUNCTION ROBOT    

#def callbackleft(data):
    #Takes data from bag file and runs through update function
#    quad.update(data.state_a.data, data.state_b.data, data.header.stamp.to_sec())
#    pub = rospy.Publisher('joint_out', JointState)
    #assigning values to JointState
#    quadout = JointState()
#    quadout.header.stamp = quad._time
    #Assuming 1000/3 ticks per revolution
#    quadout.position = (3/(2*pi*1000))*quad._position
#    quadout.velocity = (3/(2*pi*1000))*quad._velocity
    #Final publish of JointState
#    rospy.loginfo(quadout)
#    pub.publish(quadout)

#FOLLOWING FUNCTION GENERATES QUADRATURE DATA FROM ENCODER READINGS, COMMENTED OUT BECAUSE I DON'T GET ENCODER READINGS

#def leftencoder(time):
	#gather encoder data
#	if GPIO.input("P9_23"):
#  		a = True
#  	else:
#  		a = False
#  	if GPIO.input("P9_24"):
#  		b = True
#  	else:
#  		b = False
  	#assigns encoder values to Quadrature Data Type
#  	leftenc = Quadrature()
#  	leftenc.state_a.data = a
#  	leftenc.state_b.data = b
  	#getting time
#  	t = time.secs + time.nsecs/(1000.0)
#  	leftenc.header.stamp.to_sec() = t
  	#publishing Quadrature data
#  	pub = rospy.Publisher('leftencoder_out', Quadrature)
#	rospy.loginfo(leftenc)
#    pub.publish(leftenc)


#subscribes to controller messages and calls functions that actually command wheels
def motorcommand():
    rospy.init_node('motorcommand', anonymous=True)
    rospy.Subscriber('/py_controller/front_left_wheel/cmd', JointState, frontleft)
 
# FOLLOWING PART OF THE FUNCTION IS SUBSCRIBED TO TIME AND CALLS ENCODER-BASED FUNCTIONS, COMMENTED OUT BECAUSE OF LACK OF ENCODER

#    rospy.Subscriber('leftencoder_out', Quadrature, callbackleft)

    #calls updater for left encoder
#    if GPIO.event_detected("P9_23") or GPIO.event_detected("P9_24"):
#  		rospy.Subscriber('/Clock', Clock, leftencoder)


    rospy.spin()

if __name__ == '__main__':
  try:
    motorcommand()
  except rospy.ROSInterruptException:
    pass

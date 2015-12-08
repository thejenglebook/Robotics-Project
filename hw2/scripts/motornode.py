#!/usr/bin/python
# This is a ROS node designed to command the motors of KHAN and read the corresponding encoder data
# Author: Thomas Schluszas <tms2874@vt.edu>

# Imports
#commented out unecessary imports since we are not implementing encoder
import rospy
from sensor_msgs.msg import JointState
#from std_msgs.msg import String
#from khan_msgs.msg import Quadrature
#from rosgraph_msgs import Clock
#import quadrature
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
#from math import pi


#quad = quadrature.QuadratureEstimator(1000.0/3)

#frontleft
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_11", GPIO.OUT)
#front right
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
#rear left
GPIO.setup("P9_13", GPIO.OUT)
GPIO.setup("P9_15", GPIO.OUT)
#rear right
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_11", GPIO.OUT)

#GPIO.setup("P9_23", GPIO.IN)
#GPIO.setup("P9_24", GPIO.IN)
#GPIO.add_event_detect("P9_23", GPIO.BOTH)
#GPIO.add_event_detect("P9_24", GPIO.BOTH)

#I AM PRINTING COMMANDS INSTEAD OF EXECUTING THEM, FOR DEMONSTRATION

#controls front left wheel
def frontleft(flcmd):
  rate=6.8461703882*abs(flcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if flcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P9_14", 50)
  if flcmd.velocity[0] > 0:
    #counterclockwise motion (forward)
    GPIO.output("P9_11", GPIO.HIGH)
    GPIO.output("P9_12", GPIO.LOW)
  if flcmd.velocity[0] < 0:
    #clockwise motion (backward)
    GPIO.output("P9_11", GPIO.LOW)
    GPIO.output("P9_12", GPIO.HIGH)


#controls front right wheel
def frontright(frcmd):
  rate=6.8461703882*abs(frcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if frcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P8_13", 50)
  if frcmd.velocity[0] > 0:
    #counterclockwise motion (backward)
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.LOW)
  if frcmd.velocity[0] < 0:
    #clockwise motion (forward)
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_9", GPIO.HIGH)

 #controls rear left wheel
def rearleft(rlcmd):
  rate=6.8461703882*abs(rlcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if rlcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P9_16", 50)
  if rlcmd.velocity[0] > 0:
    #counterclockwise motion (forward)
    GPIO.output("P9_13", GPIO.HIGH)
    GPIO.output("P9_15", GPIO.LOW)
  if rlcmd.velocity[0] < 0:
    #clockwise motion (backward)
    GPIO.output("P9_13", GPIO.LOW)
    GPIO.output("P9_15", GPIO.HIGH)

 #controls rear right wheel
def rearright(rrcmd):
  rate=6.8461703882*abs(rrcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if rrcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P8_19", 50)
  if rrcmd.velocity[0] > 0:
    #counterclockwise motion (backward)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_11", GPIO.LOW)
  if rrcmd.velocity[0] < 0:
    #clockwise motion (forward)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_11", GPIO.HIGH)  



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
    rospy.Subscriber('/py_controller/front_right_wheel/cmd', JointState, frontright)
    rospy.Subscriber('/py_controller/rear_left_wheel/cmd', JointState, rearleft)
    rospy.Subscriber('/py_controller/rear_right_wheel/cmd', JointState, rearright)
 
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

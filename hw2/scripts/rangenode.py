#!/usr/bin/python
#This ROS node takes readings from the range finder and sends out the appropriate signal
#Author: Thomas Schluszas <tms2874@vt.edu>

#imports
import rospy
from sensor_msgs.msg import Range
from std_msgs.msg import String
import Adafruit_BBIO.ADC as ADC
import math

#setting up pin
ADC.setup()

def callback():
	value = ADC.read("P9_39")
	outvoltage = 3.3 * value
	#minimum range
	if outvoltage > 2.75:
		rangevalue = 15
	elif outvoltage < .4:
		rangevalue = 150
	else:
		#exponential fit function, derived from data sheet
		rangevalue = 2000 * math.pow(outvoltage, -1.02)

	#assign values and publish
	pub = rospy.Publisher('/range', Range, queue_size=10)
	rangeout = Range()
	rangeout.min_range = 15
	rangeout.max_range = 150
	rangeout.range = rangevalue
	rospy.loginfo(rangeout)
	pub.publish(rangeout)
	

#main function reads voltage and publishes Range value
#ranges reported in cm
def rangefunc():
	rospy.init_node('rangefunc', anonymous=True)

	rospy.Timer(1.0, callback)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		rangefunc()
	except rospy.ROSInterruptException:
		pass

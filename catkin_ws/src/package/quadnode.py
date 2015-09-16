#!/usr/bin/env python
# node by Thomas Schluszas <tms2874@vt.edu>
import rospy
from std_msgs.msg import String
import quadrature

def quadmessager():
    rospy.init_node('quadmessager', anonymous=True)
    quad = QuadratureEstimator(Ticks)
    rospy.Subscriber('/encoder_in', Jointstate)
    quad.update(/encoder_in)
    rospy.Publisher('joint_out',Jointstate)

if __name__ == '__main__':
    try:
        quadmessager()
    except rospy.ROSInterruptException:
        pass

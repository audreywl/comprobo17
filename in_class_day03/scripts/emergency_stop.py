#!/usr/bin/env/ python

"""Basics of creating messages in ROS node"""

from geometry_msgs.msg import Twist
from neato_node.msg import Bump
from sensor_msgs.msg import LaserScan
import rospy



class EmergencyStop(object):
    def __init__(self):
        rospy.init_node('e_stop')
        rospy.Subscriber('/bump', Bump, self.stopper)
        rospy.Subscriber('/scan', LaserScan, self.scan)
        rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.r = rospy.Rate(10)
    def stopper(self,msg):
        print msg
    def scan(self,msg):
        print msg
    def run(self):
        while not rospy.is_shutdown():
            self.r.sleep()
        print "Node is finished!"

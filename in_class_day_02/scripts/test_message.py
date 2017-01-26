#!/usr/bin/env/ python

"""Basics of creating messages in ROS node"""

from geometry_msgs.msg import PointStamped
import rospy

rospy.init_node('my_first_node')
rospy.Publisher('/nifty_point', PointStamped, queue_size=10)

r = rospy.Rate(2)
while not rospy.is_shutdown():
    point_message = Point(x=1.0, y=2.0)
    header_message = Header(stamp=rospy.Time.now(), frame_id="odom")
    stamped_message = PointStamped(header=header_message, point=point_message)
    print point_message

    pub.publish(stamped_message)

    r.sleep()

print "Node is finished!"

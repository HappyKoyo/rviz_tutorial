#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

if __name__ == '__main__':
    rospy.init_node("Rviz1",anonymous=True)
    visual_pub = rospy.Publisher("visualization_marker",Marker)
    while not rospy.is_shutdown():
        print 'AA'
        marker = Marker()
        marker.header.frame_id = "/my_frame"
        marker.header.stamp = rospy.get_rostime()
        marker.ns = "basic_shapes"
        marker.id = 0
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.pose.position.x = 1.0
        marker.pose.position.y = 1.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.color.r = 1.0
        marker.color.a = 0.3
        marker.lifetime = rospy.Duration()
        visual_pub.publish(marker)
        rate = rospy.Rate(1)
        rate.sleep()
        

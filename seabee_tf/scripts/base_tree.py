#!/usr/bin/env python

import rospy
import tf
import nav_msgs.msg


def callback(data):
    br = tf.TransformBroadcaster()
    br.sendTransform((data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z),
                     (data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w),
                     data.header.stamp,
                     "base_link",
                     "world")


if __name__ == "__main__":
    rospy.init_node("base_link")
    rospy.Subscriber("/odom", nav_msgs.msg.Odometry, callback)
    rospy.spin()

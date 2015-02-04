#!/usr/bin/env python

import rospy
import nav_msgs.msg
import tf


if __name__ == '__main__':
    rospy.init_node("camera1_link")
    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/base_link', '/world', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        br.sendTransform((0, 0, 0),
                         (0, 0, 0, 0),
                         rospy.Time.now(),
                         "camera1_link",
                         "base_link")

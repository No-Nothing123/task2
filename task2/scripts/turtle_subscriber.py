#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def poseCallback(msg):
    rospy.loginfo("x : %0.5f,y : %0.5f",msg.x,msg.y)

def turtle_subscriber():
    rospy.init_node('pose_subscriber',anonymous=True)
    rospy.Subscriber("/turtle1/pose",Pose,poseCallback)
    rospy.spin()

if __name__ == '__main__':
    turtle_subscriber()

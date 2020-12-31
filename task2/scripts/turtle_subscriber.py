#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def poseCallback(msg):
    rospy.loginfo("x : %0.5f,y : %0.5f",msg.x,msg.y)

if __name__ == '__main__':
    rospy.init_node('turtle_subscriber',anonymous = True)
    sub = rospy.Subscriber("/turtle1/pose",Pose,poseCallback)
    rospy.spin()
    

	

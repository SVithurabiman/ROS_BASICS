#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo(msg)

def pose_callbackX(msg:Pose):
    rospy.loginfo(str(msg.x)+","+str(msg.y))


if __name__== '__main__':
    rospy.init_node("turtle_Pose_Subscriber")
    

    sub=rospy.Subscriber("/turtle1/pose",Pose, callback=pose_callbackX)
    rospy.loginfo("Helloooo from pose node")
    rospy.spin() #keep the program unitl node is alive. It is alive even if tutlesim is stopped
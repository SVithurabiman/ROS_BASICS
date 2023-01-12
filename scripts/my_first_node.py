#!/usr/bin/env python3
import rospy

if __name__== '__main__':

    rospy.init_node("test_node") #name of the node
    rospy.loginfo("Helloooo from test node")
    rate =rospy.Rate(10) #Hertz
    while not rospy.is_shutdown():
        rospy.logerr("HELLO")
        rate.sleep()  #control the speed of the loop



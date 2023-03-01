#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
if __name__== '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Helloooo from draw_circle node")
    #pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10) #topic_name #msgType  #buffer_size
    pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    rate =rospy.Rate(0.1) #Hertz
    while not rospy.is_shutdown():
        msg=Twist() #create object of class Twist
        msg.linear.x=0.5
        # msg.linear.y=3.0
        # msg.angular.z=0.5
        pub.publish(msg)
        rate.sleep()  #control the speed of the loop

#!/usr/bin/env python3
import rospy
import rosbag

if __name__== '__main__':
    rospy.init_node('read_bag_node')
    bag=rosbag.Bag("/home/vithurabiman/catkin_ws/src/my_robot_controller/bag/test.bag")

    for topic,msg,t in bag.read_messages(topics=["/sam", "/alice"]): #can add list of topic in topics=
        
        print(msg.data)
        # if topic== "/sam":
        #     print(msg.data)
        #     print(t) 
        # if topic== "/alice":
        #     print(msg.data)
        #     print(t) 


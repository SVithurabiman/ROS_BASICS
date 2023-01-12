# !/usr/bin/env Python3
import rospy
from std_msgs.msg import Int64
import os
import sys
import time
import smbus
import numpy as np

from imusensor.MPU9250 import MPU9250
from imusensor.filters import kalman

rospy.init_node("publish_node")
pub = rospy.publisher("/iroll", Int64, queue_size = 1)
pub2 = rospy.publisher("/iyaw", Int64, queue_size = 1)
pub2 = rospy.publisher("/ipitch", Int64, queue_size = 1)

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

imu.loadCalibDataFromFile("place_your_calib_file_here.json") #https://medium.com/@niru5/hands-on-with-rpi-and-mpu9250-part-3-232378fa6dbc

sensorfusion = kalman.Kalman()

imu.readSensor()
imu.computeOrientation()
sensorfusion.roll = imu.roll
sensorfusion.pitch = imu.pitch
sensorfusion.yaw = imu.yaw

count = 0
currTime = time.time()
while True:
	imu.readSensor()
	imu.computeOrientation()
	newTime = time.time()
	dt = newTime - currTime
	currTime = newTime

	sensorfusion.computeAndUpdateRollPitchYaw(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2], imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2],\
												imu.MagVals[0], imu.MagVals[1], imu.MagVals[2], dt)

	print("Kalmanroll:{0} KalmanPitch:{1} KalmanYaw:{2} ".format(sensorfusion.roll, sensorfusion.pitch, sensorfusion.yaw))
    pub.publish(sensorfusion.roll)
    pub2.publish(sensorfusion.pitch)
    pub3.publish(sensorfusion.yaw)
	rospy.sleep(0.01)

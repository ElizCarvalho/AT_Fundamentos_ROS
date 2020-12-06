#!/usr/bin/env python3

import rospy
import random

from std_msgs.msg import Float64

def talker():
	pub = rospy.Publisher('/at_fund/sensor', Float64, queue_size=10)
	rospy.init_node('ros1_talker_at')
	rate = rospy.Rate(1) #1hz

	while not rospy.is_shutdown():
		num = round(random.uniform(0.10, 270.10), 2)
		rospy.loginfo(num)
		pub.publish(num)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

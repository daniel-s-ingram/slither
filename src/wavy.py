#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from math import sin

rospy.init_node('wavy_test', anonymous=True)
pub = [rospy.Publisher('/slither/joint'+str(i-1)+str(i)+'_controller/command', Float64, queue_size=10) for i in xrange(1, 21)]

angle = Float64()
t = 0

while not rospy.is_shutdown():
	for i in xrange(20):
		angle.data = 0.25*sin(t) if i%2 == 0 else -0.25*sin(t)
		pub[i].publish(angle)

	t += 0.01
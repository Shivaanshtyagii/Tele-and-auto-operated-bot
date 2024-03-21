#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def velocity(data):
    move_vel = Twist()
    move_vel = data
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.loginfo(move_vel)
    pub.publish(move_vel)

def joystick():
    rospy.init_node('joystick_move', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, velocity)
    rospy.spin()

if __name__ == '__main__':
    try:
        joystick()
    except rospy.ROSInterruptException:
        pass
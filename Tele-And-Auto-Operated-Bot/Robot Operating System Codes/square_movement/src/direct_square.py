#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
import math

def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drt_sqr', anonymous=True)
    rate = rospy.Rate(10000) # 10hz

    move_square = Twist()

    # making a square:
    for i in range(4):
        move_square.linear.x = 1
        move_square.angular.z = 0
        straight_time = rospy.Time.now()
        while rospy.Time.now() < straight_time + rospy.Duration.from_sec(3):
                rospy.loginfo(move_square)
                pub.publish(move_square)
        
        move_square.angular.z = 0
        move_square.linear.x = 0
        rate.sleep()
                
        straight_time = rospy.Time.now()
        move_square.angular.z = math.pi/2
        move_square.linear.x = 0
        while rospy.Time.now() < straight_time + rospy.Duration.from_sec(1):
                rospy.loginfo(move_square)
                pub.publish(move_square)
    

            

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
import math

def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drt_rect', anonymous=True)

    move_rect = Twist()

    # making a rectangle:
    for i in range(2):
        move_rect.linear.x = 1
        move_rect.angular.z = 0
        pub.publish(move_rect)
        if(i==0):
            # pub.publish(move_rect)
            
            move_rect.linear.x = 0
            move_rect.angular.z = 0
            # rospy.sleep(3)
            pub.publish(move_rect)
        elif(i==1):
            # pub.publish(move_rect)
            rospy.sleep(5)
            move_rect.linear.x = 0
            move_rect.angular.z = 0
            # rospy.sleep(5)
            pub.publish(move_rect)

        move_rect.linear.x = 0
        move_rect.angular.z = math.pi/2
        pub.publish(move_rect)
        rospy.sleep(1)
         
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

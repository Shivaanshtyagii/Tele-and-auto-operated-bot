#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    x=1
    k1=0.5
    while not rospy.is_shutdown():
        msg=Twist()
        if(x==1): 
            msg.linear.x=1+k1
            msg.angular.z=0
            pub.publish(msg)
            rospy.sleep(1)
        elif(x==-1):
            msg.angular.z=1.57
            msg.linear.x=0
            pub.publish(msg)
            rospy.sleep(2) 
            k1*=-1 
        x*=-1
        


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



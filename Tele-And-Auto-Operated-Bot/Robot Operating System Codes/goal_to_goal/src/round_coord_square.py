#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

def position(data):
    curr_data = Pose()
    curr_data = data
    global curr_posx, curr_posy, curr_theta
    curr_posx = round(curr_data.x, 4)
    curr_posy = round(curr_data.y, 4)
    curr_theta = curr_data.theta

def distance(goal_pos):
    dis = math.sqrt(math.pow(goal_pos.x - curr_posx, 2) + math.pow(goal_pos.y - curr_posy, 2))
    return dis

def angle(goal_pos):
    rot_angle = math.atan2(goal_pos.y - curr_posy, goal_pos.x - curr_posx) - curr_theta 
    return rot_angle

def coordinate_square():
    rospy.init_node('coord_sqr', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, position)
    goal_pos = Pose()
    velocity = Twist()

    # moving to any specified position
    goal_pos.x = float(input("Set your x goal: "))
    goal_pos.y = float(input("Set your y goal: "))

    # velocity.linear.x = 0
    # velocity.angular.z = math.atan2(goal_pos.y - curr_posy, goal_pos.x - curr_posx) - curr_theta
    # pub.publish(velocity)
    # rospy.sleep(1)

    # move_angle = math.atan2(goal_pos.y - curr_posy, goal_pos.x - curr_posx) - curr_theta
    # if(move_angle >= 0):
    #     angular_velocity = 0.4
    # else:
    #     move_angle = math.radians(2*math.pi) - move_angle
    #     angular_velocity = -0.4

    # while angle(move_angle) >= 0.1:
    #     print(angle(move_angle))
    #     velocity.angular.z = angular_velocity
    #     velocity.linear.x = 0
    #     pub.publish(velocity)

    # turn_time = rospy.Time.now()
    # velocity.angular.z = math.atan2(goal_pos.y - curr_posy, goal_pos.x - curr_posx) - curr_theta
    # velocity.linear.x = 0
    # while rospy.Time.now() < turn_time + rospy.Duration.from_sec(1):
    #     pub.publish(velocity)
    
    velocity.linear.x = 0
    velocity.angular.z = 0
    pub.publish(velocity)
    rate = rospy.Rate(10)

    while distance(goal_pos) >= 0.01:
        # print(distance(goal_pos), curr_posx, curr_posy)
        velocity.linear.x = 1.5 * distance(goal_pos)
        velocity.angular.z = 6 * angle(goal_pos)
        print(distance(goal_pos), angle(goal_pos))
        pub.publish(velocity)
        rate.sleep()

    velocity.angular.z = 0
    velocity.linear.x = 0
    pub.publish(velocity)
    # rospy.spin()

    # list_cord = []

    # for i in range(3):
    #     x = float(input("Set your x goal: "))
    #     y = float(input("Set your y goal: "))
    #     cord = [x, y]
    #     list_cord.append(cord)
    
    # x = curr_posx
    # y = curr_posy
    # cord = [x, y]
    # list_cord.append(cord)

    # for i in range(3):
    #     goal_pos.x = list_cord[i][0]
    #     goal_pos.y = list_cord[i][1]

    #     velocity.linear.x = 0
    #     velocity.angular.z = 0
    #     pub.publish(velocity)

    #     while distance(goal_pos) >= 0.01:
    #         # print(distance(goal_pos), curr_posx, curr_posy)
    #         velocity.linear.x = 1.5 * distance(goal_pos)
    #         velocity.angular.z = 6 * angle(goal_pos)
    #         pub.publish(velocity)
    #         # rospy.sleep(0.000001)

    #     velocity.angular.z = 0
    #     velocity.linear.x = 0
    #     pub.publish(velocity)


if __name__ == '__main__':
    try:
        coordinate_square()
    except rospy.ROSInterruptException:
        pass

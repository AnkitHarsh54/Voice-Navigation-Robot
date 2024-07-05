#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
    # Initialize the ROS node with a unique name
    rospy.init_node('Circle', anonymous=True)

    # Create a publisher object
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # linear and angular speeds
    l_speed = 6.0
    a_speed = 4.0

    # Defined Rate
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        # Create Twist message
        twist = Twist()
        twist.linear.x = l_speed  # Set linear speed

        # Set angular speed (for rotational movement around the z-axis)
        twist.angular.z = a_speed

        # Publish Twist message
        pub.publish(twist)

        # Log the published message (for debugging)
        rospy.loginfo(f"Linear speed: {l_speed}, Angular speed: {a_speed}")

        # Sleep according to the rate (1 Hz)
        rate.sleep()
circle()
# if __name__ == '__main__':
#     try:
#         circle()
#     except rospy.ROSInterruptException:
#         pass


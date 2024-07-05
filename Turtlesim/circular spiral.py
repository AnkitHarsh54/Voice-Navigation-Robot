#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def spiral():
    # Initialize the ROS node with a unique name
    rospy.init_node('Spiral', anonymous=True)

    # Create a publisher object
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Initial linear and angular speeds
    l_speed = 1  # Start with a modest linear speed
    a_speed = 2  #constant angular speed

    # Rate at which the loop runs (1 Hz)
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

        # Adjust velocities for the next iteration
        l_speed += 0.2  # Gradually increase linear speed
        

        # Sleep according to the rate (1 Hz)
        rate.sleep()
spiral()
# if __name__ == '__main__':
#     try:
#         spiral()
#     except rospy.ROSInterruptException:
#         pass

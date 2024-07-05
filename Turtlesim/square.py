#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def square():
    # Initialize the ROS node with a unique name
    rospy.init_node('Square', anonymous=True)

    # Create a publisher object
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Initial linear speed
    l_speed = 1.0  # Adjust speed as needed for your square size

    # Rate at which the loop runs (1 Hz)
    rate = rospy.Rate(1)

    # Duration for each segment of the square path (in seconds)
    segment_duration = 2.0

    while not rospy.is_shutdown():
        # Create Twist message
        twist = Twist()

        # Move forward (along x-axis)
        twist.linear.x = l_speed
        pub.publish(twist)
        rospy.loginfo(f"Moving forward: Linear speed: {l_speed}")
        rospy.sleep(segment_duration)  # Keep moving for segment_duration seconds

        # Stop the turtle
        twist.linear.x = 0.0
        pub.publish(twist)
        rospy.sleep(1.0)  # Pause for a second after each movement

        # Turn (rotate 90 degrees)
        twist.angular.z = pi/2  # Rotate 90 degrees (in radians)
        pub.publish(twist)
        rospy.loginfo("Turning 90 degrees")
        rospy.sleep(segment_duration)  # Keep turning for segment_duration seconds

        # Stop the turtle
        twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1.0)  # Pause for a second after each movement

    rospy.spin()  # Ensure the node does not exit

if __name__ == '__main__':
    try:
        square()
    except rospy.ROSInterruptException:
        pass

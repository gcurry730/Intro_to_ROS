#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import JointState

PI = 3.14

def msg_pub():
    rospy.init_node('message_publisher')
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)    
 
    start = rospy.Time.now() 
	
    while not rospy.is_shutdown():

     msg = JointState()
     time = (rospy.Time.now() - start).to_sec()

     # The desired path
     x = (0.5)*math.cos((2.0*PI*time)/5.0) + 1.25
     y = (0.5)*math.sin((2.0*PI*time)/5.0)

     # IK solution:
     # solve for theta2: 
     a = math.sqrt(1-math.pow(((math.pow(x,2) + math.pow(y,2)-2)/2),2))
     b = ((math.pow(x,2) + math.pow(y,2)-2)/2)
     theta2 = math.atan2(a,b)
     
     # solve for theta1:
     k1 = 1 + math.cos(theta2)
     k2 = math.sin(theta2) 
     gamma = math.atan2(k2,k1)
     theta1 = math.atan2(y,x) - gamma

     # fill in the message
     msg.header.stamp = rospy.Time.now()     
     msg.name = ["base_to_first_link", "first_to_second_link"]
     msg.position = [theta1,theta2]
     msg.velocity = []
     msg.effort = []

     # debugging
     rospy.loginfo("=========================")
     rospy.loginfo("=========================")
     rospy.loginfo("Joint: %s, Position: %.2f", msg.name[0], msg.position[0])
     rospy.loginfo("Joint: %s, Position: %.2f", msg.name[1], msg.position[1])
     rospy.loginfo("=========================")
     rospy.loginfo("=========================")
     rospy.loginfo("Xdesired: %f, Ydesired: %f", x,y)

     # publish message
     pub.publish(msg)
     rospy.sleep(0.01)

if __name__ == '__main__':
	
    try:
        msg_pub()
    except rospy.ROSInterruptException:
        
	pass

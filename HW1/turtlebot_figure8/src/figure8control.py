#!/usr/bin/env python
import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

PI = 3.14 


def msg_pub():
    rospy.init_node('message_publisher')
    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)    
 
    start = rospy.Time.now() 
	
    while not rospy.is_shutdown():
     if rospy.has_param('~param_period'):
     	T = rospy.get_param('~param_period')
     else: 
     	T = 10

     msg = Twist()
     time = (rospy.Time.now() - start).to_sec()

     vx = ((12*PI)/T)*math.cos((4*PI*time)/T)
     vy = ((6*PI)/T)*math.cos((2*PI*time)/T)
     
     msg.linear.x = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2)) 
	
     a = 4*PI*(3*math.sin(2*PI*time/T) + math.sin(6*PI*time/T))
     b = T*(math.cos(4*PI*time/T) + 4*math.cos(8*PI*time/T) + 5)
     
     msg.angular.z = a/b
     #-4*PI*math.sin(2*PI*time/T)/T*(3+2*math.cos(4*PI*time/T)) //This makes a cool design	

     rospy.loginfo("Vx: %.2f, Wz: %.2f with Period: %i s", msg.linear.x, msg.angular.z, T)

     pub.publish(msg)
     rospy.sleep(0.01)

def move_to_init_client(x, y, theta):
     rospy.wait_for_service('turtle1/teleport_absolute')
     try:
         move_turtle = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
         resp1 = move_turtle(x, y, theta)
	 rospy.loginfo("Moved to : %f , %f , %f", x, y, theta)
        
     except rospy.ServiceException, e:
         print "Service call failed: %s"%e

if __name__ == '__main__':

    move_to_init_client(5.44, 5.44, 0) 
	
    try:
        msg_pub()
    except rospy.ROSInterruptException:
        pass

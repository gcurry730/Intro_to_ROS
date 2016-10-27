#!/usr/bin/env python
import rospy
import tf
import random
import geometry_msgs.msg
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

def msg_pub():
    rospy.init_node('marker_publisher')
    pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    listener = tf.TransformListener()

    while not rospy.is_shutdown():
	# first subscribe....
        try:
	    (trans,rot) = listener.lookupTransform('/base_link', '/end_effector', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rospy.loginfo("Transform, x: %.2f y: %.2f", trans[0], trans[1])
	
	# then publish
        marker = Marker()
        marker.header.frame_id = "/base_link";
        marker.header.stamp = rospy.Time.now();
        marker.id = random.randint(1, 1000);
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.05
        marker.scale.y = 0.05
        marker.scale.z = 0.05
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = trans[0]
        marker.pose.position.y = trans[1] 
        marker.pose.position.z = 0.0 
        marker.lifetime = rospy.Duration(2.)
	
	pub.publish(marker)

        rospy.sleep(0.02)

if __name__ == '__main__':
	
    try:
        msg_pub()
    except rospy.ROSInterruptException:
        
	pass

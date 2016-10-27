# Intro_to_ROS
repo for ROS packages developed during a course at NU

## Homework 1 

#### **3.1 Package**: turtlebot_figure8
* Package can be found here: [turtlebot_figure8](https://github.com/gcurry730/Intro_to_ROS/tree/master/HW1/turtlebot_figure8)
* Dependencies: [turtlesim](http://wiki.ros.org/turtlesim)
* This script contains the node: [figure8control.py](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW1/turtlebot_figure8/src/figure8control.py)

#### **3.2 Node**: figure8control

This node sends linear velocity and angular velocity commands to turtle1, a turtlesim node, to make it folllow a figure-eight trajectory. 
    
* Published Topics: **turtle1/cmd_vel**	([geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html))
* Subscribed Topics: None
* Services: **turtle1/teleport_absolute** ([turtlesim/TeleportAbsolute](http://docs.ros.org/api/turtlesim/html/srv/TeleportAbsolute.html))  
* Parameters: **~param_period** controls the period of oscillation, deault is 10s. 

Example command line usage: 
```
rosrun turtlebot_figure8 figure8control.py _param_period:=10.0
```
#### **3.3 Bag Files**
* Bag file can be found here: [bag](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-gcurry730/blob/master/2016-10-06-19-23-13.bag). 
	* It contains the data published to **turtle1/cmd_vel** over a period of one figure-eight.  


## Homework 2
 

### **Package**: two_link_robot
* Package can be found here: [two_link_robot](https://github.com/gcurry730/Intro_to_ROS/tree/master/HW2/two_link_robot)
* Dependencies: [rviz](http://wiki.ros.org/rviz)
* This script contains the nodes: [circle_path_pub.py](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW2/two_link_robot/src/circle_path_pub.py) and [marker_pub.py](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW2/two_link_robot/src/marker_pub.py)

### 2.1 Generating a URDF
* URDF:  [here](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW2/two_link_robot/urdf/twolinkmodel.urdf). 

### 2.2 Inverse Kinematics 

#### **Node**: circle_path_pub

This node calculates the IK solution ([equations found here](https://ashwinnarayan.blogspot.com/2014/07/inverse-kinematics-for-2dof-arm.html)) for the end effector of the two-link robot to follow a circular path in the XY plane, and sends the joint states to the robot_state_publisher to visualize in rviz. 
    
* Published Topics: **/joint_states** ([sensor_msgs/JointState](http://docs.ros.org/api/sensor_msgs/html/msg/JointState.html))
* Subscribed Topics: None
* Services: None  
* Parameters: None 

### 2.3 Animating a Trajectory

#### **Node**: marker_pub

This node listens to **tf** data from the *base_link* frame to the *end_effector* frame. It then publishes a [Marker](http://wiki.ros.org/rviz/DisplayTypes/Marker) message to **rviz** to visualize the path of the end effector. The marker is a sphere which is added every loop and which dissapears after two seconds, to create a line behind the path of the end effector.

* Published Topics: **/visualization_marker** ([visualization_msgs/Marker](http://docs.ros.org/jade/api/visualization_msgs/html/msg/Marker.html))
* Subscribed Topics: **/tf** ([tf2_msgs/TFMessage](http://docs.ros.org/kinetic/api/tf/html/msg/tfMessage.html))
* Services: None  
* Parameters: None 

### 2.4 Deliverables 
 
* Run from a single **launch file** located [here](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW2/two_link_robot/launch/twolink.launch).

* *Example Usage:*
```
roslaunch two_link_robot twolink.launch
```
* The **rviz config file** can be found [here](https://github.com/gcurry730/Intro_to_ROS/blob/master/HW2/two_link_robot/rviz/urdf.rviz).

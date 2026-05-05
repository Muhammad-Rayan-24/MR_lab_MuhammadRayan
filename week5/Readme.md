# Lab 5: Introduction to Gazebo, RViz, and TurtleBot3

## Overview
This repository contains the deliverables for Lab 5 of the Mobile Robotics course. The primary objective of this lab was to simulate the TurtleBot3 'burger' model using Gazebo, visualize its sensor data (LiDAR, TF, Odometry) in RViz, and generate a 2D map using the Cartographer SLAM package. 

Additionally, this package includes custom Python nodes to programmatically control the robot's velocity and read its odometry data.

## Package Structure
The `lab5_turtlebot3_pkg` contains the following directories:
* `/images`: Contains screenshots of RViz, rqt_graph, and terminal outputs.
* `/maps`: Contains the `.pgm` and `.yaml` files of the SLAM-generated map.
* `/bag_files`: Contains the recorded `.db3` ROS 2 bag file of the robot's motion.
* `/lab5_turtlebot3_pkg`: Contains the custom Python scripts (`vel_publisher.py` and `odom_subscriber.py`).

## Prerequisites
Ensure you have the following installed on an Ubuntu 22.04 system:
* ROS 2 Humble
* Gazebo ROS packages
* TurtleBot3 packages (`ros-humble-turtlebot3*`)

## Build Instructions
Before running the custom nodes, you must build the package in your ROS 2 workspace:

```bash
cd ~/your_ros2_ws
colcon build --packages-select lab5_turtlebot3_pkg
source install/setup.bash

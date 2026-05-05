# Lab 6: Reactive Navigation Using TurtleBot3 LiDAR

## Overview
This repository contains the deliverables for Lab 6 of the Mobile Robotics course. The objective of this lab was to implement autonomous, reactive navigation using LiDAR sensor data (`/scan`) in a Gazebo simulation environment. 

Unlike previous map-based navigation, this package allows the TurtleBot3 to act autonomously in an unknown environment by extracting directional distances (front, left, right) and computing real-time motion commands for obstacle detection, avoidance, and wall following.

## Package Structure
The `lab6_reactive_nav` package contains the following directories:
* `/images`: Contains screenshots of RViz LaserScan visualization, rqt_graph, and the robot actively avoiding obstacles.
* `/lab6_reactive_nav`: Contains the custom Python node (`lidar_navigator.py`).

## Prerequisites
Ensure you have the following installed on an Ubuntu 22.04 system:
* ROS 2 Humble
* Gazebo ROS packages
* TurtleBot3 packages (`ros-humble-turtlebot3*`)

## Build Instructions
Before running the autonomous node, you must build the package in your ROS 2 workspace:
```bash
cd ~/your_ros2_ws
colcon build --packages-select lab6_reactive_nav
source install/setup.bash

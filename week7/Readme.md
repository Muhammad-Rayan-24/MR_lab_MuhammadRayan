# Lab 7: Autonomous Navigation & Multi-Waypoint Mission Planning

## Overview
This package implements the full autonomous navigation pipeline using the **ROS 2 Nav2 (Navigation 2) Stack**. Building upon the static map generated in previous sessions, this package enables a TurtleBot3 to localize itself via **AMCL (Adaptive Monte Carlo Localization)** and execute complex, multi-waypoint patrol missions.

The primary node included, `waypoint_navigator`, demonstrates both hardcoded mission execution (Task 2) and dynamic waypoint injection via command-line arguments (Task 3).

## Prerequisites
* **ROS 2 Humble**
* **Nav2 Navigation Stack** (`ros-humble-navigation2`, `ros-humble-nav2-bringup`)
* **TurtleBot3 Packages** (`ros-humble-turtlebot3-gazebo`, `ros-humble-turtlebot3-navigation2`)
* A saved map from Lab 5 (`my_map.pgm` and `my_map.yaml`)

## Build Instructions
Clone this package into your ROS 2 workspace and build it:

```bash
cd ~/Rayan_ros2_ws
colcon build --packages-select lab7_nav
source install/setup.bash

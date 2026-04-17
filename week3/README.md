# Mobile Robotics Lab - Week 3

*Instructor - Ma'am Maria Akram* | *Repo Owner - Muhammad Rayan*

## Description
This folder contains the deliverables and source code for Week 3. The objective of this lab was to set up a custom ROS 2 workspace, create a Python package (`my_turtle_package`), and write modular nodes to control `turtlesim`. We explored open-loop control (drawing shapes), dynamic topic remapping for multi-robot control, and closed-loop proportional control.

## Repository Structure
* **`MR_lab_3_Report_2022_MC_55.pdf`**: The formal lab report detailing the methodology, math, and observations.
* **`my_turtle_package/`**: The complete source code of the custom ROS 2 package containing the modular Python nodes.
* **`screenshots/`**: Visual proofs of the deliverables, including the multi-turtle swarm and the interactive closed-loop controller in action.

## Node Modularity & Features
Instead of a monolithic script, behaviors were separated into specific nodes:
1. `my_node` (Square pattern)
2. `draw_circle` (Circular pattern)
3. `draw_triangle` (Triangular pattern)
4. `go_to_goal` (Interactive Closed-Loop Controller)
   * *Feature:* Subscribes to `/turtle1/pose` to calculate Euclidean distance error.
   * *Feature:* Uses a Proportional (P) controller to smoothly steer and decelerate.
   * *Feature:* Prompts the user via terminal input to define custom (X, Y) target coordinates dynamically.

## Key Commands Used
**1. Building the Package:**
```bash
cd ~/Rayan_ros2_ws
colcon build
source install/setup.bash

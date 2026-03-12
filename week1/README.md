# Mobile Robotics Lab - Week 1

*Instructor - Ma'am Maria Akram*
*Repo Owner - Muhammad Rayan*

## Description

**This repository contains the deliverables for Week 1 of the Mobile Robotics lab.** 

The primary objectives were to set up a ROS 2 Humble workspace on Ubuntu, learn fundamental Linux navigation, and create our first  custom Python package (`my_first_pkg`). 
The package includes nodes that demonstrate basic logging, file-based execution counting, and ROS 2 parameter handling i personally added a user input in the parameter handling task.

## Commands Used

The following commands were used heavily in this week 1 lab 
* `source /opt/ros/humble/setup.bash`: Sourced the core ROS 2 environment.
* `colcon build`: Compiled the workspace.
* `source install/setup.bash`: Sourced the local workspace overlay.
* `ros2 pkg create --build-type ament_python my_first_pkg`: Created the new Python package.
* `chmod +x <filename>`: Made the Python node scripts executable].
* `ros2 run my_first_pkg <node_name>`: Executed the specific nodes.
* `ros2 run my_first_pkg simple_node_with_parameter --ros-args -p student_name:="Muhammad Rayan"`: Ran a node while passing a custom parameter via the terminal.

## Problems Faced & Solutions

During the lab, I encountered a `SyntaxError` when attempting to build the workspace after editing `setup.py`. The build aborted because I accidentally used an equals sign to assign the entry point instead of wrapping the entire mapping in a single string. I solved this by reviewing the terminal traceback, opening `setup.py` with `nano`, and correcting the syntax to `'simple_node = my_first_pkg.simple_node:main',` before rebuilding with `colcon build`. Furthermore, I initially encountered the `executable not found` error, which was quickly resolved by remembering to run `colcon build` after modifying Python files Moreover during the parameter node execution i encountered many errors but most of them were related to Python syntax and my personal typo errors in the Ubuntu Command line.

## Reflection

Setting up the ROS 2 Humble environment this week provided a crucial foundation for bridging the gap between hardware and software. Coming from a mechatronics and control engineering perspective, seeing how nodes modularize tasks like sensor data parsing or actuator control makes the architecture of complex robotic systems much clearer. Overcoming the initial learning curve with the Linux environment, particularly understanding the absolute necessity of sourcing setups and rebuilding the workspace, was highly practical. Moving from basic terminal navigation to writing custom Python nodes with interactive parameters gives me a solid starting point for designing the communication networks required for my future mobile robot designs.I personally was super excited for this Mobile RObotics Course because I really like this and am really fond of this and i want to be able to use ROS2 properly so i could make place for myself in the industry.

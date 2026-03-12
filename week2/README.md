# Mobile Robotics Lab - Week 1

*Instructor - Ma'am Maria Akram*
*Repo Owner - Muhammad Rayan*

## Description

This folder contains the deliverables for Week 2 of the Mobile Robotics lab. The primary objective of this lab was to get familiar with turtlesim in ROS 2, utilize Command Line Interface (CLI) tools, and explore how nodes communicate via ROS 2 Topics and Services. Finally, we used the rqt Graphical User Interface to control the simulation and change parameters.##A Detailed explanation of the entire lab including all the commands used and all the porblems faced are mention in the attached pdf file of the lab report

#Repo Contents

* MR_lab_2_Report_2022_MC_55.pdf: The detailed, formal lab report explaining all observations, the "ghost driver" 1 Hz loop conflict, and step-by-step methodology.

* screenshots/: A directory containing all visual proofs of the deliverables, including:

	* Calling the /reset service via rqt.

	* Calling the /spawn service via rqt.

	* Independent movement of a second turtle using the rqt Message Publisher.

#Key Commands Used

* For quick reference, here are the primary ROS 2 CLI commands utilized in this lab:

* ros2 run turtlesim turtlesim_node (Launch simulation)

* ros2 run turtlesim turtle_teleop_key (Keyboard control)

* ros2 topic list (List active communication channels)

* ros2 topic echo /turtle1/pose (Spy on live coordinate data)

* ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist ... (Publish autonomous velocity commands)

* ros2 service call /reset std_srvs/srv/Empty (Reset the simulation)

* rqt (Launch the ROS 2 GUI)
A bonus experiment modifying the turtlesim background color using Dynamic Parameter Reconfigure.

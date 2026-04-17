# Mobile Robotics Lab - Week 4

*Instructor - Ma'am Maria Akram* | *Repo Owner - Muhammad Rayan*

## Description
This folder contains the deliverables for Week 4. The objective was to transition from individual node execution to system-level ROS 2 management. We utilized Launch files for automated startup, Rosbag for data logging, and rqt_plot for real-time kinematic visualization. 

## Repository Structure
* **`MR_lab_4_Report_2022_MC_55.pdf`**: The formal lab report detailing the methodology, terminal commands, and mathematical logic.
* **`my_launch_pkg/`**: The custom ROS 2 package containing the Python launch file and the Follow-the-Leader autonomous tracking node.
* **`bags/`**: The extracted Rosbag trajectory data recorded during teleoperation.
* **`screenshots/`**: Visual proofs of the dual-turtle launch, active rosbag recording, the follow-the-leader execution, and the live rqt_plot graphing.

## Key Features Implemented
1. **Launch Files:** Automated the startup of the simulator and the dynamic spawning of multiple entities.
2. **Rosbag Logging:** Captured live pose and velocity topics for offline analysis and playback.
3. **Follow-the-Leader Node:** A custom script utilizing proportional control math to make `turtle2` autonomously track and chase `turtle1` based on real-time coordinate feedback.
4. **Data Visualization:** Plotted live kinematic data streams using `rqt_plot` to verify control signal integrity.

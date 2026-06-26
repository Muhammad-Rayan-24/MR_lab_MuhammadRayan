# Lab 9: Vision-Based Target Tracking Using Camera 📷🤖

**Course:** MCT-454L Mobile Robotics  
**Platform:** TurtleBot3 Waffle (Gazebo Simulation)  
**Author:** Muhammad Rayan Ur Rehman  

## 📝 Overview

This repository contains the ROS 2 package and source code for Lab 9. The objective of this lab is to implement a complete perception-to-control pipeline. Using the TurtleBot3 Waffle's onboard camera, the robot processes live image feeds using OpenCV, isolates specific colored objects via HSV masking, calculates the centroid, and uses a Proportional (P) Controller to autonomously navigate toward the targets.

### ✨ Key Features Implemented:

* **ROS 2 & OpenCV Integration:** Bridges `/camera/image_raw` using `cv_bridge`.
* **Advanced Color Segmentation:** Handles the HSV "red wrap-around" using bitwise mask combinations.
* **Proportional Control:** Dynamically calculates angular velocity based on the pixel error from the camera's center.
* **Finite State Machine (FSM):** The robot sequentially hunts multiple targets:
  1. Searches for and tracks a **Red Sphere**.
  2. Once reached, rotates to search for and track a **Green Cuboid**.
  3. Halts and spins in place once the mission is complete.

## 🛠️ Prerequisites

Ensure you have the following installed on your Ubuntu machine running **ROS 2 Humble**:

```bash
sudo apt update
sudo apt install ros-humble-cv-bridge python3-opencv
sudo apt install ros-humble-turtlebot3* ros-humble-gazebo-ros-pkgs
```

## 🚀 How to Build and Run

### 1. Launch the Simulation Environment

The Waffle model must be used as it is equipped with a camera. Open a terminal and run:

```bash
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

*(Note: Drop a Red Sphere and a Green Cuboid into the Gazebo world so the robot has targets to track).*

### 2. Build the Workspace

Open a new terminal, navigate to your ROS 2 workspace, and build the package:

```bash
cd ~/Rayan_ros2_ws
colcon build --packages-select lab9_vision
source install/setup.bash
```

### 3. Run the Vision Tracking Node

Execute the `camera_follower` node. This will pop up OpenCV windows displaying the raw camera feed (with HUD overlays) and the active color mask.

```bash
ros2 run lab9_vision camera_follower
```

## 📊 Node Architecture

* **Subscribed Topic:** `/camera/image_raw` (Type: `sensor_msgs/Image`)
* **Published Topic:** `/cmd_vel` (Type: `geometry_msgs/Twist`)
* **Control Logic:**
  * K_p (Proportional Gain): `0.001`
  * Center Alignment Threshold: `40` pixels
  * Stopping Distance (Pixel Area): `550,000`

## 📁 Repository Contents

* `camera_follower.py`: The main ROS 2 Python node containing the FSM and OpenCV logic.
* `Lab_9_Final_Report.pdf/doc`: Detailed lab report including tuning observations and methodology.

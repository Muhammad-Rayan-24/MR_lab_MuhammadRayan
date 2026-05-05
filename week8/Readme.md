# Lab 8: Custom Mobile Robot Description (URDF)

## Overview
This package contains the **Unified Robot Description Format (URDF)** for a custom-designed differential drive mobile robot. Unlike standard tutorials, this model features a transparent chassis and modular sensor pillars to facilitate the study of internal coordinate frames and future sensor integration.

## Learning Outcomes
*   Constructed a hierarchical robot model using links and joints.
*   Resolved complex ROS 2 pathing and directory configuration issues.
*   Visualized real-time transform (TF) trees to verify mechanical logic.

---

## Package Structure
```text
my_robot_description/
├── CMakeLists.txt
├── package.xml
├── urdf/
│   └── my_robot.urdf      # The core robot description
├── launch/                # Corrected from 'lanch' for standard compliance
├── rviz/                  # Optional RViz configuration files
└── docs/                  # Contains generated frames.pdf and screenshots

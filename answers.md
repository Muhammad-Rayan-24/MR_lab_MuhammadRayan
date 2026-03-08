# Week 1 Post-Lab Questions

**1. Define: node, topic, package, workspace. Provide one sentence each.**
* [cite_start]**Node:** A Node can be defined as worker, a node does the task, in other workds it can be defined as a process that performs computation, such as a controller or sensor driver.[cite: 107].
* [cite_start]**Topic:** A Topic can be defined as Team name, for instance in a Technical team the workers do technical tasks or in other words a topic is a  named communication channel used for streaming messages between nodes[cite: 107].
* [cite_start]**Package:** A folder containing ROS 2 code, dependencies, and build information it contains everything necessary to run the ROS2 stuff.[cite: 111].
* [cite_start]**Workspace:** A directory that contains one or more ROS 2 packages and their build outputs we need to make our entire ROS2 commands and nodes and packages in a ROS2 Workspace[cite: 111].

**2. Explain why sourcing is required. What happens if you do not source a workspace?**
Sourcing updates the terminal's environment variables so it knows exactly where the ROS 2 installation and your custom packages are located. [cite_start]If you do not source the workspace, the terminal will not recognize ROS 2 commands, resulting in a `command not found` error[cite: 140], and it will be unable to locate or run any packages you have built.

**3. What is the purpose of colcon build? What folders does it generate?**
[cite_start]The `colcon build` command is used to compile the packages within a workspace so that ROS 2 can execute them[cite: 152]. [cite_start]It generates the `build/` (intermediate files), `install/` (installed packages and executables), and `log/` (build process logs) folders[cite: 162, 163].

**4. In your own words, explain what the entry_points console script does in setup.py.**
[cite_start]The `entry_points` console script acts as a map for ROS 2. It links a simple terminal command name (like `simple_node`) to the specific Python executable and function (like `main`) so the system knows exactly what code to run when the `ros2 run` command is executed if this is not included then the result would either be random or unwanted[cite: 190, 217].

**5. Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected by a topic.**
[cite_start] This is the best i could do :)

+-----------------+                                 +-------------------+
|     Node A      |                                 |      Node B       |
|   (Publisher)   |                                 |   (Subscriber)    |
|                 |                                 |                   |
| publishes msgs  |          /topic_name            | receives msgs     |
|                 +-------------------------------->| and acts on them  |
+-----------------+                                 +-------------------+

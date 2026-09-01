# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/humble/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: The first command ('source /opt/ros/humble/setup.bash') loads the installation of ROS2 Humble into the terminal. The second command ('source install/local_setup.bash') makes the packages in my workspace (lab1_pkg) available in the terminal on top of ROS2. 

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: The 'queue_size' argument determines how many messages can be stored in an outgoing buffer (in the case of a publisher) or an incoming message history (in the case of a subscriber). A small queue size uses less memory but there is a risk of dropping intermediate messages if there is a processing lag that overloads the buffer. A queue size that is too large prevents data loss during processing lags or slow callbacks but requires a lot of memory and can increase the amount of time it takes to process the message once received. The standard queue size is 10, which balances memory usage and message buffering for most robotic sensor rates and control loops. 

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: You don't need to call 'colcon build' again if the launch file is run from the source directory. However, if the launch file is run through the installed package (like 'ros2 launch lab1_pkg lab1_launch.py'), then the package needs to be rebuilt if the launch file is changed. This is because 'colcon build' copies the launch file into the workspace's install directory, and the launch command uses that installed version to launch the nodes rather than the version directly from the source. 

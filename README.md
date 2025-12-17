# F1TENTH Lab 1
Introduction to ROS2 and Docker

Assignment link: https://github.com/f1tenth/f1tenth_lab1_template

**Deliverable:** One publisher and one suscriber node for sending/receiving `AckermannDriveStamped` messages.

## Written Questions:
### Q1: During this assignment, you've probably ran these two following commands at some point: source /opt/ros/foxy/setup.bash and source install/local_setup.bash. Functionally what is the difference between the two?

They key difference between these two commands is that `source /opt/ros/foxy/setup.bash` sources the underlay, initializing the core ROS2 environment (standard ROS2 libraries, CLI tools, and built-in packages), while `source install/local_setup.bash` sources the overlay, which is specific to the current workspace. `local_setup.bash` only adds the packages found in that specific workspace, not the core ROS2 environment, so these two commands must be run in tandem.

### Q2: What does the queue_size argument control when creating a subscriber or a publisher? How does different queue_size affect how messages are handled?

Queue size determines the maximum number of messages that will be stored during the processing time (callback runtime) of one message. If the queue is full and an 11th message arrives before the first one is finished, the oldest message in the queue is discarded to make room for the newest one. A smaller queue size is more effective for time-sensitive data like sensors, where old states are effectively useless. A longer queue size is best for important events or commands where you cannot afford to lose a single message.

### Q3: Do you have to call colcon build again after you've changed a launch file in your package? (Hint: consider two cases: calling ros2 launch in the directory where the launch file is, and calling it when the launch file is installed with the package.)

If you point `ros2 launch` directly to the path of the launch file `src/`, you do not need to rebuild. If you run `ros2 launch package_name file.py`, ROS 2 looks in the `install/` directory soyou must call colcon build again to copy the modified file from `src/` to `install/`.

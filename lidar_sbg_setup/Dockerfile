ARG ROS_DISTRO=humble 
FROM ros:${ROS_DISTRO}

# System dependencies
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-sbg-driver \
    ros-${ROS_DISTRO}-ouster-ros \
    && rm -rf /var/lib/apt/lists/*

# --- Source ROS2 ---
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc 


ARG ROS_DISTRO=humble 
FROM ros:${ROS_DISTRO}

# System dependencies
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-sbg-driver \
    ros-${ROS_DISTRO}-ouster-ros
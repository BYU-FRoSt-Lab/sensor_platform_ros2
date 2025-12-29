#!/bin/bash
set -e

CONTAINER="ouster_lidar_sbg"
BAGS_PATH='/root/bags/local'
TOPICS="/imu/data /imu/nav_sat_fix /points /tf /tf_static" # '/imu' for ouster imu

echo ""
echo "IMPORTANT! Name the rosbag with the testing location combined with the test number (ex. 'utah_lake1.0')"
echo "-> If the mission fails, keep the same name and increment the second number for reruns (ex. 'utah_lake1.1')"
echo "-> If the mission is successful, increment the first number to indicate a new mission (ex. 'utah_lake2.0')"
echo ""
read -p "Enter a folder name for the rosbag: " folder
echo ""

TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
BAG_NAME="${folder}-${TIMESTAMP}"
BAG_DIR="${BAGS_PATH}/${BAG_NAME}"


echo "Starting rosbag recording..."
echo "Bag directory: ${BAG_DIR}"
echo "Topics: ${TOPICS}"
echo ""

docker exec -it "${CONTAINER}" bash -c "
    source /root/ros2_ws/install/setup.bash &&
    ros2 bag record \
    -s mcap \
    --storage-preset-profile fastwrite \
    --max-cache-size 200000000 \
    -o '${BAG_DIR}' \
    ${TOPICS}
"

echo "Copying config"
docker exec "${CONTAINER}" bash -c "
  set -e
  cp -r /root/config '${BAG_DIR}/config'
"
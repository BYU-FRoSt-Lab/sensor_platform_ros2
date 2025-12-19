import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	sbg_config = os.path.join(
		'/root',
		'config',
		'sbg_driver_params.yaml'
	)
	ntrip_config = os.path.join(
        '/root',
        'config',
        'ntrip_client_params.yaml'
    )
	nmea_config = os.path.join(
        '/root',
        'config',
        'nmea_gpsd_params.yaml'
    )

	return LaunchDescription([
		DeclareLaunchArgument('namespace', default_value='/'),
		Node(
			package='sbg_driver',
		#	name='sbg_device_1',
			executable = 'sbg_device',
			output = 'screen',
			namespace=LaunchConfiguration('namespace'),
			parameters = [sbg_config]
		),
		Node(
			package='nmea_gpsd',
			executable='nmea_gpsd_udp',
			output='screen',
			namespace=LaunchConfiguration('namespace'),
			parameters=[nmea_config]
        ),
		Node(
            package='ntrip_client',
            executable='ntrip_ros.py',
            name='ntrip_client',
            namespace=LaunchConfiguration('namespace'),
            parameters=[ntrip_config],
        )
		
	])

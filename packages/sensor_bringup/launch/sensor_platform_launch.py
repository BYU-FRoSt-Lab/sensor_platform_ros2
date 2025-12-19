import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
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
		Node(
			package='sbg_driver',
		#	name='sbg_device_1',
			executable = 'sbg_device',
			output = 'screen',
			parameters = [sbg_config]
		),
		Node(
			package='nmea_gpsd',
			executable='nmea_gpsd_udp',
			output='screen',
			parameters=[nmea_config]
        ),
		Node(
                name='ntrip_client',
                package='ntrip_client',
                executable='ntrip_ros.py',
				parameters=[ntrip_config]
        ),
		
	])

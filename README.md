Setup the pps line by putting this on a raspberry pi /boot/config.txt at the end
'''
# the next 3 lines are for GPS PPS signals
dtoverlay=pps-gpio,gpiopin=18
enable_uart=1
init_uart_baud=9600

'''

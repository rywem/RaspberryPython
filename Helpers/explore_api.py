import RPi.GPIO as GPIO

#list all functions and attributes
print(dir(GPIO))

# Get detailed help on a specific method
help(GPIO.RPI_INFO)

'''
['BCM', 'BOARD', 'BOTH', 'Event', 'FALLING', 'HARD_PWM', 'HIGH', 'I2C', 'IN', 'LOW', 'OUT',
'PUD_DOWN', 'PUD_OFF', 'PUD_UP', 'PWM', 'Path', 'RISING', 'RPI_INFO', 'RPI_REVISION',
'SERIAL', 'SPI', 'UNKNOWN', 'VERSION', 'WeakValueDictionary', '_Alert', '_BCM_MAP',
'_BOARD_MAP', '_LG_ALERT', '_LG_GROUP', '_LG_INPUT', '_LG_MODES', '_LG_OUTPUT', '_LG_PULLS',
'_LG_PULL_DOWN', '_LG_PULL_NONE', '_LG_PULL_UP', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__path__', '__spec__', '_alerts', '_check', '_check_bounce', '_check_edge', '_check_input',
'_check_output', '_chip', '_from_gpio', '_get_alert', '_get_gpiochip_num', '_get_rpi_info', '_gpio_list',
'_in_use', '_mode', '_pwms', '_retry', '_set_alert', '_to_gpio', '_unset_alert', '_warnings',
'add_event_callback', 'add_event_detect', 'cleanup', 'event_detected', 'getmode', 'gpio_function',
'input', 'lgpio', 'os', 'output', 'remove_event_detect', 'setmode', 'setup', 'setwarnings', 'sleep',
'struct', 'sys', 'wait_for_edge', 'warnings']
'''
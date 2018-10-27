"""
This is octopusLab basic library for robotBoard PCB
Edition: --- 21.10.2018 ---
Installation:
ampy -p /dev/ttyUSB0 put ./octopus_robot_board.py
"""

from micropython import const

#ESP32 pinout setup
BUILT_IN_LED = const(2)
WS_LED_PIN = const(13)    #ws RGB ledi diode
ONE_WIRE_PIN = const(32)  #one wire (for Dallas temperature sensor)

#I2C:
I2C_SCL_PIN = const(22)
I2C_SDA_PIN = const(21)

#PWM/servo:
PWM1_PIN = const(17)
PWM2_PIN = const(16)
PWM3_PIN = const(4)
#pwm duty for servo:
SERVO_MIN = const(38)
SERVO_MAX= const(130)

#inputs:
I39_PIN = const(39)
I34_PIN = const(34)
I35_PIN = const(35)

#main analog input (for power management)
PIN_ANALOG = const(36)

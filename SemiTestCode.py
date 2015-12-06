#!/usr/bin/python
# MOTORS
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
​
#right front
PWM.start("P9_14", 0, 1000, 0)
#right back
PWM.start("P9_16", 0, 1000, 0)
#left back
PWM.start("P8_13", 0, 1000, 0)
#left front
PWM.start("P8_19", 0, 1000, 0)
print "Hello, World!"
​
#right front motor
GPIO.setup("P9_11", GPIO.OUT); GPIO.output("P9_11", GPIO.LOW)
GPIO.setup("P9_12", GPIO.OUT); GPIO.output("P9_12", GPIO.LOW)
print "Check 1"
#right back motor
GPIO.setup("P9_13", GPIO.OUT); GPIO.output("P9_13", GPIO.LOW)
GPIO.setup("P9_15", GPIO.OUT); GPIO.output("P9_15", GPIO.LOW)
print "Check 2"
#left back motor
GPIO.setup("P8_11", GPIO.OUT); GPIO.output("P8_11", GPIO.LOW)
GPIO.setup("P8_12", GPIO.OUT); GPIO.output("P8_12", GPIO.LOW)
print "Check 3"
#left front motor
GPIO.setup("P8_17", GPIO.OUT); GPIO.output("P8_17", GPIO.LOW)
GPIO.setup("P8_18", GPIO.OUT); GPIO.output("P8_18", GPIO.LOW)
print "Check 4"
​
​
print "Test Motor 1 - Right Front"
PWM.set_duty_cycle("P9_14", 50)
raw_input('Press enter to activate')
GPIO.output("P9_11", GPIO.HIGH)
GPIO.output("P9_12", GPIO.LOW)
print GPIO.output("P9_11",GPIO.HIGH)
print GPIO.output("P9_12",GPIO.LOW)
raw_input('Press enter to change direction')
GPIO.output("P9_11", GPIO.LOW)
GPIO.output("P9_12", GPIO.HIGH)
raw_input('Press enter to continue')
PWM.stop("P9_14")
​
print "Test Motor 2 - Right Back"
PWM.set_duty_cycle("P9_16", 50)
raw_input('Press enter to activate')
GPIO.output("P9_13", GPIO.HIGH)
GPIO.output("P9_15", GPIO.LOW)
raw_input('Press enter to change direction')
GPIO.output("P9_13", GPIO.LOW)
GPIO.output("P9_15", GPIO.HIGH)
raw_input('Press enter to continue')
PWM.stop("P9_16")
​
print "Test Motor 3 - Left Back"
PWM.set_duty_cycle("P8_13", 50)
raw_input('Press enter to activate')
GPIO.output("P8_11", GPIO.HIGH)
GPIO.output("P8_12", GPIO.LOW)
raw_input('Press enter to change direction')
GPIO.output("P8_11", GPIO.LOW)
GPIO.output("P8_12", GPIO.HIGH)
raw_input('Press enter to continue')
PWM.stop("P8_13")
​
print "Test Motor 4 - Left Front"
PWM.set_duty_cycle("P8_19", 50)
raw_input('Press enter to activate')
GPIO.output("P8_17", GPIO.HIGH)
GPIO.output("P8_18", GPIO.LOW)
raw_input('Press enter to change direction')
GPIO.output("P8_17", GPIO.LOW)
GPIO.output("P8_18", GPIO.HIGH)
raw_input('Press enter to continue')
PWM.stop("P8_19")
​
GPIO.cleanup()
PWM.cleanup()
​
#Setup the ADC
ADC.setup()
print "Test IR Sensor"
i=0
while i <= 0:
  print("Raw ",  ADC.read_raw("P9_39"))
  i=raw_input("Press 0 to re-read 1 to end")
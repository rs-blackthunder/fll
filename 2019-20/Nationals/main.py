#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import movement, missions

# test beeps
brick.sound.beep(1500, 500, 5)
brick.sound.beep(750, 500, 5)

# check current
if brick.battery.current() < 150:
  brick.sound.beep(1500, 1000, 5)
# check voltage
if brick.battery.voltage() < 7000:
  brick.sound.beep(750, 1000, 5)
# display current & voltage in console and on brick's screen
print(str(brick.battery.current()) + "mA")
print(str(brick.battery.voltage()) + "mV")
brick.display.clear()
brick.display.text(str(brick.battery.current()) + "mA", (60, 50))
brick.display.text(str(brick.battery.voltage()) + "mV")

# testing
# robot.drive_time(150,0,2000)
# robot.drive_time(0, 50, 7200)
# movement.turn(50, 0, 7200)
movement.lineFollow(True, 1)

# missions
# missions.Mission12.brown()
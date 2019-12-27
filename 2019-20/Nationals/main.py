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
brick.sound.beep(2000, 200, 50)

# check current
if brick.battery.current() < 150:
  brick.sound.beep(1000, 1000, 100)
# check voltage
if brick.battery.voltage() < 7000:
  brick.sound.beep(400, 1000, 100)
# display current & voltage in console and on brick's screen
print(str(brick.battery.current()) + "mA")
print(str(brick.battery.voltage()) + "mV")
brick.display.clear()
brick.display.text(str(brick.battery.current()) + "mA", (60, 50))
brick.display.text(str(brick.battery.voltage()) + "mV")

########## TESTING ##########
# movement.lineFollow(True, 0)
# movement.move(50, 0, 360)


########## MISSIONS #########
# missions.Mission12.brown()
# missions.Mission9()
missions.Mission2()
# movement.move(-10, 0, 54)

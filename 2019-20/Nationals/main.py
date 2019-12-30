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

# missions.Mission12.brown()
# missions.Mission9()
# missions.Mission2()
# movement.move(-10, 0, 54)

#############################

# use brick buttons & a colour sensor to choose missions
colour_sensor = ColorSensor(Port.S3)

# wait until button is pressed
while not (any(brick.buttons())):
  wait(10)

######## attachments that do only one mission (missions 1, 6 & 7) ########

if colour_sensor.color() == Color.RED:
  # display mission numbers so we know what has been detected
  brick.display.text(str("Missions 1, 6, 7 & 8"), (60, 50))
  # wait until button is pressed
  while not (any(brick.buttons())):
    wait(10)
  # clockwise is probable order (i.e. UP -> RIGHT -> DOWN -> LEFT)
  if Button.UP in brick.buttons():
    pass # mission 6
  elif Button.RIGHT in brick.buttons():
    pass # mission 7
  elif Button.DOWN in brick.buttons():
    pass # mission 8
  elif Button.LEFT in brick.buttons():
    pass # mission 1
  elif Button.MIDDLE in brick.buttons():  # in case colour sensor detects wrong colour
    break

##########################################################################



### attachments that do more than one mission (missions 2/9, 3/4 & 12) ###

# mission 12
elif colour_sensor.color() == Color.GREEN:
  # display mission number so we know what has been detected
  brick.display.text(str("Mission 12")
  # clockwise is probable order (i.e. UP -> RIGHT -> DOWN -> LEFT)
  if Button.UP in brick.buttons():
    missions.Mission12.blue()
  elif Button.RIGHT in brick.buttons():
    missions.Mission12.brown()
  elif Button.DOWN in brick.buttons():
    missions.Mission12.white()
  elif Button.LEFT in brick.buttons():
    missions.Mission12.red()
  elif Button.MIDDLE in brick.buttons():  # in case colour sensor detects wrong colour
    break

# mission 2 & 9
elif colour_sensor.color() == Color.BLUE:
  # display mission numbers so we know what has been detected
  brick.display.text(str("Mission 2/9")
  if Button.LEFT in brick.buttons():
    missions.Mission2()
  elif Button.RIGHT in brick.buttons():
    missions.Mission9()
  elif Button.MIDDLE in brick.buttons():  # in case colour sensor detects wrong colour
    break

##########################################################################
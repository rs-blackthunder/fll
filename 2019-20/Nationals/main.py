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
# missions.Mission2()
# movement.move(-10, 0, 54)

# Using brick buttons and colour sensors to run missions.
port = None 
coloursensor = ColorSensor(port) # I don't know the port, change port/ change port parameter to be the port of the colour sensor.

# Attachments that do only one mission (Mission 1, 6, 7 or 8)
if coloursensor.color() == Color.RED: # Change this to the colour being added to the attachment
  # Mission 6/7/8 when coded
  # Display "Mission 6/7/8" so we know what has been detected 
  brick.display.text(str("Mission 6/7/8")
  # Change the missions being executed so that they are in chronological order. I have tried to make it so that the first mission
  # gets executed by 'UP' and then the next ones are in a clockwise motion (i.e. UP -> RIGHT -> DOWN -> LEFT)
  if Button.UP in brick.buttons():
    pass # Mission 6
  elif Button.RIGHT in brick.buttons():
    pass # Mission 7
  elif Button.DOWN in brick.buttons():
    pass # Mission 8
  elif Button.LEFT in brick.buttons():
    pass # Mission 1
  elif Button.MIDDLE in brick.buttons(): # In case the colour sensor detects wrongly
    break

# Attachments that do a few missions. (Missions 2+9, 3+4(if being done), 12)
elif coloursensor.color() == Color.GREEN: # Same as above, change this to the colour being added to the attachment
  # Mission 12.
  # Display "Mission 12" so we know what has been detected 
  # Same as above, the individual stacks get executed in chronological order starting from UP and then in a clockwise motion. 
  brick.display.text(str("Mission 12")
  if Button.UP in brick.buttons():
    missions.Mission12.blue()
  elif Button.RIGHT in brick.buttons():
    missions.Mission12.brown()
  elif Button.DOWN in brick.buttons():
    missions.Mission12.white()
  elif Button.LEFT in brick.buttons():
    missions.Mission12.red()
  elif Button.MIDDLE in brick.buttons(): # In case the colour sensor detects wrongly
    break

elif coloursensor.color() == Color.BLUE: 
  # Mission 2 + 9
  # Display "Mission 2/9" so we know what has been detected 
  brick.display.text(str("Mission 2/9")                   
  if Button.LEFT in brick.buttons():
    missions.Mission2()
  elif Button.RIGHT in brick.buttons():
    missions.Mission9()
  elif Button.MIDDLE in brick.buttons(): # In case the colour sensor detects wrongly
    break

# Colours need to be added to the attachments. 
# Code needs to be checked in different light levels, may detect differently in different enviroments.
# Maybe add a fallback manual selection if the light sensor does not end up working




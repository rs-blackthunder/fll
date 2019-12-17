from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase

import movement

class Mission9:
  def __init__(self):
    # left_attachment.run_until_stalled(-90)
    # right_attachment.run_until_stalled(-90)
    movement.move(0, 100, 350)
    movement.lineFollow(True, 0)

class Mission12:
  def brown():
    movement.move(-10, 0, 50)
    movement.accelerate(0, 200, 0.001, 250, 7, False, False)
    movement.move(0, 200, 600)
    movement.accelerate(200, 0, 0.001, 300, 4, True, False)
    movement.accelerate(0, -200, 0.001, 150, 10, False, False)
    movement.move(0, -200, 1000)
  def red():
    movement.move(-10, 0, 35)
    movement.accelerate(0, 200, 0.001, 250, 7, False, False)
    movement.move(0, 200, 150)
    movement.accelerate(200, 0, 0.001, 300, 4, True, False)
    movement.accelerate(0, -200, 0.001, 150, 10, False, False)
    movement.move(0, -200, 550)
  def white():
    movement.move(10, 0, 61)
    movement.accelerate(0, 200, 0.001, 220, 7, False, False)
    movement.accelerate(200, 0, 0.001, 210, 5, False, False)
    movement.accelerate(0, -200, 0.001, 100, 10, False, False)
    movement.move(0, -200, 340)
  def blue():
    movement.accelerate(0, 200, 0.001, 200, 7, False, False)
    movement.accelerate(200, 0, 0.001, 200, 5, False, False)
    movement.accelerate(0, -200, 0.001, 100, 10, False, False)
    movement.move(0, -200, 300)

left_attachment = Motor(Port.B)
right_attachment = Motor(Port.C)
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase

class Mission12:
  def brown(self):
    movement.accelerate(0, 200, 0.001, 400, 5, False, False)
    movement.accelerate(200, 0, 0.001, 400, 5, True, True)
    movement.accelerate(0, -200, 0.001, 330, 5, True, False)
    movement.move(300, -300, 100, True, False)
    movement.move(0, -100, 200, True, False)

class Mission9:
  def __init__(self):
    left_attachment.run_until_stalled(-90)
    right_attachment.run_until_stalled(-90)
    # TODO: PID line following

left_attachment = Motor(Port.B)
right_attachment = Motor(Port.C)
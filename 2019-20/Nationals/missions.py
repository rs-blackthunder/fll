from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase

import movement

def resetAngles():
  left_attachment.reset_angle(0)
  right_attachment.reset_angle(0)

class Mission2:
  def __init__(self):
    movement.move(10, 0, 30)
    # movement.move(0, 150, 350)
    movement.accelerate(0, 150, 0.01, 300, 10, False, False)
    movement.accelerate(150, 0, 0.01, 112, 10, True, True)
    movement.move(-10, 0, 31)
    # movement.move(0, 150, 250)
    movement.accelerate(0, 150, 0.01, 100, 10, False, False)
    movement.accelerate(150, 0, 0.01, 84, 10, True, False)
    resetAngles()
    wait(1500)
    angle_to_turn = 220
    for i in range(2):
      left_attachment.run_angle(300, angle_to_turn, Stop.BRAKE, False)
      right_attachment.run_angle(300, angle_to_turn, Stop.BRAKE, True)
      left_attachment.run_angle(-300, angle_to_turn, Stop.BRAKE, False)
      if i != 1:
        right_attachment.run_angle(-300, angle_to_turn, Stop.BRAKE, True)
      else:
        right_attachment.run_angle(-300, angle_to_turn, Stop.BRAKE, False)
    movement.move(0, -200, 100)
    movement.move(-90, 0, 90)
    movement.move(0, 200, 200)

class Mission9:
  def __init__(self):
    movement.move(0, 150, 450)
    print("following")
    line_follow = movement.lineFollow(True, 20, 9)
    print("stopped")
    left_attachment.run_angle(300, 300, Stop.BRAKE, False)
    right_attachment.run_angle(300, 300, Stop.BRAKE, False)
    # movement.move(-10, 0, 40)
    # if line_follow < 30:
    #   movement.move(0, 150, 440)
    # else:
    #   movement.move(0, 150, 475)
    # movement.move(10, 0, 39)
    # if line_follow < 30:
    #   movement.move(0, 50, 150)
    # else:
    #   movement.move(0, 50, 130)
    print("turning", str(23 + 0.5 * line_follow), "degrees")
    movement.move(-10, 0, 23 + 0.5 * line_follow)
    movement.move(0, 150, 475)
    movement.move(10, 0, 23 + 0.5 * line_follow)
    movement.move(0, 50, 120)
    left_attachment.run_angle(-300, 205, Stop.BRAKE, False)
    right_attachment.run_angle(-300, 205, Stop.BRAKE, False)
    movement.move(10, 0, 25)
    resetAngles()
    left_attachment.run_angle(300, 300, Stop.BRAKE, False)
    right_attachment.run_angle(300, 300, Stop.BRAKE, True)
    movement.move(-10, 0, 55)
    movement.move(10, 0, 50)
    left_attachment.run_angle(-300, 395, Stop.BRAKE, False)
    right_attachment.run_angle(-300, 395, Stop.BRAKE, True)
    movement.move(0, -150, 200)
    movement.move(10, 0, 20)
    movement.move(0, 150, 350)
    movement.move(0, -150, 100)
    movement.move(-10, 0, 70)
    movement.move(0, -150, 600)
    movement.move(-10, 0, 15)
    movement.move(0, -150, 700)

class Mission12:
  def brown():
    movement.move(0, 50, 200)
    movement.move(-10, 0, 100)
    movement.accelerate(0, 150, 0.001, 250, 7, False, False)
    movement.move(0, 150, 605)
    movement.accelerate(150, 0, 0.001, 300, 4, True, False)
    movement.accelerate(0, -150, 0.001, 150, 10, False, False)
    movement.move(0, -150, 1000)
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

left_attachment = Motor(Port.B, Direction.CLOCKWISE)
right_attachment = Motor(Port.C, Direction.COUNTERCLOCKWISE)
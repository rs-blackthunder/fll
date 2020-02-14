from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

import movement

def resetAngles():
  left_attachment.reset_angle(0)
  right_attachment.reset_angle(0)

class Mission1:
  def __init__(self):
    Mission1.run()
  def run():
    left_colour_sensor = ColorSensor(Port.S1)
    right_colour_sensor = ColorSensor(Port.S2)
    # movement.move(0, 500, 1000)
    left_attachment.run_angle(30, 30, Stop.BRAKE, False)
    right_attachment.run_angle(30, 30, Stop.BRAKE, False)
    movement.accelerate(0, 150, 0.01, 500, 10, False, False)
    print("following")
    line_follow = movement.lineFollow(True, 32, 9)
    movement.move(-10, 0, 65)
    while left_colour_sensor.color != Color.BLACK or right_colour_sensor.color != Color.BLACK:
      movement.move(0, 10, 5)
    line_follow = movement.lineFollow(True, 1, 9)
    movement.move(0, 150, 300)


    line_follow = 60
    print("stopped")

class Mission2:
  def __init__(self):
    Mission2.run()
  def run():
    movement.move(10, 0, 37.5)
    movement.move(0, 100, 430)
    movement.move(-10, 0, 38.5)
    movement.accelerate(0, 150, 0.01, 100, 10, False, False)
    movement.accelerate(150, 0, 0.01, 84, 10, True, False)
    resetAngles()
    wait(1500)
    angle_to_turn = 221.7
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

class Mission9_2:
  def __init__(self):
    Mission9_2.run()
  def run():
    # movement.move(0, 500, 1000)
    left_attachment.run_angle(30, 30, Stop.BRAKE, False)
    right_attachment.run_angle(30, 30, Stop.BRAKE, False)
    movement.accelerate(0, 150, 0.01, 500, 10, False, False)
    print("following")
    line_follow = movement.lineFollow(True, 20, 9)
    line_follow = 38.213
    print("stopped")
    # angle_to_turn = 33.5 if (line_follow < 32) else 35 if (line_follow < 34) else 33.5
    #### angle_to_turn = -0.006 * line_follow ** 3 + 0.53 * line_follow ** 2 - 14.8* line_follow + 166
    angle_to_turn = 34
    angle_to_turn = 31.5
    # angle_to_turn = 32 if (0.6667*line_follow + 16.6667 < 32) else 39 if (0.6667*line_follow + 16.6667 > 39) else (0.6667*line_follow + 16.6667)
    # angle_to_turn = 0.0074074 * line_follow ** 2 +-0.174074 * line_follow + 33.51852
    # Working values: Value = 38.213, Turning = 39.57189919241802
    movement.move(-10, 0, angle_to_turn)
    movement.move(0, 150, 465)
    movement.move(10, 0, 29)
    movement.move(0, 50, 92)
    movement.move(10, 0, 35)
    movement.move(0, -50, 70)
    movement.move(20, 0, 30)
    movement.move(0, 150, 178)
    movement.move(0, -150, 90)
    ''''movement.move(10, 0, 20)
    movement.move(0, -150, 50)'''
    left_attachment.run_angle(340, 340, Stop.BRAKE, False)
    right_attachment.run_angle(340, 340, Stop.BRAKE, False)
    movement.move(-20, 0, 110)
    movement.move(0, -300, 400)
    movement.move(-10, 0, 15)
    movement.move(0, -300, 300)
    movement.move(50, 0, 45)
    movement.move(0, -150, 700)

class Mission9:
  def __init__(self):
    Mission9.run()
  def run():
    # movement.move(0, 500, 1000)
    movement.accelerate(0, 150, 0.01, 500, 10, False, False)
    print("following")
    line_follow = movement.lineFollow(True, 20, 9)
    line_follow = 38.213
    print("stopped")
    left_attachment.run_angle(300, 300, Stop.BRAKE, False)
    right_attachment.run_angle(300, 300, Stop.BRAKE, False)
    # angle_to_turn = 33.5 if (line_follow < 32) else 35 if (line_follow < 34) else 33.5
    #### angle_to_turn = -0.006 * line_follow ** 3 + 0.53 * line_follow ** 2 - 14.8* line_follow + 166
    angle_to_turn = 43
    # angle_to_turn = 32 if (0.6667*line_follow + 16.6667 < 32) else 39 if (0.6667*line_follow + 16.6667 > 39) else (0.6667*line_follow + 16.6667)
    # angle_to_turn = 0.0074074 * line_follow ** 2 +-0.174074 * line_follow + 33.51852
    # Working values: Value = 38.213, Turning = 39.57189919241802
    movement.move(0, 5, -9)
    movement.move(-10, 0, angle_to_turn)
    movement.move(0, 150, 465)
    movement.move(10, 0, 29.5)
    movement.move(0, 50, 110)
    left_attachment.run_angle(- 300, 205, Stop.BRAKE, False)
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
    value = 50
    value = 38
    movement.move(0, 50, 200)
    movement.move(-30, 0, value)
    
    movement.accelerate(0, 150, 0.001, 250, 7, False, False)
    movement.move(0, 150, 540)
    movement.accelerate(150, 0, 0.001, 300, 4, True, False)
    movement.accelerate(0, -150, 0.001, 150, 10, False, False)
    movement.move(0, -150, 1000)
  def red():
    # make it go a bit further.
    value = 35
    value = 22
    movement.move(-10, 0, value)
    movement.accelerate(0, 200, 0.001, 260, 7, False, False)
    movement.move(0, 200, 150)
    movement.accelerate(200, 0, 0.001, 300, 4, True, False)
    movement.accelerate(0, -200, 0.001, 150, 10, False, False)
    movement.move(0, -200, 600)
  def white():
    value = 61
    value = 48
    value = 52
    movement.move(10, 0, value)
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
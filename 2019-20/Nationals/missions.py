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

class Mission2_old:
  def __init__(self):
    Mission2.run()
  def run():
    movement.move(10, 0, 40)
    movement.move(0, 100, 430)
    movement.move(-10, 0, 40.9)
    movement.accelerate(0, 135, 0.01, 98.5, 10, False, False)
    movement.accelerate(135, 0, 0.01, 83, 10, True, False)
    resetAngles()
    wait(2200)
    angle_to_turn = 221.125
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

class Mission2:
  def __init__(self):
    Mission2.run()
  def run():
    movement.move(10, 0, 36)
    #movement.move(0, 200, 430)
    movement.accelerate(0, 200, 0.01, 400, 10, False, False)
    movement.move(-15, 0, 41.5)
    movement.accelerate(0, 135, 0.01, 100, 9, False, False)
    movement.accelerate(135, 0, 0.01, 81.9, 9, True, False)
    resetAngles()
    wait(2200)
    angle_to_turn = 221.125
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
    Mission9.run()
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
    angle_to_turn = 30
    # angle_to_turn = 32 if (0.6667*line_follow + 16.6667 < 32) else 39 if (0.6667*line_follow + 16.6667 > 39) else (0.6667*line_follow + 16.6667)
    # angle_to_turn = 0.0074074 * line_follow ** 2 +-0.174074 * line_follow + 33.51852
    # Working values: Value = 38.213, Turning = 39.57189919241802
    movement.move(-10, 0, angle_to_turn)
    movement.move(0, 150, 465)
    Drift = False
    Old = False
    if Old:
      movement.move(10, 0, 28)
      movement.move(0, 50, 93)
      movement.move(20, 0, 33)
    if not Old and Drift:
      left_attachment.run_angle(70, 70, Stop.BRAKE, False)
      right_attachment.run_angle(70, 70, Stop.BRAKE, False)
      movement.move(10, 0, 20)
      movement.move(0, 50, 93)
      movement.move(5, 0, 10)
      movement.move(0, -50, 50)
      movement.move(5, 0, 10)
      movement.move(0, 50, 50)
      movement.move(20, 0, 33)
    if not Old and not Drift:
      left_attachment.run_angle(70, 70, Stop.BRAKE, False)
      right_attachment.run_angle(70, 70, Stop.BRAKE, False)
      movement.move(10, 0, 12)
      movement.move(0, 50, 30)
      movement.move(14, 0, 14)
      movement.move(0, -50, 28)
      movement.move(10, 0, 7)
      movement.move(0, 50, 80)
      movement.move(20, 0, 30)

    movement.move(0, -50, 100)
    movement.move(20, 0, 30)
    movement.move(0, 150, 190)
    movement.move(0, -150, 100)
    '''movement.move(10, 0, 20)
    movement.move(0, -150, 50)'''
    left_attachment.run_angle(350, 350, Stop.BRAKE, False)
    right_attachment.run_angle(350, 350, Stop.BRAKE, False)
    if not Old and Drift:
      movement.move(-20, 0, 95)
    if not Old and not Drift:
      movement.move(-20, 0, 83.5)
    #movement.5accelerate(0, -300, 0.001, 150, 10, False, False)
    '''movement.move(0, -150, 150)
    movement.move(-20, 0, 30)
    movement.move(0, -150, 125)
    movement.move(20, 0, 40)
    movement.move(0, -300, 400)
    movement.move(20, 0, 30)
    movement.move(0, -300, 800)'''
    movement.move(0, -300, 600)
    movement.move(20, 0, 30)
    movement.move(0, -300, 1500)

class Mission9_old:
  def __init__(self):
    Mission9_old.run()
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

class Mission12: #Class to store the runs for Mission 12
  # All the following subroutines have similar structure to make it easier for us to debug and make changes. 
  def brown(): # Individual Mission 12 runs have been differentiated into different subroutines of the object.
    value = 50 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 38
    movement.move(0, 50, 200) # Using the move function we declared in movement as it is more accurate then ev3's movement.
    movement.move(-30, 0, value)
    movement.accelerate(0, 150, 0.001, 250, 7, False, False) # Function to accelerate/decelerate from x to y vel at z m/s^2
    movement.move(0, 150, 540)
    movement.accelerate(150, 0, 0.001, 292, 4, True, False) # Decelerating to allow greater control over the blocks and to allow a less change in delta v when stopping.
    movement.accelerate(0, -150, 0.001, 150, 10, False, False) 
    movement.move(0, -300, 1000)
  def red(): # Function to store the run of Mission 12, red. 
    # make it go a bit further.
    value = 35 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 21
    movement.move(-10, 0, value)
    movement.accelerate(0, 200, 0.001, 260, 7, False, False) # Running the function to accelerate from x vel to y vel at z m/s^2
    movement.move(0, 200, 150) # 0 steering, hence there is straight movement.
    movement.accelerate(200, 0, 0.001, 315, 4, True, False) # Decelerating back to 0, i.e. to the circle where they must be placed
    movement.accelerate(0, -200, 0.001, 150, 10, False, False) # Accelerating on the way back.
    movement.move(0, -300, 600) # Movement.move also allows for negative movement, i.e. backwards movement for Returning back to base
  def white():# Function to store the run of Mission 12, white. 
    value = 61 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 48
    value = 50
    movement.move(20, 0, value) # Movement.move taking the following input parameters (steering, speed, amount)
    movement.accelerate(0, 200, 0.001, 220, 7, False, False) # Accelerating to allow greater control over the blocks
    movement.accelerate(200, 0, 0.001, 210, 5, False, False) 
    movement.accelerate(0, -200, 0.001, 100, 10, False, False) # Accelerating back, allows for smooth movement, to not displace the blocks.
    movement.move(0, -300, 340)
  def blue(): # Function to store the run of Mission 12, blue. 
    movement.accelerate(0, 200, 0.001, 200, 7, False, False) # Accelerating to allow greater control over the blocks
    movement.accelerate(200, 0, 0.001, 200, 5, False, False) 
    movement.accelerate(0, -200, 0.001, 100, 10, False, False) 
    movement.move(0, -200, 300) # Movement.move also allows for negative movement, i.e. backwards movement for Returning back to base

left_attachment = Motor(Port.B, Direction.CLOCKWISE)
right_attachment = Motor(Port.C, Direction.COUNTERCLOCKWISE)

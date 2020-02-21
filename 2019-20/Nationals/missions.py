# Importing the required EV3 modules and libraries
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

import movement # Importing the movement script which contains function that we use for accurate movement around the board.

def resetAngles(): # Function to reset angles of both Medium Motors
  left_attachment.reset_angle(0)
  right_attachment.reset_angle(0)

class Mission1: # Class to contain the run for Mission 1 (Not run)
  def __init__(self): # Running the code when the class is called.
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

class Mission2: # Class to contain the run for Mission 2 (Probably not run)
  def __init__(self): # Running the code when the class is called.
    Mission2.run()
  def run(): # Function to store the code for the run of Mission 2
    movement.move(10, 0, 38) # Using movement.move as it is more accurate than EV3 move()
    #movement.move(0, 200, 430)
    movement.accelerate(0, 200, 0.01, 400, 10, False, False) # Accelerating in order to have greater control
    movement.move(-15, 0, 41.5)
    movement.accelerate(0, 135, 0.01, 100, 9, False, False)
    movement.accelerate(135, 0, 0.01, 83, 9, True, False)
    resetAngles()
    wait(2200)
    angle_to_turn = 221.125 # Soft-coded variables to make it easier to change movement values. 
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

class Mission9: # Class to contain the run for Mission 9
  def __init__(self): # Running the code when the class is called.
    Mission9.run()
  def run(): # Function to store the code for the run of Mission 9
    left_attachment.run_angle(30, 30, Stop.BRAKE, False) # Moving platform up a bit
    right_attachment.run_angle(30, 30, Stop.BRAKE, False)
    movement.accelerate(0, 150, 0.01, 500, 10, False, False)
    print("following") # Outputting the state of the robot to the console.
    line_follow = movement.lineFollow(True, 20, 9) # Line-following as it is more accurate than straight moving.
    line_follow = 38.213
    print("stopped") # Outputting the state of the robot to the console.
    angle_to_turn = 30
    movement.move(-10, 0, angle_to_turn) # Turns when line follow is done
    movement.move(0, 150, 465)
    Drift = False # Drift affects the direction of the bot
    if Drift:
      left_attachment.run_angle(70, 70, Stop.BRAKE, False) # Platform moves up so moment increases (m=fxd)
      right_attachment.run_angle(70, 70, Stop.BRAKE, False)
      movement.move(10, 0, 20)
      movement.move(0, 50, 93)
      movement.move(5, 0, 10) # Move middle beam
      movement.move(0, -50, 50)
      movement.move(5, 0, 10) # Move right beams
      movement.move(0, 50, 50)
      movement.move(20, 0, 33)
    if not Drift:
      left_attachment.run_angle(70, 70, Stop.BRAKE, False)
      right_attachment.run_angle(70, 70, Stop.BRAKE, False)
      movement.move(10, 0, 13)
      movement.move(0, 50, 30)
      movement.move(14, 0, 14) # Move middle beam
      movement.move(0, -50, 28)
      movement.move(10, 0, 7) # Move right beams
      movement.move(0, 50, 80)
      movement.move(20, 0, 30)

    movement.move(0, -50, 100)
    movement.move(20, 0, 30)
    movement.move(0, 150, 190) # Run into swings
    movement.move(0, -150, 100)
    left_attachment.run_angle(350, 350, Stop.BRAKE, False)
    right_attachment.run_angle(350, 350, Stop.BRAKE, False)
    # Pushing the house downwards & leftwards
    if Drift:
      movement.move(-20, 0, 95)
    if not Drift:
      movement.move(-20, 0, 83.5)
    movement.move(0, -500, 600) # Into traffic jam
    movement.move(20, 0, 30)
    movement.move(0, -1000, 5000) # Into base

class Mission12: #Class to store the runs for Mission 12
  # All the following subroutines have similar structure to make it easier for us to debug and make changes. 
  def brown(): # Individual Mission 12 runs have been differentiated into different subroutines of the object.
    value = 50 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 38
    movement.move(0, 50, 200) # Using the move function we declared in movement as it is more accurate then ev3's movement.
    movement.move(-30, 0, value)
    movement.accelerate(0, 150, 0.001, 250, 7, False, False) # Function to accelerate/decelerate from x to y vel at z mm/s^2
    movement.move(0, 150, 540)
    movement.accelerate(150, 0, 0.001, 292, 4, True, False) # Decelerating to allow greater control over the blocks and to allow a less change in delta v when stopping.
    movement.move(0, -300, 100)
    movement.move(30, 0, 30) # Turning to ensure fastest return to base
    movement.accelerate(0, -150, 0.001, 150, 10, False, False) 
    movement.move(0, -1000, 3000)
    movement.move(100, -300, 200) # Fitting into base

  def red(): # Function to store the run of Mission 12, red. 
    # make it go a bit further.
    value = 35 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 21
    movement.move(-10, 0, value)
    movement.accelerate(0, 200, 0.001, 260, 7, False, False) # Running the function to accelerate from x vel to y vel at z mm/s^2
    movement.move(0, 200, 150) # 0 steering, hence there is straight movement.
    movement.accelerate(200, 0, 0.001, 315, 4, True, False) # Decelerating back to 0, i.e. to the circle where they must be placed
    movement.accelerate(0, -200, 0.001, 150, 10, False, False) # Accelerating on the way back.
    movement.move(0, -1000, 3000) # Movement.move also allows for negative movement, i.e. backwards movement for Returning back to base
  def white():# Function to store the run of Mission 12, white. 
    value = 61 # Value to store the turning amount, soft-coded to make it easier to change values.
    value = 48
    value = 50
    movement.move(20, 0, value) # Movement.move taking the following input parameters (steering, speed, amount)
    movement.accelerate(0, 200, 0.001, 220, 7, False, False) # Accelerating to allow greater control over the blocks
    movement.accelerate(200, 0, 0.001, 210, 5, False, False) 
    movement.accelerate(0, -200, 0.001, 100, 10, False, False) # Accelerating back, allows for smooth movement, to not displace the blocks.
    movement.move(0, -1000, 3000)
  def blue(): # Function to store the run of Mission 12, blue. 
    movement.accelerate(0, 200, 0.001, 200, 7, False, False) # Accelerating to allow greater control over the blocks
    movement.accelerate(200, 0, 0.001, 200, 5, False, False) 
    movement.move(0, -1000, 300) # Movement.move also allows for negative movement, i.e. backwards movement for Returning back to base
    movement.move(30, 0, 80)
    movement.move(0, -1000, 1500)

left_attachment = Motor(Port.B, Direction.CLOCKWISE)
right_attachment = Motor(Port.C, Direction.COUNTERCLOCKWISE)

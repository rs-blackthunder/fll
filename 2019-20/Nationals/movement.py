#!/usr/bin/env pybricks-micropython

# Importing the required EV3 modules and libraries
# from pybricks import ev3brick as brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.ev3devices import (Motor, ColorSensor)
# from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def angleToDistance(angle): # Function that returns the distance when the wheels are moved by x degrees
  return angle / 360 * 196.035381584 # Diameter of the wheels.

def distanceToAngle(distance): # Function that returns the angle by which the wheels need to be moved to move x mm
  return distance * 360 / 196.035381584 # Diameter of the wheels.

def resetAngles(): # Resets the angles of both Large motors to 0
  left_motor.reset_angle(0)
  right_motor.reset_angle(0)

def accelerate(start_power, final_power, delay, distance, speed_increment, stop: bool, correct: bool): # Function to accelerate/decelerate from x vel to y vel at z mm/s^2
  resetAngles() # Resetting the angles
  current_power = start_power # Assigning the current power to the start power given as a parameter.
  if speed_increment == 0: # If no speed increment is given or speed increment is 0
    speed_increment = abs(final_power - start_power) / distance * 8 # Assigning the speed increment to be the different of powers divided by the distance.
  resetAngles() # reset angle rotations
  # get desired direction
  try:
    direction_coefficient = final_power / abs(final_power)
  except ZeroDivisionError:
    direction_coefficient = start_power / abs(start_power)
  # while power is less than final power
  while (abs(current_power) < abs(final_power) if abs(current_power) <= abs(final_power) else abs(current_power) > abs(final_power)):
    # move in desired direction at increasing power
    robot.drive(current_power, 0)
    # increment speed
    if ((abs(start_power) <= abs(final_power)) or (abs(start_power) > abs(final_power) and abs(current_power) > 20)):
      print("speed increment:", str(speed_increment), "increase:", speed_increment * direction_coefficient * (1  if abs(current_power) <= abs(final_power) else -1))
      current_power += (speed_increment * direction_coefficient * (1  if abs(current_power) <= abs(final_power) else -1))
    # display current movement stats
    print("moving, power", str(current_power), "left rotations", str(left_motor.angle()), "right rotations", str(right_motor.angle()), "left distance", str(angleToDistance(left_motor.angle())), "right distance", str(angleToDistance(right_motor.angle())), "continue?", (angleToDistance(abs(left_motor.angle())) < distance))
    # wait for specified delay before changing power again
    wait(delay)
    # if desired distance reached, stop increasing power
    if ((abs(angleToDistance(left_motor.angle())) >= distance) or (angleToDistance(abs(right_motor.angle())) >= distance)):
      break
  # keep moving until desired distance reached
  while not ((angleToDistance(abs(left_motor.angle())) >= distance) or (angleToDistance(abs(right_motor.angle())) >= distance)):
    wait(delay)
  # if braking desired
  if stop:
    # brake
    robot.stop(Stop.HOLD)
    # if angle correction required
    if correct:
      # correct angle (making robot face correct direction)
      correctRotation(distance)

def move(steering, speed, amount): # A function to move the robot when steering, speed and amount is given.
  # speed is in mm/s and steering is in degrees/s so time can be calculated
  # reset motor rotations
  resetAngles()
  # if not turning on spot
  if speed != 0:
    # set time to move until desired distance is reached, where amount is a distance in mm
    time = abs(amount / speed * 1000)
  # if turning on spot
  else:
    # set time to move until desired angle is reached, where amount is a distance in degrees
    time = abs(amount / steering * 1000)
  # move for specified time to reach target distance/angle
  robot.drive_time(speed, steering, time)
  # display movement stats
  print("moved, left", left_motor.angle(), "right", right_motor.angle())

def correctRotation(distance): # Function to make sure there is straight movement.
  # The function realligns the robot depending on the rotations the two motors have completed.
  # work out how many degrees need to be moved on each motor
  left_motor_degrees_remaining = abs(left_motor.angle()) - distanceToAngle(distance)
  right_motor_degrees_remaining = abs(right_motor.angle()) - distanceToAngle(distance)
  print("left motor degrees remaining:", str(left_motor_degrees_remaining)) # Displaying the degrees remaining to the console.
  print("right motor degrees remaining:", str(right_motor_degrees_remaining))
  # if motor needs to move
  if (left_motor_degrees_remaining != 0):
    # reset motor rotations
    left_motor.reset_angle(0)
    # move motor required number of degrees
    left_motor.run_angle(5, left_motor_degrees_remaining, Stop.HOLD)
  # if motor needs to move
  if (right_motor_degrees_remaining != 0):
    # reset motor rotations
    right_motor.reset_angle(0)
    # move motor required number of degrees
    right_motor.run_angle(5, right_motor_degrees_remaining, Stop.HOLD)

def lineFollow(forward: bool, threshold, caller: int): # Function to make the robot follow any line with the robot's two downfacing sensors.
  # Assinging variables that are used in the code below.
  # Soft-coding variables makes it easier to change in the future
  speed = 50 if forward else -50 # Speed at which the robot travels.
  error = 0
  last_error = 0
  integral = 0
  derivative = 0
  kp = 0.6
  ki = 0.02

  kd = 0.001
  perfect_steering = 0
  resetAngles()
  
  # run until break
  while True:
    error = left_colour_sensor.reflection() - right_colour_sensor.reflection() # Getting the difference in reflection of the two colour sensors.
    # work out total error
    integral += error
    # predict next error
    derivative = error - last_error
    # work out amount to steer
    steering = error * kp + integral * ki + derivative * kd
    # if turning value is below threshold, increase count of number of times this has happened
    if (threshold != 0 and -2 < steering < 2 and caller != 9):
      perfect_steering += 1
      # if maximum required number of times required reached, stop line following
      if (threshold <= perfect_steering):
        break
    else:
      # move robot
      robot.drive(speed, steering)
    # if called from mission 9 (beams), robot has moved 600 degrees of motor rotation and steering value is above threshold
    if (caller == 9 and left_motor.angle() > 600 and steering >= threshold):
      # print steering stats
      print("POSITION 1, steering", steering)
      # reset motor rotations
      resetAngles()
      # stop line following
      break
    # store last error
    last_error = error
  # brake
  robot.stop(Stop.HOLD)
  # return final steering value
  return steering

# Assinging the modules of the Robot. 
# Two Large Motors.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE) # Ports and direction of motion are given as parameters.
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
# The Robot DriveBase
robot = DriveBase(left_motor, right_motor, 62.4, 96.5) # The two motors and ... are given as parameters. 
# The two downward facing colour sensors.
left_colour_sensor = ColorSensor(Port.S1) # Ports of the sensors are given as a parameter.
right_colour_sensor = ColorSensor(Port.S2)

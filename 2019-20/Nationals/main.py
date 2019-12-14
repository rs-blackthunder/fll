#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def accelerate(start_power: int, final_power: int, delay: int, distance: int):
  current_power = start_power
  left_motor.reset_angle(0)
  right_motor.reset_angle(0)
  try:
    direction_coefficient = final_power / abs(final_power)
  except:
    direction_coefficient = start_power / abs(start_power)
  while (abs(current_power) < abs(final_power) if abs(current_power) <= abs(final_power) else abs(current_power) > abs(final_power)):
    robot.drive(current_power, 0)
    if ((abs(start_power) <= abs(final_power)) or (abs(start_power) > abs(final_power) and abs(current_power) > 20)):
      try:
        current_power += (3 * direction_coefficient * 1  if abs(current_power) <= abs(final_power) else -1)
      except:
        current_power += (3 * direction_coefficient * 1  if abs(current_power) <= abs(final_power) else -1)
    print("moving, power", str(current_power), "left rotations", str(left_motor.angle()), "right rotations", str(right_motor.angle()), "left distance", str(left_motor.angle() / 360 * 196.035381584), "right distance", str(right_motor.angle() / 360 * 196.035381584), "continue?", (abs(left_motor.angle()) / 360 * 196.035381584 < distance))
    wait(delay)
    if ((abs(left_motor.angle()) / 360 * 196.035381584 >= distance) or (abs(right_motor.angle()) / 360 * 196.035381584 >= distance)):
      break
  while not ((abs(left_motor.angle()) / 360 * 196.035381584 >= distance) or (abs(right_motor.angle()) / 360 * 196.035381584 >= distance)):
    wait(delay)
  robot.stop(Stop.BRAKE)
  left_motor_rotations_remaining = abs(left_motor.angle()) - (distance * 360 / 196.035381584)
  right_motor_rotations_remaining = abs(right_motor.angle()) - (distance * 360 / 196.035381584)
  print("left motor rotations remaining:", str(left_motor_rotations_remaining))
  print("right motor rotations remaining:", str(right_motor_rotations_remaining))
  if (left_motor_rotations_remaining != 0):
    left_motor.reset_angle(0)
    left_motor.run_angle(5, left_motor_rotations_remaining)
  elif (right_motor_rotations_remaining != 0):
    right_motor.reset_angle(0)
    right_motor.run_angle(5, right_motor_rotations_remaining)


# initialise motors
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, 62.4, 96.5)

# test beeps
# brick.sound.beep(1500, 500, 50)
# brick.sound.beep(750, 500, 50)

# check current
if brick.battery.current() < 150:
  brick.sound.beep(1500, 1000, 50)
if brick.battery.voltage() < 7000:
  brick.sound.beep(750, 1000, 50)
print(str(brick.battery.current()) + "mA")
print(str(brick.battery.voltage()) + "mV")

# robot.drive_time(150,0,2000)
# robot.drive_time(0, 50, 7200)
accelerate(150, 0, 0.001, 600)
wait(1000)
accelerate(0, -150, 0.001, 600)
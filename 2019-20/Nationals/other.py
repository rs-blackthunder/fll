"""
Code that is not needed anymore

Main.py

# A better way to select missions than the colour sensor that may not work in different environments.
selecting = True

while selecting:
  while not (any(brick.buttons())):
    wait(10)
  if Button.UP in brick.buttons():
    print("Mission 2")
    missions.Mission2()
  elif Button.RIGHT in brick.buttons():
    print("Mission 6/7/9")
    missions.Mission9_2()
  elif Button.DOWN in brick.buttons():
    while not (any(brick.buttons())):
      wait(10)
    if Button.UP in brick.buttons():
      print("Mission 8 + Mission12_brown")
      missions.Mission12.brown()
      break
    elif Button.RIGHT in brick.buttons():
      print("Mission 12_blue")
      missions.Mission12.blue()
    elif Button.DOWN in brick.buttons():
      print("Mission 12_white")
      missions.Mission12.white()
    elif Button.LEFT in brick.buttons():
      print("Mission 12_red")
      missions.Mission12.red()
    elif Button.MIDDLE in brick.buttons():
      break
  elif Button.RIGHT in brick.buttons():
    print("Mission 1")
  elif Button.MIDDLE in brick.buttons():
    selecting = False

"""


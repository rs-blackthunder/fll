class Mission12:
  def brown(self):
    movement.accelerate(0, 200, 0.001, 400, 5, False, False)
    movement.accelerate(200, 0, 0.001, 400, 5, True, True)
    movement.accelerate(0, -200, 0.001, 330, 5, True, False)
    movement.move(300, -300, 100, True, False)
    movement.move(0, -100, 200, True, False)
# sys
import sys
sys.path.append('..')

# math
import math

# matplotlib
import matplotlib.pyplot as plt

# robot
from robot import Robot, Body


if __name__ == '__main__':
  # root
  b1 = Body('root', 0, 0, 0)

  # right leg
  # femur
  b2 = Body('right femur', 0, 1, -3 * math.pi / 4., b1)
  # tibia
  b3 = Body('right tibia', 0, 0.7, -math.pi / 4., b2)

  # left leg
  # femur
  b4 = Body('left femur', 0, 1, 3 * math.pi / 4., b1)
  # tibia
  b5 = Body('left tibia', 0, 0.7, math.pi / 4., b4)

  # torso
  b6 = Body('torso', 0, 2, 0.1, b1)

  r = Robot()
  r.setRoot(b1)


  print b3.jacobian
  b1.q = 0.1
  b1.q = 0.
  print b3.jacobian

  l = r.getLines()
  plt.plot(*l)
  plt.show()


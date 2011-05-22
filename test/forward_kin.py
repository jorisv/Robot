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
  # head
  b1 = Body(0, 0, 0)

  # right leg
  # femur
  b2 = Body(0, 1, -3 * math.pi / 4., b1)
  # tibia
  b3 = Body(0, 0.7, -math.pi / 4., b2)

  # left leg
  # femur
  b4 = Body(0, 1, 3 * math.pi / 4., b1)
  # tibia
  b5 = Body(0, 0.7, math.pi / 4., b4)

  # torso
  b6 = Body(0, 2, 0.1, b1)

  r = Robot()
  r._root = b1

  l = r.getLines()
  print l

  print b3.jacobian()

  plt.plot(*l)
  plt.show()


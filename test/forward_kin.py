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
  b1 = Body(0, 0, 0)

  b2 = Body(0, 1, -3 * math.pi / 4., b1)
  b3 = Body(0, 1, 3 * math.pi / 4., b1)

  b4 = Body(0, 1, 0.5, b1)

  r = Robot()
  r._root = b1

  l = r.getLines()
  print l

  plt.plot(*l)
  plt.show()


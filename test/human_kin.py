# sys
import sys
sys.path.append('..')

# matplotlib
import matplotlib.pyplot as plt

# robot
from robot import Robot, human_maker


if __name__ == '__main__':
  root = human_maker.makeProportionalHuman(1.75)

  r = Robot()
  r.setRoot(root)

  l = r.getLines()
  plt.plot(*l)
  plt.show()


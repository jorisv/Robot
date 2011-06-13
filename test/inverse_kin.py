# sys
import sys
sys.path.append('..')

# math
import math

# matplotlib
import matplotlib.pyplot as plt

# robot
from robot import Robot, Body
from robot import Line
from robot import ContactConstraint
from robot import InverseKinematics


if __name__ == '__main__':
  # root
  b1 = Body('root', 0, 0, 0, fixed=False)

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

  line1 = Line(2+0.0, -1.5, 2+1.5, -1)
  line2 = Line(2+-1.0, -1.5, 2+-0.1, -1)

  c1 = ContactConstraint(b3, line1, 0.5)
  c2 = ContactConstraint(b5, line2, 0.5)

  ik = InverseKinematics(r)
  ik.addConstraint(c1)
  ik.addConstraint(c2)
  ik.solve()

  l = r.getLines() + line1.getLines() + line2.getLines()
  plt.plot(*l)
  plt.show()


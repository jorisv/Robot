#math
import numpy as np

#robot
from body import Body
from transform2d import Transform2D


class Robot(object):
  def __init__(self):
    self._bodies = []
    self._root = None

  def setBodies(self, bodies):
    self._bodies = bodies

  def getLines(self):
    return self._getLines(self._root)

  def _getLines(self, body):
    lines = []
    if body:
      bt = body.globalTransform()
      for b in body.post:
        bbt = b.globalTransform()
        lines += [[bt.x, bbt.x], [bt.y, bbt.y]]
        lines += self._getLines(b)
    return lines



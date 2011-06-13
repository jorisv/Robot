# math
import numpy as np

class Line(object):
  def __init__(self, x0, y0, x1, y1):
    vec = np.mat([[x1 - x0],
                  [y1 - y0]])

    self.length = np.linalg.norm(vec)
    self.vec = vec / self.length

    self.p0 = np.mat([x0, y0]).T
    self.p1 = np.mat([x1, y1]).T
    self.norm = np.mat([[-vec[1,0]], [vec[0,0]]])

  def pointAt(self, p):
    return self.p0 + self.vec * self.length * p

  def getLines(self):
    return zip(self.p0.__array__().tolist(),
               self.p1.__array__().tolist())


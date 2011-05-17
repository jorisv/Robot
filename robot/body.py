
#robot
from transform2d import Transform2D

class Body(object):
  def __init__(self, x, y, q, previousBody=None):
    self._x = x
    self._y = y
    self._q = q

    self._transform = None
    self._globalTransform = None
    self._dirty = True

    self._pre = previousBody
    self._post = []
    if self.pre is not None:
      self._pre._post.append(self)

  def isRoot(self):
    return self._pre is None

  @property
  def q(self):
    return self._q

  @q.setter
  def q(self, val):
    self._q = val
    self._dirty = True

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @property
  def pre(self):
    return self._pre

  @property
  def post(self):
    return self._post

  def globalTransform(self):
    if self._dirty:
      self._transform = Transform2D(0, 0, self._q) * Transform2D(self._x, self._y, 0)
      if self.isRoot():
        self._globalTransform = self._transform
      else:
        self._globalTransform = self._pre.globalTransform() * self._transform
      self._dirty = False
    return self._globalTransform


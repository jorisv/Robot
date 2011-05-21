
#robot
from transform2d import Transform2D

class Body(object):
  def __init__(self, x, y, q, previousBody=None):
    self._x = x
    self._y = y
    self._q = q

    self._transform = None
    self._globalTransform = None
    self._dirtyLocal = True
    self._dirtyGlobal = True

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
    self._dirty()

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x
    self._dirty()

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self._y = y
    self._dirty()

  @property
  def pre(self):
    return self._pre

  @property
  def post(self):
    return self._post

  def globalTransform(self):
    if self._dirtyLocal:
      self._transform = Transform2D(0, 0, self._q) * Transform2D(self._x, self._y, 0)
      self._dirtyLocal = False
    if self._dirtyGlobal:
      if self.isRoot():
        self._globalTransform = self._transform
      else:
        self._globalTransform = self._pre.globalTransform() * self._transform
      self._dirtyGlobal = False
    return self._globalTransform

  def isDirty(self):
    return self._dirtyGlobal or self.dirtyLocal

  def _dirty(self):
    self._dirtyGlobal = True
    self._dirtyLocal = True
    for b in self._post:
      if b.isDirty():
        b.dirty()


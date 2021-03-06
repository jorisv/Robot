#math
import math
import numpy.matlib

#robot
from transform2d import Transform2D

class Body(object):
  def __init__(self, name, x, y, q, previousBody=None, fixed=False):
    self.name = name

    self._fixed = fixed
    self._x = x
    self._y = y
    self._q = q

    self.id = None

    self._transform = None
    self._dirtyLocal = True
    self._globalTransform = None
    self._dirtyGlobal = True

    self._pre = previousBody
    self._post = []
    self._rootPath = [self]
    self._mobileRootPath = [] if fixed else [self]
    self._nbMobile = 0 if fixed else 3

    if self._pre is not None:
      self._pre._post.append(self)
      self._rootPath = self._pre._rootPath + [self]
      self._mobileRootPath = self._pre._mobileRootPath + [self]
      self._nbMobile = (0 if fixed else 1) + self._pre._nbMobile

    self._jacob = numpy.matlib.zeros((2, self._nbMobile))
    self._dirtyJacob = True


  def isRoot(self):
    return self._pre is None

  def hasFixedRoot(self):
    return self._rootPath[0].fixed

  def children(self):
    child = self._post[:]
    for b in self._post:
      child += b.children()
    return child

  def varsCount(self):
    return self._nbMobile

  @property
  def fixed(self):
    return self._fixed

  @property
  def rootPath(self):
    return self._rootPath

  @property
  def mobileRootPath(self):
    return self._mobileRootPath

  @property
  def q(self):
    return self._q

  @q.setter
  def q(self, q):
    if q != self._q:
      self._q = q
      self._dirtyAll()

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    if x != self._x:
      self._x = x
      self._dirtyAll()

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    if y != self._y:
      self._y = y
      self._dirtyAll()

  @property
  def pre(self):
    return self._pre

  @property
  def post(self):
    return self._post

  @property
  def globalTransform(self):
    if self._dirtyGlobal:
      if self.isRoot():
        self._globalTransform = self.transform
      else:
        self._globalTransform = self._pre.globalTransform * self.transform
      self._dirtyGlobal = False
    return self._globalTransform

  @property
  def transform(self):
    if self._dirtyLocal:
      self._transform = Transform2D(0, 0, self._q) * Transform2D(self._x, self._y, 0)
      self._dirtyLocal = False
    return self._transform

  @property
  def jacobian(self):
    if self._dirtyJacob:
      nbBody = len(self._rootPath)
      revGlobalTrans = Transform2D()

      curJac = self._nbMobile - 1
      for i in range(nbBody - 1, 0, -1):
        curQ = self._rootPath[i]
        if not curQ.fixed:
          curD = curQ.pre.globalTransform *\
                 curQ.transform.thetaDerivated() * Transform2D(curQ.x, curQ.y, 0.) *\
                 revGlobalTrans
          self._jacob[:,curJac] = [[curD.x],[curD.y]]
          curJac -= 1
        revGlobalTrans = curQ.transform * revGlobalTrans

      curQ = self._rootPath[0]
      if not curQ.fixed:
        ct = math.cos(curQ.q)
        st = math.sin(curQ.q)
        curD = curQ.transform.thetaDerivated() * Transform2D(curQ.x, curQ.y, 0.) *\
               revGlobalTrans
        self._jacob[:,0] = [[ct],[st]] # dx
        self._jacob[:,1] = [[-st],[ct]] # dy
        self._jacob[:,2] = [[curD.x],[curD.y]] # dq

      self._dirtyJacob = False

    return self._jacob

  def isDirty(self):
    return self._dirtyGlobal or self._dirtyLocal or self._dirtyJacob

  def _dirtyAll(self):
    self._dirtyGlobal = True
    self._dirtyLocal = True
    self._dirtyJacob = True
    for b in self._post:
      if not b._dirtyGlobal or not b._dirtyLocal or not b._dirtyJacob:
        b._dirtyAll()


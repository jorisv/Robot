# math
import math
import numpy as np
import numpy.matlib

class Transform2D(np.matrix):
  def __new__(cls, *args):
    if len(args) == 3:
      x = args[0]
      y = args[1]
      theta = args[2]
      ct = math.cos(theta)
      st = math.sin(theta)
      mat = np.matrix([[ct, -st, x],
                       [st, ct, y],
                       [0., 0., 1.]])
    elif len(args) == 1 and isinstance(args[0], np.matrix) and args[0].shape == (3, 3):
      mat = args[0]
    elif len(args) == 0:
      mat = numpy.matlib.eye(3)
    else:
      raise TypeError("Bad arguments")

    mat.__class__ = Transform2D
    return mat

  @property
  def x(self):
    return self[0,2]

  @property
  def y(self):
    return self[1,2]

  @staticmethod
  def derivate(theta):
    ct = math.cos(theta)
    st = math.sin(theta)
    mat = np.matrix([[-st, -ct, 0.],
                     [ct, -st, 0.],
                     [0., 0., 0.]])
    return Transform2D(mat)



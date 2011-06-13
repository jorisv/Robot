
# math
import math
import numpy as np

# opt
import pyipopt

class InverseKinematics(object):
  def __init__(self, robot):
    self._robot = robot
    self._constraint = []

  def addConstraint(self, constraint):
    self._constraint.append(constraint)

  def solve(self):
    x0 = self._robot.configuration()
    nbVar = len(x0)

    xL = [-math.pi] * nbVar
    xU = [math.pi] * nbVar
    cL = []
    cU = []
    nCon = 0
    nnzH = 0
    ssR = []
    ssC = []

    for c in self._constraint:
      cL.append(c.lBounds())
      cU.append(c.uBounds())
      ss = c.sparseStruct()
      ssR += (np.array(ss[0]) + nCon).tolist()
      ssC += ss[1]
      nCon += c.constraintCount()

    ss = (np.array(ssR), np.array(ssC))
    nnzJ = len(ssC)

    def evalF(x, user=None):
      self._robot.configure(x)
      return 0.0

    def evalFJ(x, user=None):
      self._robot.configure(x)
      return np.zeros(nbVar)

    def evalC(x, user=None):
      self._robot.configure(x)
      l = []
      for c in self._constraint:
        l += c.eval(x)

      return np.array(l)

    def evalCJ(x, flag, user=None):
      if flag:
        return ss
      else:
        l = []
        for c in self._constraint:
          l += c.evalJ(x)

        return np.array(l)


    opt = pyipopt.create(nbVar, np.array(xL), np.array(xU),
                         nCon, np.array(cL), np.array(cU),
                         nnzJ, nnzH, evalF, evalFJ, evalC, evalCJ)

    x, zl, zu, obj, status = opt.solve(np.array(x0))
    opt.close()


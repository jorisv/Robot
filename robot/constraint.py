
class Constraint(object):

  def uBounds(self):
    raise NotImplementedError("uBounds is not implemented")

  def lBounds(self):
    raise NotImplementedError("lBounds is not implemented")

  def constraintCount(self):
    raise NotImplementedError("constraintCount is not implemented")

  def sparseStruct(self):
    raise NotImplementedError("sparseStruct is not implemented")

  def eval(self, x):
    raise NotImplementedError("eval is not implemented")

  def evalJ(self, x):
    raise NotImplementedError("evalJ is not implemented")


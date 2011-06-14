
class ContactConstraint(object):

  def __init__(self, body, line, lineP):
    self._body = body
    self._point = line.pointAt(lineP)
    self._pointN = line.norm
    self._nbQ = body.varsCount()
    self._nbJQ = self._nbQ * 2

  def uBounds(self):
    return [0., 0.]

  def lBounds(self):
    return [0., 0.]

  def constraintCount(self):
    return 2

  def sparseStruct(self):
    sparse = [] if self._body.hasFixedRoot() else [0, 1]
    sparse += [b.id for b in self._body.mobileRootPath]

    return ([0] * self._nbQ + [1] * self._nbQ, sparse + sparse)

  def eval(self, x):
    return [self._body.globalTransform.x - self._point[0,0],
            self._body.globalTransform.y - self._point[1,0]]

  def evalJ(self, x):
    return self._body.jacobian.__array__().reshape((self._nbJQ,)).tolist()



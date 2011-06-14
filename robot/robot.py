
class Robot(object):
  def __init__(self):
    self._bodies = []
    self._mobileBodies = []
    self._nbMobileBodies = 0
    self._root = None

  def setRoot(self, root):
    self._root = root
    self._bodies = [root] + root.children()
    self._mobileBodies = []
    self._nbMobileBodies = 0

    i = 0 if self._root.fixed else 2

    for b in self._bodies:
      if not b.fixed:
        b.id = i
        self._mobileBodies.append(b)
        i += 1

    self._nbMobileBodies = i

  def bodieCount(self):
    return len(self._bodies)

  def mobileBodieCount(self):
    return self._nbMobileBodies

  def getLines(self):
    return self._getLines(self._root)

  def configure(self, x):
    beg = 0
    if not self._root.fixed:
      self._root.x = x[0]
      self._root.y = x[1]
      beg = 2

    for b, q in zip(self._mobileBodies, x[beg:]):
      b.q = q

  def configuration(self):
    xyC = [] if self._root.fixed else [self._root.x, self._root.y]

    return xyC + [b.q for b in self._mobileBodies]

  def _getLines(self, body):
    lines = []
    if body:
      bt = body.globalTransform
      for b in body.post:
        bbt = b.globalTransform
        lines += [[bt.x, bbt.x], [bt.y, bbt.y]]
        lines += self._getLines(b)
    return lines



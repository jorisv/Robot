
class Robot(object):
  def __init__(self):
    self._bodies = []
    self._root = None

  def setRoot(self, root):
    self._root = root
    self._bodies = [root] + root.children()
    for i, b in enumerate(self._bodies):
      b.id = i

  def bodieCount(self):
    return len(self._bodies)

  def getLines(self):
    return self._getLines(self._root)

  def configure(self, x):
    for b, q in zip(self._bodies, x):
      b.q = q

  def configuration(self):
    return [b.q for b in self._bodies]

  def _getLines(self, body):
    lines = []
    if body:
      bt = body.globalTransform
      for b in body.post:
        bbt = b.globalTransform
        lines += [[bt.x, bbt.x], [bt.y, bbt.y]]
        lines += self._getLines(b)
    return lines



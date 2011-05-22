import math
import sympy as sp

def makeTransMat(x, y, q):
  m0 = sp.matrices.Matrix([[sp.cos(q), -sp.sin(q), 0.],
                           [sp.sin(q), sp.cos(q), 0.],
                           [0., 0., 1.]])

  m1 = sp.matrices.Matrix([[1., 0., x],
                           [0., 1., y],
                           [0., 0., 1.]])
  return m0 * m1

def eval(func, x, y, q, xv, yv, qv):
  return func.subs(x[0], xv[0]).subs(y[0], yv[0]).subs(q[0], qv[0]).\
              subs(x[1], xv[1]).subs(y[1], yv[1]).subs(q[1], qv[1]).\
              subs(x[2], xv[2]).subs(y[2], yv[2]).subs(q[2], qv[2]).\
              evalf()


if __name__ == '__main__':
  x0 = sp.Symbol('x0')
  y0 = sp.Symbol('y0')
  q0 = sp.Symbol('q0')

  x1 = sp.Symbol('x1')
  y1 = sp.Symbol('y1')
  q1 = sp.Symbol('q1')

  x2 = sp.Symbol('x2')
  y2 = sp.Symbol('y2')
  q2 = sp.Symbol('q2')

  x = [x0, x1, x2]
  y = [y0, y1, y2]
  q = [q0, q1, q2]

  xv = [0., 0., 0.]
  yv = [0., 1., 0.7]
  qv = [0., -3. * math.pi / 4., -math.pi / 4.]

  m0 = makeTransMat(x0, y0, q0)
  m1 = makeTransMat(x1, y1, q1)
  m2 = makeTransMat(x2, y2, q2)

  m = m0 * m1 * m2

  print m
  print

  print m.diff(q0)[2]
  print m.diff(q0)[5]
  print

  print m.diff(q1)[2]
  print m.diff(q1)[5]
  print

  print m.diff(q2)[2]
  print m.diff(q2)[5]
  print

  print eval(m.diff(q0)[2], x, y, q, xv, yv, qv)
  print eval(m.diff(q0)[5], x, y, q, xv, yv, qv)
  print

  print eval(m.diff(q1)[2], x, y, q, xv, yv, qv)
  print eval(m.diff(q1)[5], x, y, q, xv, yv, qv)
  print

  print eval(m.diff(q2)[2], x, y, q, xv, yv, qv)
  print eval(m.diff(q2)[5], x, y, q, xv, yv, qv)


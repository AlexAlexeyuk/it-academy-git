import random
from sympy import Symbol, symbols
'''dct_for_val = {var: random.randint(2, 5) for var in variables}'''
'''def deriv( h = .01):
  x, y, z = (random.randint(1, 5) for _ in range(3))
  dx = (f(x + h, y, z) - f(x, y, z)) / h
  dy = (f(x, y + h, z) - f(x, y, z)) / h
  dz = (f(x, y, z + h) - f(x, y, z)) / h
  lambda_ = .01
  for i in range(10000):
    x = x - lambda_ * dx
    y = y - lambda_ * dy
    z = z - lambda_ * dz
  return dx, dy, dz, x, y, z
print(deriv())'''

def f (x, y, z):
    return x, y, z
t = Symbol('a, b, c')
print(t)
t = (random.randint(1, 5) for var in range(3))
print(t)
dct = {str(var): random.randint(1, 5) for var in t}
for i in t:
    i = dct.pop(i)
"""l = []
    for i in dct_for_val:
        di = dct_for_val[i] + h
        l.append(di)
    return (f(l.pop(0), dct_for_val[variabl[1]], dct_for_val[variabl[2]]) - f(dct_for_val.values())) / h
        """

def some_func(*lis):
    lis = Symbol('x y z')
    print(x, y, z)
params = ['a', 3.4, None]
some_func(*params)


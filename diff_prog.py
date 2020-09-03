from sympy import diff, symbols
x, y, z = symbols('x y z')
def F(x, y, z):
  return x ** (y + z)
## поиск производной аналитически

print(diff(x ** (y + z), x, y, z))



import numpy as np
a = np.linspace(1, 3/2, 100)
print(a)

for i in range(1000):
  lambda = 1 / min(i + 1, 100)
  x -=  lmd*np.sign(df(x))
  
  
  
from sympy import Symbol
import sys
lst = []
for i in ('x', 'y', 'z', 'b'):
  lst.append(Symbol(i))

print(lst)

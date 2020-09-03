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



from numpy import sin, cos, arange, linspace, pi, zeros
import scipy.optimize as opt    

def dG(thetaf, psi, gamma):
    return 0.35*(cos(psi))**2*(2*sin(3*thetaf/2+2*gamma)+(1+4*sin(gamma)**2)*sin(thetaf/2)-sin(3*thetaf/2))+sin(psi)**2*sin(thetaf/2)    

nt = 100 
np = 100 
gamma = linspace(0, pi/2, nt) 
psi = linspace(0, pi/2, np) 
x = zeros((nt, np)) 
for i, theta in enumerate(gamma):
    for j, phi in enumerate(psi):
        print('i = %d, j = %d') %(i, j) 
        g = lambda thetaf: dG(thetaf,phi,theta) 
        x[i,j] = opt.brenth(g,-pi/2,pi/2)

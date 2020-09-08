from sympy import Symbol, symbols, diff
import numpy as np
import random
import math
from math import e, pi, log, sin, cos


def determ_amount_var():
  """ Функция.
  
  возвращает количество пременных во введённой функции
  """
  global function
  function = input('Введите функцию:F(): ')
  dct = {}
  fun = ''
  list_of_var = []
  for i in function: # убираем e, т.к. знаем, что это не переменная
    if i.isalpha():
      fun = fun + i # формируем строку с вероятными синволами
    fun = fun.replace('log', '').replace('cos', '').replace('sin', '').\
    replace('e', '').replace('pi', '')#убираем разного рода функции и константы
  for i in fun:
    dct[i] = dct.get(i, 0) + 1 # делаем словарь с ключами, чтобы получить только уникальные ключи
  for i in dct.keys():
    list_of_var.append(Symbol(i))  # формируем список символов
  return tuple(list_of_var)


# x ** 2 + y ** 3 + z ** 4
# x ** 2 - y ** 3
# 10 * x ** 2 + y ** 2
variables = determ_amount_var()
print('Внесите в аргументы искомой функции f{0}'.format(variables)) # просим человека внести аргументы функции


def f(x, y, z):
    return eval(function)


def derivative(h = .0001):
    lst = []
    for i in range(len(variables)):
        lst_of_values  =  [4 for i in range(len(variables))]
        lst_of_values[i] = lst_of_values[i] + h 
        lst.append(f(*lst_of_values))
    lst_of_values  =  [4 for i in range(len(variables))]
    return  np.array([(np.array(lst) - np.array([f(*lst_of_values)] * len(lst_of_values))) / h])


print(derivative())

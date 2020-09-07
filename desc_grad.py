from sympy import Symbol, symbols, diff
import numpy as np
import random
from math import cos, sin,  log, pi, e

def determ_amount_var():
  """ Функция.
  
  возвращает количество пременных во введённой функции
  """
  f = input('Введите функцию:F(.....): ')
  dct = {}
  lst = []
  for i in f.replace("e", '').replace("pi", "").split(): # убираем e, т.к. знаем, что это не переменная
    dct[i] = dct.get(i, 0) + 1 # делаем словарь с ключами, чтобы получить только уникальные ключи
  for i in dct.keys():
    if i[0].isalpha(): 
      lst.append(Symbol(i)) # далее запихиваем в список только те ключи, которые начинаются с буквы ( чтобы получить кол-во переменных в нашей функции)
    else:
      pass
  variables = lst
  return [len(lst), variables, f]


# x ** 2 + y ** 3 + z ** 4
# x ** 2 - y ** 3
# 10 * x ** 2 + y ** 2
data_form_input = determ_amount_var()
amount_of_var = data_form_input[0]
variables = tuple(data_form_input[1])
variabl = list(variables)
function_for_paste = data_form_input[2] 
print('Внесите в аргументы искомой функции f{0}'.format(variables))


def f(x, y):
    return eval(function_for_paste)

def derivative(h = .0001, lambda_ = .0001):
   lst_of_values  =  [random.randint(4, 4) for val in variables]
   list_for_delta = []
   for i in lst_of_values:
       di = i + h
       list_for_delta.append(di)
   array_1 = np.array(list_for_delta)
   array_2 = np.array(lst_of_values)
   deriv_1 = np.array([(f(array_1[0], array_2[1] ) - f(*array_2)) / h])
   deriv_2 = np.array([(f(array_1[1], array_2[0] ) - f(*array_2)) / h])
   for _ in range(1000):
       lst_of_values = np.array(lst_of_values) - lambda_ * np.array([deriv_1, deriv_2]) 
   return  array_1, array_2, deriv_1, deriv_2, lst_of_values
    
    
print(derivative())

    

    

    

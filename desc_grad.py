from sympy import Symbol, symbols, diff
import numpy as np
import random

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
data_form_input = determ_amount_var()
amount_of_var = data_form_input[0]
variables = tuple(data_form_input[1])
variabl = list(variables)
function_for_paste = data_form_input[2] 
print('Внесите в аргументы искомой функции f{0}'.format(variables))


def f(x, y, z):
    return eval(function_for_paste)

def derivative(h = .01, lambda_ = .01, *args):
   lst_of_values  =  [random.randint(2, 5) for val in variables]
   dct_for_val = {val: random.randint(2, 5) for val in variables}
   return f(*lst_of_values)
    
    
   
    
    
print(derivative())

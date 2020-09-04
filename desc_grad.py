from sympy import Symbol, symbols

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
  return [len(lst), variables, [Symbol(f)]]


# x ** 2 + y ** 3 + z ** 4
print(determ_amount_var())
c = determ_amount_var()
amount_of_var = c[0]
variabl = c[1]
funci = c[2] 

def Func(variabl):
    
    return Symbol(str(funci).replace("[", "").replace("]", ""))

print(Func(variabl))
    



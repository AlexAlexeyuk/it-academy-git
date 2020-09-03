from sympy import Symbol
def determ_amount_var():
  """ Функция.
  возвращает количество пременных во введённой функции
  """
  f = input('Введите функцию: ')
  dct = {}
  lst = []
  for i in f.replace("e", '').replace("pi", "").split(): # убираем e, т.к. знаем, что это не переменная
    dct[i] = dct.get(i, 0) + 1 # делаем словарь с ключами, чтобы получить только уникальные ключи
  for i in dct.keys():
    if i[0].isalpha(): 
      lst.append(Symbol(i)) # далее запихиваем в список только те ключи, которые начинаются с буквы ( чтобы получить кол-во переменных в нашей функции)
    else:
      pass
  variables = tuple(lst)
  return len(lst), variables


print(determ_amount_var())

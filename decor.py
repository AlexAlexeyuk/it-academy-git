from sympy import Symbol, symbols, diff
global function
function = input('Введите функцию:F(.....): ')
def a_decorator_passing_arguments(function_to_decorate):

    def a_wrapper_accepting_arguments(*variables): # аргументы прибывают отсюда
        lst = []
        for i in function.replace("e", "").replace("pi", "").split(): # убираем e, т.к. знаем, что это не переменная
            if i[0].isalpha(): 
                lst.append(i) # далее запихиваем в список только те ключи, которые начинаются с буквы ( чтобы получить кол-во переменных в нашей функции)
            else:
                pass
            d = diff(eval(function), variables)
            print(d)
        variables = list(set(lst))  
        return function_to_decorate(variables, d)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def f(*variables, d):
    print(variables, d)
    

print(f(2, 1))

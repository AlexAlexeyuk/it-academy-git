""" Написать класс.

Класс будет считать вероятность того, что полученный
синий шар из первого ящика из двух"""


class Probability_counter:
  def __init__(self, p1 = 0.5, p2 = 0.5):
    self.p2 = 0.5
    self.p1 = 0.5

  def probability(self):
    amount_of_blue_balls_1 = (int(input("Введите сколько синих шариков в первом ящике: ")))
    amount_of_white_balls_1 = (int(input("Введите сколько белых шариков в первом ящике: ")))
    amount_of_blue_balls_2 = (int(input("Введите сколько синих шариков во втором ящике: ")))
    amount_of_white_balls_2 = (int(input("Введите сколько белых шариков во втором ящике: ")))
    try:
      pb1 = amount_of_blue_balls_1 / (amount_of_blue_balls_1 + amount_of_white_balls_1)
    except ZeroDivisionError:
      pb1 = 0
    try:
      pb2 = amount_of_blue_balls_2 / (amount_of_blue_balls_2 + amount_of_white_balls_2)
    except ZeroDivisionError:
      pb2 = 0
    try:
      return  ("Вероятность составляет: " + str(((self.p1 * pb1) / \
              (self.p1 * pb1 + self.p2 * pb2)*100)) + " процентов")
    except ZeroDivisionError:
      return ("Коль нет шаров ни в одном из ящиков, так " 
       "и вероятности рассчитать не сумеешь ты")

   

inst1 = Probability_counter()
print(inst1.probability())

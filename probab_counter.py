""" Написать класс.

Класс будет считать вероятность того, что полученный
синий шар из первого ящика из двух"""


class Probability_counter:
  def __init__(self, p1 = 0.5, p2 = 0.5):
    self.p2 = 0.5
    self.p1 = 0.5

  def probabil(self):
    amount_of_blue_balls_1 = (int(input("Введите сколько синих шариков в первом ящике: ")))
    amount_of_white_balls_1 = (int(input("Введите сколько белых шариков в первом ящике: ")))
    amount_of_blue_balls_2 = (int(input("Введите сколько синих шариков во втором ящике: ")))
    amount_of_white_balls_2 = (int(input("Введите сколько белых шариков во втором ящике: ")))
    try:
      pb1 = amount_of_blue_balls_1 / (amount_of_blue_balls_1 + amount_of_white_balls_1)
    except ZeroDivisionError:
      print(" мы не можем посчитать вероятность если нет шаров")
    try:
      pb2 = amount_of_blue_balls_2 / (amount_of_blue_balls_2 + amount_of_white_balls_2)
    except ZeroDivisionError:
      print(" мы не можем посчитать вероятность если нет шаров")
    return   (self.p1 * pb1) / (self.p1 * pb1 + self.p2 * pb2), pb1, pb2
   

inst_ = Probability_counter()
print(inst_.probabil())

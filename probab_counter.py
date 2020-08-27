class Probability_counter:
  def __init__(self, p1 = 0.5, p2 = 0.5):
    self.p2 = 0.5
    self.p1 = 0.5
  amount_of_blue_balls_1 = (int(input("Введите сколько синих шариков в первом ящике: ")))
  amount_of_blue_balls_2 = (int(input("Введите сколько синих шариков во втором ящике: ")))
  amount_of_white_balls_1 = (int(input("Введите сколько белых шариков в первом ящике: ")))
  amount_of_white_balls_2 = (int(input("Введите сколько белых шариков в первом ящике: ")))
  pb1 = amount_of_blue_balls_1 / (amount_of_blue_balls_1 + amount_of_white_balls_1)
  pb2 = amount_of_blue_balls_2 / (amount_of_blue_balls_2 + amount_of_white_balls_2)
  def probabil(self):
    return (self.p1 * pb1) / self.p1 * pb1 + self.p2 * pb2

inst_ = Probability_counter()
print(inst_.probabil())

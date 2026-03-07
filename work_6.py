class Prust:
    def __init__(self):
        self.turn_off = "Пристрій ввимкнено"
        self.turn_on = "Пристрій увімкнено"

class Mobile(Prust):
    def __init__(self):
        super().__init__()


class Computer(Prust):
    def __init__(self):
        super().__init__()


m = Mobile()
c = Computer()
print(m.turn_off)
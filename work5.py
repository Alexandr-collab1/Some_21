class Transport:
    def __init__(self):
        self.speed = 80
        self.method = "on ground"

class Car(Transport):
    def __init__(self):
        super().__init__()

class Boat(Transport):
    def __init__(self):
        super().__init__()
        self.speed = 20
        self.method = "on water"
class Velobike(Transport):
    def __init__(self):
        super().__init__()
        self.speed = 20

c = Car()
b = Boat()
v = Velobike()


print(v.method)
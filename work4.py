class Osoba:
    def __init__(self):
        self.name = "Bogdan"
        self.age = 41

class Vodi(Osoba):
    def __init__(self):
        self.number = 9283445284
        super().__init__()

vod = Vodi()
print(vod.name)
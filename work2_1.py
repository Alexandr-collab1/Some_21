class Product:
    def __init__(self, name, money, actual):
        self.name = name
        self.money = money
        self.actual = actual

class Cart:
    def __init__(self, coshic):
        self.coshic = coshic
        self.spysok = []

    def add_product(self, products):
        self.spysok.append(products)

    def Print_product(self):
        print(f"Кошик продукців {self.coshic}")
        for i in self.spysok:
            print(i.name)
            print(i.money)
            print(i.actual)

Product_1 = Product("eegs", 10, True)
cart = Cart("1")
cart = Cart("2")

cart.add_product(Product_1)

cart.Print_product()

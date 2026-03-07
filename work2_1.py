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
        print(f"Кошик покупця {self.coshic}")
        for i in self.spysok:
            print(i.name)
            print(i.money , "грн")
            print(i.actual)

    def All_money(self):
        result = 0
        for i in self.spysok:
            result += i.money 
        print(f"Загальна вартість {result} грн")

        

Product_1 = Product("Яйця", 20, "Є в наявності")
Product_2 = Product("Сир", 30, "Немає")
cart = Cart("1")


cart.add_product(Product_1)
cart.add_product(Product_2)
cart.Print_product()
cart.All_money()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def calculate_total_price(self):
    result = self.price * self.quantity
    return result
def display_info(self):
    print(f"Товар {self.name}, Ціна за один {self.price} грн , Ціна за пачку {calculate_total_price(self)} грн")

Tovar_1 = Product("Яйця", 20, 30) 
display_info(Tovar_1)
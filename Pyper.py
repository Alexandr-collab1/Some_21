class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
def deposit(self,number):
    result = self.balance + number
    print(f"Рахунок поповнено на {number} грн. Стало {result} грн")
def wirhdraw(self,number):
    if number < self.balance:
        result = self.balance - number
        print(f"З вашого рахунку знято {number} грн. Залишилося {result}")
    else:
        print(f"На вашому рахунку недостатньо коштів для списування {number} грн. У вас {self.balance} грн")
Person_1 = BankAccount(7535566934, 900)
deposit(Person_1,400)
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def get_salary_info(self):
    print(f"Цього робітника звуть {self.name}, його посада {self.position}, його заробітня плата {self.salary} грн у місяць")

Manager = Employee("Антон Владиславович", "Менеджер", 30000)
get_salary_info(Manager)
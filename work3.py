class Animal:
    leg = 4

class Cat(Animal):
    pass

class Dog(Animal):
    pass

c = Cat()
d = Dog()

print(c.leg)
print(d.leg)
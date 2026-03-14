slov = {"Makar": 16, "Sasha": 14, "Olena": 15, "Igor": 15, "Alex": 16}

def saput():
    if input(str("Введіть ім'я: ")) not in slov:
        raise NameError("not in slov")
    else:
        print(input())
    
saput()
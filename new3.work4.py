import random

al = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def vipadk(number, al):
    for i in range(number):
        a = ''.join(random.choice(al))
        print(a) 
        
        
        


v = vipadk(8, al)




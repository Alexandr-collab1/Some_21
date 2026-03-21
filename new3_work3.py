def raise_(number):
    i = 0
    while True:
        res = number**i
        yield res
        if res > 10**10:
            return 
        i += 1
    
    
res = raise_(3)
print(res)
for b in res:
    print(b)
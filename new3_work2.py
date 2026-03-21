def raise_(number, pos):
     i = 0
     for b in range(pos):
          yield (number) ** i
          i += 1


res = raise_(2, 10)
print(res)
for b in res:
    print(b)
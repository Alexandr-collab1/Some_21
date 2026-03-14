import math

try:
    math.Window()
except AttributeError:
    print("Not found")
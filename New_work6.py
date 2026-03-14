try:
    file = open("dxf.txt", "r")
    content = file.read()
    print(content)
except:
    print("This file is none")
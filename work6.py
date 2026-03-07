class LanguageProgram:
    def __init__(self):
        self.name = "Python"
    def print_Hello_world(self):
        print("print('Hello world')")

class Java(LanguageProgram):
    def __init__(self):
        super().__init__()
        self.name = "Java"
    def print_Hello_world(self):
        print("System.out.println('Hello, World!')")



j = Java()
print(j.print_Hello_world())
print(j.name)

from Base import Database
from poshyk import Parser
from front import AppInterface

def run():

    db = Database()
    parser = Parser()
    

    ui = AppInterface(db, parser)
    

    ui.run()

if __name__ == "__main__":
    run()

from Project.Base import Database
from Project.poshyk import Parser
from Project.front import AppInterface

def run():

    db = Database()
    parser = Parser()
    

    ui = AppInterface(db, parser)
    

    ui.run()

if __name__ == "__main__":
    run()

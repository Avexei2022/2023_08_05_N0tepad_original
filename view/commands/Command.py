class Command:

    def __init__(self, consoleUI):
        description = None
        self.consoleUI = consoleUI

    def Command(self, consoleUI):
        self.consoleUI = consoleUI
    

    def getDescription(self) -> str:
        return self.description
    
    def execute():
        None



from view.commands import Command
from view import ConsoleUI


class Exit(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Выход из программы"
        self.consoleUI = consoleUI

    def execute(self):
        self.consoleUI.exit()
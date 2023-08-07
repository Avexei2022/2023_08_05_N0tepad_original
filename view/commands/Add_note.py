from view.commands import Command


class Add_note(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Создать заметку"
        self.consoleUI = consoleUI

    def execute(self):
        self.consoleUI.add_note()


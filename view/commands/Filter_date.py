from view.commands import Command

class Filter_date(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Выбрать заметки по дате"
        self.consoleUI = consoleUI

    def execute(self):
        self.consoleUI.print_notes('date')
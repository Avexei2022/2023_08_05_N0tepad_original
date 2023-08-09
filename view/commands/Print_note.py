from view.commands import Command

class Print_note(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Чтение, редактирование или удаление заметки с поиском по ID"
        self.consoleUI = consoleUI

    def execute(self):
        self.consoleUI.print_notes('list')
        self.consoleUI.action_byId()

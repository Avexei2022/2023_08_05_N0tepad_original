import commands.Command as Command
import view.ConsoleUI as ConsoleUI


class Delete_note(Command):
    def __init__(self, consoleUI):
        super(ConsoleUI)
        discription = "Удалить заметку"

    def execute():
        ConsoleUI.action_byId('delete')

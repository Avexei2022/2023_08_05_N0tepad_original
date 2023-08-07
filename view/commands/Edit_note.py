import commands.Command as Command
import view.ConsoleUI as ConsoleUI


class Edit_note(Command):
    def __init__(self, consoleUI):
        super(ConsoleUI)
        discription = "Редактировать заметку"

    def execute():
        ConsoleUI.action_byId('edit')

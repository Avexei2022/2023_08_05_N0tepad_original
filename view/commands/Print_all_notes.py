from view.commands import Command

class Print_all_notes(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Показать все заметки (сортировка по дате)"
        self.consoleUI = consoleUI

    def execute(self):
        print("\nВсе заметки (сортировка по дате и времени):")
        self.consoleUI.print_notes('all')
        print("\nВывод на экран всех заметок завершен.")

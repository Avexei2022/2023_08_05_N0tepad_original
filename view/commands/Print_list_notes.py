from view.commands import Command


class Print_list_notes(Command.Command):
    def __init__(self, consoleUI):
        super()
        self.description = "Показать список заметок"
        self.consoleUI = consoleUI

    def execute(self):
        print("\nCписок заметок (сортировка по дате и времени):")
        self.consoleUI.print_notes('list')
        print("\nВывод на экран списка заметок завершен.")

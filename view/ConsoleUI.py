from presenter import Presenter
from view import Menu, View
import re


class ConsoleUI(View.View):
    
    def __init__(self):
        self.presenter = Presenter.Presenter()
        self.work = True
        user_string = ""
        self.menu = Menu.Menu(self)
        self.min_text_length = 3
        
        
    def start(self):
        print("\nПРОГРАММА ЗАМЕТКИ")
        while self.work:
            self.execute()

    def exit(self):
        self.work = False

    def execute(self):
        print(self.menu.printMenu())
        choice = input("Введите цифру соответствующего пункта меню: ")
        if self.checkTextForInt(choice):
            numCommand = int(choice)
            if self.checkCommand(numCommand):
                self.menu.execute(numCommand)

    def checkTextForInt(self,choice) -> bool:
        if re.match("[1-9]+", choice):
            return True
        else:
            self.inputError()
            return False

    def inputError(self):
        print("\nВведено неверное значение.\n")

    def checkCommand(self, numCommand):
        size = self.menu.getSize()
        if numCommand <= size:
            return True
        else:
            self.inputError()
            return False

    def check_len_text_input(self, text):
        while len(text) <= (self.min_text_length):
            print(
                f'Минимальный количество символов в тексте: {self.min_text_length}\n')
            text = input('Введите текст: ')
        else:
            return text.replace(";", ",")

    def add_note(self):
        title = self.check_len_text_input(
        input('\nВведите название заметки: '))
        body = self.check_len_text_input(input('\nВведите текст заметки: '))
        self.presenter.add_note(title, body)

    def print_notes(self, numCommand):
        self.presenter.print_notes(numCommand)

    def action_byId(self):
        self.presenter.action_byId()

    def finish(self):
        print("\nЗАМЕТКИ. Программа закрыта.\n")

    def printAnswer(self, text):
        print(text)

    def dialog(self, text_out) -> str:
        return input(text_out)

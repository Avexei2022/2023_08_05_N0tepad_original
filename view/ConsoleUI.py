from model import Service
from presenter import Presenter
from view import Menu, View
import re


class ConsoleUI(View.View):
    
    def __init__(self):
        self.service = Service.Service()
        # self.presenter = Presenter.
        self.work = True
        user_string = ""
        self.menu = Menu.Menu(self)
        
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

    def check_len_text_input(self, text, n):
        while len(text) <= n:
            print(f'Текст должен содержать не менее {n} символов.\n')
            text = input('Введите текст: ')
        else:
            return text

    def print_notes(self, numCommand):
        self.service.print_notes(numCommand)

    def add_note(self):
        self.service.add_note()

    def action_byId(self):
        self.service.action_byId()

    def finish(self):
        print("\nЗАМЕТКИ. Программа закрыта.\n")

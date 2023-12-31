from model import Service
from view import ConsoleUI


class Presenter:

    def __init__(self):
        self.service = Service.Service()


    def print_notes(self, numCommand):
        self.service.print_notes(numCommand)

    def add_note(self, title, body):
        self.service.add_note(title, body)

    def action_byId(self):
        self.service.action_byId()

    def get_body(self) -> str:
        return ConsoleUI.ConsoleUI().get_body()

    def dialog(self, text_out)-> str:
        return ConsoleUI.ConsoleUI().dialog(text_out)
    
    def printAnswer(self, text):
        ConsoleUI.ConsoleUI().printAnswer(text)


from view.commands import Add_note, Exit, Print_all_notes, Print_list_notes, Print_note



class Menu:
    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        self.add_note = Add_note.Add_note(consoleUI=consoleUI)
        self.print_all_notes = Print_all_notes.Print_all_notes(consoleUI=consoleUI)
        self.print_list_notes = Print_list_notes.Print_list_notes(
            consoleUI=consoleUI)
        self.print_note = Print_note.Print_note(consoleUI=consoleUI)
        self.exit = Exit.Exit(consoleUI=consoleUI)
        self.commandList = []
        self.commandList.append(self.add_note)
        self.commandList.append(self.print_all_notes)
        self.commandList.append(self.print_list_notes)
        self.commandList.append(self.print_note)
        self.commandList.append(self.exit)

    def printMenu(self) -> str:
        string = "\nМеню:\n"
        for i in range(len(self.commandList)):
            string += str(i + 1) + ". "
            string += self.commandList[i].getDescription()
            string += "\n"
        return string

    def execute(self, numCommand):
        self.commandList[numCommand - 1].execute()

    def getSize(self) -> int:
        return len(self.commandList)

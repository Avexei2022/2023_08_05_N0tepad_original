from model import Note
from presenter import Presenter

class File_operator:

    def __init__(self):
        self.note_type = Note.Note


    def write_file(self, array, current_mode):
        file = open("notes.csv", mode='w', encoding='utf-8')
        file.seek(0)
        file.close()
        file = open("notes.csv", mode=current_mode, encoding='utf-8')
        for item in array:
            file.write(self.note_type().to_string(item))
            file.write('\n')
        file.close


    def read_file(self):
        try:
            array = []
            file = open("notes.csv", "r", encoding='utf-8')
            notes_string = file.read().strip().split("\n")
            for item in notes_string:
                split_item = item.split(';')
                note = self.note_type(
                    id=split_item[0], title=split_item[1], body=split_item[2], date=split_item[3])
                array.append(note)
        except Exception:
            Presenter.Presenter().printAnswer('Заметок нет')
        finally:
            return array


from datetime import datetime
import uuid


class Note(object):
    def __init__(self, id=str(uuid.uuid1())[0:5],  title="текст", body="текст", date=str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self, note):
        return note.id
    
    def set_id(self, note):
        note.id = str(uuid.uuid1())[0:5]

    def get_title(self, note):
        return note.title
    
    def set_title(self, note, title):
        note.title = title

    def get_body(self, note):
        return note.body
    
    def set_body(self, note, body):
        note.body = body

    def get_date(self, note):
        return note.date

    def set_date(self, note):
        note.date = str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))

    def to_string(self, note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def note_full_info(self, note):
        return '\nID: ' + note.id + ', Дата и время: ' + note.date + '\n' + 'Заголовок: ' + note.title + '\n' + 'Текст заметки: ' + note.body

    def note_title_info(self, note):
        return '\nID: ' + note.id  + ', Дата и время: ' + note.date + ', Заголовок: ' + note.title
    


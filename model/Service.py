from model import File_operator, Note
import view.ConsoleUI as ConsoleUI

class Service:

    def __init__(self):
        self.min_text_length = 3
        self.note = Note.Note()
        self.file_operator = File_operator.File_operator()
        self.note_type = Note.Note
        
    
    def check_len_text_input(self, text):
        while len(text) <= (self.min_text_length):
            print(
                f'Минимальный количество символов в тексте: {self.min_text_length}\n')
            text = input('Введите текст: ')
        else:
            return text

    def add_note(self):
        title = self.check_len_text_input(input('\nВведите название заметки: '))
        body = self.check_len_text_input(input('\nВведите текст заметки: '))
        new_note = self.note_type(title=title, body=body)
        array = self.file_operator.read_file()
        for item in array:
            if self.note.get_id(new_note) == self.note.get_id(item):
                self.note.set_id(new_note)
                self.note.set_date(new_note)
        save = input("\nВы создали новую заметку:\n" +
              self.note.note_full_info(new_note) + 
              "\n\nДля сохранения заметки в файл введите 'Yes': ")
        if save.lower() == 'yes':
            array.append(new_note)
            self.file_operator.write_file(array, 'a')
            print('\nЗаметка добавлена в файл.\n')
        else:
            print('\nЗаметка не сохранена.\n')


    def print_notes(self, choice):
        flag = True
        array = self.get_array_from_file()
        if choice == 'date':
            date = input('\nВведите дату (dd.mm.yyyy): ')
        for item in array:
            if choice == 'all':
                flag = False
                print(self.note.note_full_info(item))
            if choice == 'list':
                flag = False
                print(self.note.note_title_info(item))
            if choice == 'id':
                flag = False
                print('ID: ' + self.note.get_id(item))
            if choice == 'date':
                flag = False
                if date in self.note.get_date(item):
                    print(self.note.note_full_info(item))
        if flag:
            print('Данные отсутствуют')


    def action_byId(self, action):
        id = input('\nВведите id заметки: ')
        array = self.get_array_from_file()
        flag = True
        for item in array:
            if id == self.note.get_id(item):
                flag = False
                if action == 'edit':
                    note = ConsoleUI.ConsoleUI.create_note(self.num)
                    self.note.set_title(item, note.get_title())
                    self.note.set_body(item, note.get_body())
                    self.note.set_date(item)
                    print('Заметка изменена.')
                if action == 'print':
                    print(self.note.note_full_info(item))
                if action == 'delete':
                    array.remove(item)
                    print('Заметка удалена.')
        if flag:
            print('Данные отсутствуют')
        if action != 'print':
            self.file_operator.write_file(array, 'a')

    def sort_by_date(self, note):
        return note.date
    
    def get_array_from_file(self) -> list:
        array = self.file_operator.read_file()
        array.sort(key=self.sort_by_date)
        return array




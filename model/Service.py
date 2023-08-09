from model import File_operator, Note


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
            return text.replace(";" ,",")

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
            date = input('\nВведите дату (yyyy.mm.dd): ')
        for item in array:
            if choice == 'all':
                flag = False
                print(self.note.note_full_info(item))
            if choice == 'list':
                flag = False
                print(self.note.note_title_info(item))
            if choice == 'date':
                if date == self.note.get_date(item)[:10]:
                    flag = False
                    print(self.note.note_title_info(item))
        if flag:
            print('\nДанные отсутствуют')
        elif choice == 'date':
            self.action_byId()


    def action_byId(self):
        id = input('\nДля чтения, редактирования или удаления введите id заметки: ')
        array = self.get_array_from_file()
        flag = True
        flag2 = True
        for item in array:
            if id == self.note.get_id(item):
                flag = False
                print(self.note.note_full_info(item))
                print("\nОперации с заметкой:\n1. Редактировать текст заметки.\n2. Удалить заметку.\n" +
                          "Для перехода к начальному меню введите любой другой символ.\n")
                input_text = ""
                input_text = input(
                            "Введите символ необходимой операции: ").strip()
                if input_text == "1":
                    body = self.check_len_text_input(input('\nВведите новый текст заметки: '))
                    self.note.set_body(item, body.replace(";", ","))
                    self.note.set_date(item)
                    print('\nЗаметка изменена.')
                elif input_text == "2":
                    array.remove(item)
                    print('\nЗаметка удалена.')
                else:
                    flag2 = False
        if flag:
            print('\nДанные отсутствуют')
        if flag2:
            self.file_operator.write_file(array, 'a')

    def sort_by_date(self, note):
        return note.date
    
    def get_array_from_file(self) -> list:
        array = self.file_operator.read_file()
        array.sort(key=self.sort_by_date)
        return array




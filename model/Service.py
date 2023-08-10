from model import File_operator, Note
from presenter import Presenter


class Service:

    def __init__(self):
        self.note = Note.Note()
        self.file_operator = File_operator.File_operator()
        self.note_type = Note.Note
        
    def add_note(self, title, body):
        new_note = self.note_type(title=title, body=body)
        array = self.file_operator.read_file()
        for item in array:
            if self.note.get_id(new_note) == self.note.get_id(item):
                self.note.set_id(new_note)
                self.note.set_date(new_note)
        save = Presenter.Presenter().dialog("\nВы создали новую заметку:\n" +
              self.note.note_full_info(new_note) + 
              "\n\nДля сохранения заметки в файл введите 'Yes': ")
        if save.lower() == 'yes':
            array.append(new_note)
            self.file_operator.write_file(array, 'a')
            Presenter.Presenter().printAnswer('\nЗаметка добавлена в файл.\n')
        else:
            Presenter.Presenter().printAnswer('\nЗаметка не сохранена.\n')


    def print_notes(self, choice):
        flag = True
        array = self.get_array_from_file()
        if choice == 'date':
            date = Presenter.Presenter().dialog('\nВведите дату (yyyy.mm.dd): ')
        for item in array:
            if choice == 'all':
                flag = False
                Presenter.Presenter().printAnswer(self.note.note_full_info(item))
            if choice == 'list':
                flag = False
                Presenter.Presenter().printAnswer(
                    self.note.note_title_info(item))
            if choice == 'date':
                if date == self.note.get_date(item)[:10]:
                    flag = False
                    Presenter.Presenter().printAnswer(
                        self.note.note_title_info(item))
        if flag:
            Presenter.Presenter().printAnswer('\nДанные отсутствуют')
        elif choice == 'date':
            self.action_byId()


    def action_byId(self):
        id = Presenter.Presenter().dialog(
            '\nДля чтения, редактирования или удаления введите id заметки: ')
        array = self.get_array_from_file()
        flag = True
        flag2 = True
        for item in array:
            if id == self.note.get_id(item):
                flag = False
                Presenter.Presenter().printAnswer(self.note.note_full_info(item))
                Presenter.Presenter().printAnswer("\nОперации с заметкой:\n1. Редактировать текст заметки.\n2. Удалить заметку.\n" +
                          "Для перехода к начальному меню введите любой другой символ.\n")
                input_text = ""
                input_text = Presenter.Presenter().dialog(
                            "Введите символ необходимой операции: ").strip()
                if input_text == "1":
                    body = self.check_len_text_input(
                        Presenter.Presenter().dialog('\nВведите новый текст заметки: '))
                    self.note.set_body(item, body.replace(";", ","))
                    self.note.set_date(item)
                    Presenter.Presenter().printAnswer(
                        self.note.note_full_info(item))
                    Presenter.Presenter().printAnswer('\nТекст заметки изменен.')
                elif input_text == "2":
                    array.remove(item)
                    Presenter.Presenter().printAnswer('\nЗаметка удалена.')
                else:
                    flag2 = False
        if flag:
            Presenter.Presenter().printAnswer('\nДанные отсутствуют')
        if flag2:
            self.file_operator.write_file(array, 'a')

    def sort_by_date(self, note):
        return note.date
    
    def get_array_from_file(self) -> list:
        array = self.file_operator.read_file()
        array.sort(key=self.sort_by_date)
        return array




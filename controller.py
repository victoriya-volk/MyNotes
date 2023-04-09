import view
import notes
import data_base as db


def main_menu(choice: int):
    match choice:
        case 1:
            print('Показать все заметки')
            db.load_data_base()
            notes_list = notes.get_notes()
            view.print_notes_base(notes_list)
        case 2:
            print('Новая заметка')
            note = view.input_new_note()
            notes.add_note(note)
            db.save_data_base()
        case 3:
            print('Изменить заметку')
            notes_list = notes.get_notes()
            view.print_notes_base(notes_list)
            id = view.input_change_note()
            view.print_notes_base(notes.change_note(id))
            db.save_data_base()
        case 4:
            print('Удалить заметку')
            notes_list = notes.get_notes()
            view.print_notes_base(notes_list)
            id = view.input_remove_note()
            if notes.remove_note(id):
                view.remove_success()
            db.save_data_base()
        case 5:
            print('выполнить поиск по дате')
            search_text = view.input_search_text()
            founding = notes.search_note(search_text)
            view.print_notes_base(founding)
        case 0:
            db.save_data_base()
            return True
def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.logg_off()
            break
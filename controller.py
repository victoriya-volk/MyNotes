import view
def main_menu(choice: int):
    match choice:
        case 1:
            print('Показать все заметки')
        case 2:
            print('Новая заметка')
        case 3:
            print('Изменить заметку')
        case 4:
            print('Удалить заметку')
        case 5:
            print('выполнить поиск по дате')
        case 0:
            print('Закрыть приложение')
            return True
def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.logg_off()
            break
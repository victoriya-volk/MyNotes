import datetime


def main_menu():
    print('\n1. Показать все заметки')
    print('2. Новая заметка')
    print('3. Изменить заметку')
    print('4. Удалить заметку')
    print('5. Выполнить поиск')
    print('0. Выход\n')
    return choice_item_menu()

def choice_item_menu():
    while True:
        try:
            choice = int(input('Введите номер команды из меню: '))
            if choice in range(0, 6):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')

def print_notes_base(notes_list: list):
    if len(notes_list) > 0:
        for id, note in enumerate(notes_list, 1):
            print(id, *note)
    else:
        print('У вас нет сохраненных заметок')

def logg_off():
    print('Вы вышли из приложения.')

def remove_success():
    print('Заметка удалена!')

def input_new_note():
    date = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    return [date, title.upper(), text]

def input_remove_note():
    id = int(input('Введите ID заметки, которую хотите удалить: '))
    return id

def input_search_text():
    search_text = input('Введите часть дату или ее часть в формате ДД.ММ.ГГГГ для поиска: ')
    return search_text

def print_search_notes(notes_list: list):
    if len(notes_list) > 0:
        for id, note in enumerate(notes_list, 1):
            print(id, *note)
    else:
        print('\nНичего не найдено.')

def input_change_note():
    id = int(input('Введите ID заметки, которую желаете изменить: '))
    return id

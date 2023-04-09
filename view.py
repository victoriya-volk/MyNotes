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


def logg_off():
    print('Вы вышли из приложения.')
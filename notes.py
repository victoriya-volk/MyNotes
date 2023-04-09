import datetime

notes = []

def get_notes():
    global notes
    return notes

def set_notes(new_notes):
    global notes
    notes = new_notes

def add_note(note: list):
    global notes
    notes.append(note)

def remove_note(id):
    global notes
    note = notes[id-1][1]
    confirm = input(f'Подтвердите удаление заметки {note}? (y/n)')
    if confirm.lower() == 'y':
        notes.pop(id-1)
        return True
    return False

def search_note(search_text: str):
    global notes
    founding = []
    for note in notes:
        if search_text in note[0]:
            founding.append(note)
    return founding

def change_note(id):
    global notes
    note = notes[id-1]
    i = 1
    note[0] = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
    while i < len(note):
        new_data = input(f'Как вы хотите изменить {note[i]}?\n')
        if new_data:
            if i == 1:
                note[i] = new_data.upper()
            note[i] = new_data
        i += 1
    last_change = notes.pop(id-1)
    notes.append(last_change)
    return notes
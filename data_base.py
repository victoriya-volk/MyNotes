import notes as notes

path = 'notes.csv'

def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        notesStr = file.readlines()
        notes.set_notes(strs_to_list(notesStr))

def strs_to_list(notes: list):
    new_notes = []
    for note in notes:
        new_notes.append(note.strip().split(';'))
    return new_notes

def save_data_base():
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(list_to_strs())


def list_to_strs():
    newNotes = notes.get_notes()
    new_notes_base = []
    for note in newNotes:
        new_notes_base.append(';'.join(note) + '\n')
    new_notes_base[-1] = new_notes_base[-1][:-1]
    return ''.join(new_notes_base)
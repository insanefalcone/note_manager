
def load_notes_from_file(filename):
    notes = []

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip().split('---')

        for item in content:
            if item.strip():  # Проверяем, что блок не пустой
                note_dict = {}
                lines = item.strip().split('\n')

                for line in lines:
                    if line:
                        key, value = line.split(': ', 1)
                        note_dict[key.lower().replace(' ', '_')] = value.strip()

                notes.append(note_dict)

    return notes


notes = load_notes_from_file('filename.txt')
print(notes)


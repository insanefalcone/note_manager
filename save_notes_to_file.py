
# file.close()


def save_notes_to_file(notes, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("---\n")
            file.write("\n")  # Добавляет пустую строку между заметками


notes = [
    {
        'username': 'Кирилл',
        'title': 'Заметка 1',
        'content': 'Описание 1',
        'status': 'активна',
        'created_date': '2025-10-01',
        'issue_date': '2025-10-10'
    },
    {
        'username': 'Аня',
        'title': 'Заметка 2',
        'content': 'Описание 2',
        'status': 'завершена',
        'created_date': '2024-09-15',
        'issue_date': '2024-09-20'
    }
]

save_notes_to_file(notes, 'filename.txt')


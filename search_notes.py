def format_results(filtered_notes):
    if not filtered_notes:
        return "Заметки, соответствующие запросу, не найдены."

    result = ""
    for note in filtered_notes:
        result += f"Заметка:\n - Заголовок: {note['title']}\n - Содержимое: {note['content']}\n - Автор: {note['username']}\n - Статус: {note['status']}\n\n"

    return result.strip()


def search_notes(notes, keywords=None, status=None):
    if not notes:
        return "Список заметок пуст."

    if keywords is None:
        return "Введите хотя бы одно ключевое слово для поиска."

    keywords = [keyword.lower() for keyword in keywords]

    filtered_notes = []

    for note in notes:
        match = True

        if keywords:
            if not any(keyword in note['title'].lower() or
                       keyword in note['content'].lower() or
                       keyword in note['username'].lower() for keyword in keywords):
                match = False

        if status and note['status'] != status:
            match = False

        if match:
            filtered_notes.append(note)

    return format_results(filtered_notes)


# Пример списка заметок
notes = [
    {"title": "Первая заметка", "content": "Это тестовая заметка", "username": "User1", "status": "активна"},
    {"title": "Вторая заметка", "content": "Важная информация", "username": "User2", "status": "закрыта"},
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

# Основной цикл программы
while True:
    print("Доступные критерии поиска:")
    print("- keywords: одно или несколько ключевых слов (например, ['тест', 'информация'])")
    print("- status: статус заметки (например, 'активна' или 'закрыта')")
    print("Введите ключевые слова (или 'выход' для выхода):")

    user_input = input().strip()

    if user_input.lower() == 'выход':
        break

    keywords = user_input.split(',')
    keywords = [keyword.strip() for keyword in keywords if keyword.strip()]  # Удаляем лишние пробелы

    print("Введите статус заметки (или оставьте пустым):")
    status = input().strip() or None  # Если ничего не введено, статус будет None

    result = search_notes(notes, keywords=keywords, status=status)
    print(result)


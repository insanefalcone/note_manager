# этап 2: задание 5
# реализована программа для добавления и удаления заметок
# программа добавляет заметки в список, а так же удаляет их на основе имени или заголовка
# реализована нечувствительность к регистрам, вопрос о подтверждении удаления и
# удаление нескольких заметок по одинаковым именам или заголовкам


# список для хранения заметок
notes = [
    {"user": "Кирилл", "title": "Список покупок", "content": "Молоко, яйца, хлеб"},
    {"user": "олег", "title": "заметка о встрече", "content": "увеличить объем продаж"},
    {"user": "КИРИЛЛ", "title": "список задач на сегодня", "content": "пресс качат, бегит, анжуманя"},
    {"user": "Аня", "title": "список дел", "content": "сходить в магазин, уборка, приготовить ужин"}
]

while True:
    print("текущие заметки:")
    for note in notes:
        print(f"пользователь: {note['user']}, заголовок: {note['title']}, содержимое: {note['content']}")

    action = input("выберите действие: 1 - добавить заметку, 2 - удалить заметку, 3 - выход: ")

    if action == '1':  # добавление заметки
        user = input("введите имя пользователя: ")
        title = input("введите заголовок заметки: ")
        content = input("введите содержимое заметки: ")

        notes.append({"user": user, "title": title, "content": content})
        print("заметка успешно добавлена.")

    elif action == '2':  # удаление заметки
        criteria = input("введите критерий для удаления (имя пользователя (через '@') или заголовок): ")

        if criteria.startswith("@"):
            username = criteria[1:].lower()  # приводим имя пользователя к нижнему регистру
            filtered_notes = [note for note in notes if note['user'].lower() == username]
        else:
            title = criteria.lower()  # приводим заголовок к нижнему регистру
            filtered_notes = [note for note in notes if note['title'].lower() == title]

        if not filtered_notes:
            print("заметки для удаления не найдены.")
        else:
            print("найденные заметки для удаления:")
            for note in filtered_notes:
                print(f"пользователь: {note['user']}, заголовок: {note['title']}, содержимое: {note['content']}")

            confirmation = input("вы уверены, что хотите удалить эти заметки? (да/нет): ").strip().lower()

            if confirmation == 'да':
                if criteria.startswith("@"):
                    notes[:] = [note for note in notes if note['user'].lower() != username]
                else:
                    notes[:] = [note for note in notes if note['title'].lower() != title]

                print("заметки успешно удалены.")
            else:
                print("удаление отменено.")

    elif action == '3':  # выход
        break

    else:
        print("некорректный выбор. попробуйте снова.")

print("до свидания!")

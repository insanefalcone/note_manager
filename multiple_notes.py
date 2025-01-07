from datetime import datetime

# реализована программа для работы и добавления нескольких заметок
print("добро пожаловать в 'менеджер заметок'! \nвы можете добавить новую заметку.")
# Инициализация списка для хранения заметок
notes = []

while True:
    print("введите данные для заметки:")

    # ввод данных заметки
    name = input("имя: ")

    existing_titles = []  #список для хранения заголовков
    while True:
        new_title = input("введите заголовок (или оставьте пустым завершения): ")
        if new_title.lower() == '':
            break

        if new_title in existing_titles:
            print("Этот заголовок уже существует. Пожалуйста, введите уникальный заголовок.")
        else:
            existing_titles.append(new_title)
            print(f"Заголовок '{new_title}' успешно добавлен!")

    content = input("введите описание заметки: ")

    while True:
        status = input("введите статус выполнения заметки (новая, в процессе, выполнено): ")
        valid_statuses = ["новая", "выполнено", "в процессе"]
        if status in valid_statuses:
            break
        else:
            print("ошибка: неверный статус. пожалуйста, выберите один из предложенных статусов.")

    created_date_my_note = datetime.today().date()  #дата формируется автоматически от времени телефона/пк

    while True:
        issue_date = input("введите дату планируемого окончания (формат дд-мм-гггг или гггг-мм-дд): ")

        # Проверяем формат дд-мм-гггг
        try:
            if len(issue_date) == 10 and issue_date[2] == '-' and issue_date[5] == '-':
                deadline_date = datetime.strptime(issue_date, "%d-%m-%Y")
                break
        except ValueError:
            pass

        # Проверяем формат гггг-мм-дд
        try:
            if len(issue_date) == 10 and issue_date[4] == '-' and issue_date[7] == '-':
                deadline_date = datetime.strptime(issue_date, "%Y-%m-%d")
                break
        except ValueError:
            pass

        print("неверный формат даты. пожалуйста, попробуйте снова.")

    # создание заметки как словаря
    note = {
        "имя": name,
        "заголовок": existing_titles,
        "описание": content,
        "статус": status,
        "дата создания": created_date_my_note,
        "дедлайн": deadline_date.strftime('%d-%m-%Y'),
    }

    # добавление заметки в список
    notes.append(note)
    print("заметка добавлена!\n")

    # запрос на продолжение ввода заметок
    continue_input = input("Хотите добавить ещё одну заметку? ('пробел' для завершения): ")
    if continue_input.lower() == ' ':
        break


# отображение всех заметок
print("\nСписок всех заметок:")
for idx, note in enumerate(notes, start=1):
    print(f"Заметка {idx}:")
    for key, value in note.items():
        print(f"  {key}: {value}")
    print() #для разграничения между заметками
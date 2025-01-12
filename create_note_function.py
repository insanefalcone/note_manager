from datetime import datetime, timedelta


def is_valid_date(date_str):
    # Проверяет, является ли строка корректной датой в формате день-месяц-год
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def create_note():
    # Создает заметку с запрашиваемыми полями у пользователя

    username = input("Введите ваше имя пользователя: ")

    # Проверка заголовка
    while True:
        title = input("Введите заголовок заметки: ")
        if title.strip() == "":
            print("Заголовок не может быть пустым. Пожалуйста, попробуйте снова.")
        else:
            break

    # Проверка содержания заметки
    while True:
        content = input("Введите описание заметки: ")
        if content.strip() == "":
            print("Описание не может быть пустым. Пожалуйста, попробуйте снова.")
        else:
            break

    # Выбор статуса из фиксированного списка
    valid_statuses = ["новая", "в процессе", "выполнено"]
    while True:
        status = input(f"Введите статус заметки ({', '.join(valid_statuses)}): ")
        if status in valid_statuses:
            break
        else:
            print(f"Неверный статус. Пожалуйста, выберите из: {', '.join(valid_statuses)}.")

    # Получаем текущую дату
    created_date = datetime.now().strftime("%d-%m-%Y")

    # Запрашиваем дату дедлайна, задаем по умолчанию
    default_issue_date = (datetime.now() + timedelta(weeks=1)).strftime("%d-%m-%Y")
    issue_date_input = input(f"Введите дату дедлайна в формате день-месяц-год: ")

    if issue_date_input.strip() == "":
        issue_date = default_issue_date
    else:
        while not is_valid_date(issue_date_input):
            print("Неверный формат даты. Попробуйте снова.")
            issue_date_input = input(
                f"Введите дату дедлайна в формате день-месяц-год: ")
        issue_date = issue_date_input

    # Возвращаем данные заметки в виде словаря
    note = {                                     # почему выделяет желтым???? в чем ошибка?
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    return note


# Вызов функции и вывод результата на экран
if __name__ == "__main__":
    note = create_note()
    print("\nЗаметка успешно создана:")
    print(note)


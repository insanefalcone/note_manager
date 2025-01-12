from datetime import datetime


def is_valid_date(date_str):
    # Проверяет, является ли строка корректной датой в формате день-месяц-год
    if date_str == "":
        return True  # Позволяем пустую строку
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def get_new_value(field_name):
    # Запрашивает у пользователя новое значение для поля, позволяя оставить его пустым
    if field_name == "issue_date":
        new_value = input("Введите новое значение для даты дедлайна (день-месяц-год, или оставьте пустым): ")
        while not is_valid_date(new_value):
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")
            new_value = input("Введите новое значение для даты дедлайна (день-месяц-год, или оставьте пустым): ")
    else:
        new_value = input(f"Введите новое значение для {field_name} (или оставьте пустым, чтобы не менять): ")
    return new_value


def update_note(note):
    # Позволяет пользователю обновить поля заметки

    # Показываем пользователю поля, которые можно обновить
    print("Выберите поля для обновления (введите номера через запятую):")
    fields = ["username", "title", "content", "status", "issue_date"]

    for i, field in enumerate(fields, 1):
        print(f"{i}. {field}: {note[field]}")

    field_choices = input("Введите номера полей для обновления: ")
    selected_fields = [fields[int(num) - 1] for num in field_choices.split(',') if
                       num.strip().isdigit() and 1 <= int(num.strip()) <= len(fields)]

    if not selected_fields:
        print("Вы ничего не выбрали для обновления.")
        return note

    for field_name in selected_fields:
        new_value = get_new_value(field_name)
        if new_value != "":
            confirm = input(
                f"Вы уверены, что хотите обновить поле '{field_name}' на '{new_value}'? (да/нет): ").strip().lower()
            if confirm == "да":
                note[field_name] = new_value
                print(f"{field_name.capitalize()} успешно обновлено на '{new_value}'.")
            else:
                print(f"Поле '{field_name}' оставлено без изменений.")
        else:
            print(f"Поле '{field_name}' оставлено без изменений.")

    return note


# Пример использования функции
if __name__ == "__main__":
    note = {
        "username": "user1",
        "title": "Заметка 1",
        "content": "Это содержимое заметки.",
        "status": "новая",
        "created_date": "01-01-2023",
        "issue_date": "08-01-2023"
    }

    updated_note = update_note(note)
    print("\nОбновленная заметка:")
    print(updated_note)


import datetime


def append_note_with_details(filename):
    while True:
        username = input("Введите имя пользователя (или нажмите Enter для завершения): ")
        if username == "":
            break

        title = input("Введите заголовок: ")
        content = input("Введите описание: ")
        status = input("Введите статус: ")

        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        issue_date = input("Введите дедлайн (формат: YYYY-MM-DD): ")

        note = (
            f"Имя пользователя: {username}\n"
            f"Заголовок: {title}\n"
            f"Описание: {content}\n"
            f"Статус: {status}\n"
            f"Дата создания: {created_date}\n"
            f"Дедлайн: {issue_date}\n"
            f"---\n"
        )

        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(note)
            print("Заметка успешно добавлена в файл.")
        except IOError as e:
            print(f"Произошла ошибка при доступе к файлу {filename}: {e}")
        except Exception as e:
            print(f"Ошибка при добавлении заметки в файл {filename}. Подробности: {e}")


# Пример использования
append_note_with_details('filename.txt')


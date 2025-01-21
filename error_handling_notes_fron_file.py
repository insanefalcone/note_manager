
def load_notes_from_file(filename):
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # Обработка содержимого файла здесь

    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as file:
            print(f"Файл {filename} не найден. Создан новый файл.")
    except IOError as e:
        print(f"Произошла ошибка при доступе к файлу {filename}: {e}")
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое. Подробности: {e}")

notes = load_notes_from_file('filename.txt')
print(notes)

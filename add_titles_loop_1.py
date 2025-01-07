# Список для хранения заголовков
existing_titles = []

# Ввод заголовков
while True:
    new_title = input("Введите заголовок (или оставьте пустым завершения): ")
    if new_title.lower() == '':
        break

    if new_title in existing_titles:
        print("Этот заголовок уже существует. Пожалуйста, введите уникальный заголовок.")
    else:
        existing_titles.append(new_title)
        print(f"Заголовок '{new_title}' успешно добавлен!")

print("список звголовков: ", existing_titles)

from datetime import datetime

# реализована программа для отображения и возможности отслеживания дедлайнов

my_note = input("Введите название заметки: ")
created_date_my_note = datetime.today()
print("Заметка: ", my_note, "\nДата создания заметки: ", created_date_my_note)

while True:
    issue_date = input("Введите дату планируемого окончания (формат дд-мм-гггг или гггг-мм-дд): ")

    # Проверяем формат дд-мм-гггг
    try:
        if len(issue_date) == 10 and issue_date[2] == '-' and issue_date[5] == '-':
            deadline_date = datetime.strptime(issue_date, "%d-%m-%Y")
            print(f"Дата планируемого окончания: {deadline_date.strftime('%d-%m-%Y')}")
            break
    except ValueError:
        pass

    # Проверяем формат гггг-мм-дд
    try:
        if len(issue_date) == 10 and issue_date[4] == '-' and issue_date[7] == '-':
            deadline_date = datetime.strptime(issue_date, "%Y-%m-%d")
            print(f"Дата планируемого окончания: {deadline_date.strftime('%Y-%m-%d')}")
            break
    except ValueError:
        pass

    print("Неверный формат даты. Пожалуйста, попробуйте снова.")

print("Заметка: ", my_note,
      "\nДата создания заметки: ", created_date_my_note,
      "\nДата планируемого окончания: ", deadline_date.strftime('%d-%m-%Y'))

# проверка на кол-во оставшихся дней до дедлайна
today = datetime.now()
days_left = (deadline_date - today).days

if days_left > 0:
    if days_left == 1:
        print(f"У вас остался {days_left} день до дедлайна.")
    else:
        print(f"У вас осталось {days_left} дня(ей) до дедлайна.")
elif days_left == 0:
    print("Внимание! Дата окончания истекает сегодня!")
else:
    print(f"Внимание! Дедлайн прошёл {-days_left} дня(ей) назад.")
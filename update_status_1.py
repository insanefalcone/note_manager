# реализована программа для изменения статуса заметки
my_note = input("введите название заметки: ")
status_my_note = "в процессе"  #значение по умолчанию в момент создания
print("заметка: ", my_note, "\nстатус заметки: ", status_my_note)

new_status_my_note = True  #переменная новый статус заметки
while new_status_my_note:
    repeat = input("желаете изменить статус заметки? (да/нет) ")
    if repeat.lower() == "нет":
        new_status_my_note = False
        print("заметка: ", my_note, "\nстатус заметки: ", status_my_note)
    elif repeat.lower() == "да":
        valid_statuses = ["выполнено", "в процессе", "отложено"]
        while True:
            new_status = input("Выберите новый статус (выполнено, в процессе, отложено): ").lower()
            if new_status in valid_statuses:
                status_my_note = new_status
                print(f"Статус заметки изменен на '{status_my_note}'!")
                print("заметка: ", my_note,
                      "\nстатус заметки: ", status_my_note)
                break
            else:
                print("Ошибка: Неверный статус. Пожалуйста, выберите один из предложенных статусов.")
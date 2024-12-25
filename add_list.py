username=input("введите имя пользователя ")
print("имя пользователя", username)
title1=input("введите заголовок заметки №1")
title2=input("введите заголовок заметки №2")
title3=input("введите заголовок заметки №3")
a = [title1, title2, title3]
print("заголовок заметки", a)
content = input("введите описание заметки ")
print("описание заметки", content)
status = input("введите статус выполнения заметки ")
print("статус заметки", status)
created_date = input("введите дату начала в формате день-месяц-год ")
temp_create_date = created_date[0:5]
print("дата создания заметки", temp_create_date)
issue_date = input("введите дату планируемого окончания в формате день-месяц-год ")
temp_issue_date = issue_date[0:5]
print("дата планируемого окончания", temp_issue_date)
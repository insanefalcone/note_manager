username=input("введите имя пользователя ")
title1=input("введите заголовок заметки №1 ")
title2=input("введите заголовок заметки №2 ")
title3=input("введите заголовок заметки №3 ")
a = [title1, title2, title3]
content = input("введите описание заметки ")
status = input("введите статус выполнения заметки ")
created_date = input("введите дату начала в формате день-месяц-год ")
temp_create_date = created_date[0:5]
issue_date = input("введите дату планируемого окончания в формате день-месяц-год")
temp_issue_date = issue_date[0:5]
b = [username,[a], content, status, temp_create_date, temp_issue_date]
print(b)
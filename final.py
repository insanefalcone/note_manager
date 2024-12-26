note = {
     "username": input("введите имя пользователя "),
     "content": input("введите описание заметки "),
     "titles": [input("Введите текст заголовка 1 "), input("Введите текст заголовка 2 "), input("Введите текст заголовка 3 ")],
     "status": input("введите статус выполнения заметки "),
     "created_date": input("введите дату начала в формате день-месяц-год "),
     "issue_date": input("введите дату планируемого окончания в формате день-месяц-год ")}
username = note["username"]
content = note["content"]
titles = note["titles"]
status = note["status"]
created_date = note["created_date"]
issue_date = note["issue_date"]
print("имя пользователя", username)
print("описание заметки", content)
print("текст заголовка", titles)
print("статус", status)
print("дата начала", created_date[0:5])
print("дата планируемого окончания", issue_date[0:5])


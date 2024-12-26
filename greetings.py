import datetime

username = "Артём"
title = "Первая заметка"
content = "Описание в заметке"
status = "В работе"
#created_date = "21-12-2024"
#issue_date = "31-12-2024"
created_date = datetime.date(2024, 12, 21)
issue_date = datetime.date(2024, 12, 21)
temp_created_date = created_date.strftime("%d-%m-%Y")
temp_issue_date = issue_date.strftime("%d-%m-%Y")

# print("Имя пользователя: ",username)
# print("Заголовок заметки: ",title)
# print("Описание заметки: ",content)
# print("Статус заметки: ",status)
# print("Дата создания заметки: ",temp_created_date)
# print("Дедлайн: ",temp_issue_date)
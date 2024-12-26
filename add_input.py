from datetime import datetime
# greetings import *

username = input("Введите ваше имя:")
# title = input("Введите заголовок заметки:")

from add_list import * # ввод заголовков 1 2 3

content = input("Введите текст заметки:")
status = input("Введите статус задачи:")
created_date = datetime.strptime(input("Введите дату начала задачи. Пример: (2024-12-22):"),"%Y-%m-%d")
# print(f"Дата начала задачи: {created_date}")
# print(type(created_date))
issue_date = datetime.strptime(input("Введите дату окончания задачи. Пример: (2024-12-22):"),"%Y-%m-%d")
# print(f"Дата завершения задачи: {issue_date}")

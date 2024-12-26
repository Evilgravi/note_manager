from datetime import datetime
#ввод пользователем переменных
username = input("Введите ваше имя: " )
from add_list import * # ввод заголовков 1 2 3
content = input("Введите текст заметки: ")
status = input("Введите статус задачи: ")
created_date = datetime.strptime(input("Введите дату начала задачи. Пример: (2024-12-22): "),"%Y-%m-%d")
issue_date = datetime.strptime(input("Введите дату окончания задачи. Пример: (2024-12-22): "),"%Y-%m-%d")
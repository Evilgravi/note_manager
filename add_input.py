from datetime import datetime, timedelta,date

#ввод пользователем переменных
username = input("Введите ваше имя: " )
from add_list import * # ввод заголовков 1 2 3
content = input("Введите текст заметки: ")
status = input("Введите статус задачи: ")

date_for_text = date.today().strftime("%Y-%m-%d")# получение текущей даты

created_date = datetime.strptime(input(f"Введите дату начала задачи. Пример: ({date_for_text}): "),"%Y-%m-%d")

date_for_text_new = datetime.strptime(date_for_text,"%Y-%m-%d") + timedelta(days=10) # преобразование в тип даты и добавление 10 дней
date_for_text_new = date_for_text_new.strftime("%Y-%m-%d") # преобразование в строку в нужном виде

issue_date = datetime.strptime(input(f"Введите дату окончания задачи. Пример: ({date_for_text_new}): "),"%Y-%m-%d")
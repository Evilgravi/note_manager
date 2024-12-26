from date_changer import * # Импорт всех переменных
# import pprint
note = {1: f"Имя пользователя  {username}",
        2: f"Заголовки:  {title_list}",
        3: f"Текст заметки: {content}",
        4: f"Статус задачи: {status}",
        5: f"Дата создания: {temp_created_date}",
        6: f"Дата окончания: {temp_issue_date}"
        }

for i in note:
        if i != 2:
                print(note[i])
        else:
                for j in title_list:
                        print(title_list[j])
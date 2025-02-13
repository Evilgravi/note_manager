from multiple_notes import *
from check_deadline import *
cmd_help = """/newzmt - создать новую заметку
/chekzmt - просмотреть заметки
/delzmt - удалить выбранную заметку
/swapstat - изменить статус заметки
/exit - завершить выполнение программы
"""
arg = 1
while arg == 1:
    print(cmd_help)
    # прверка вводов команд и вызов функций
    var_cmd = input("Введите команду: ")
    if var_cmd == "/newzmt":
        add_parametr() # функция из файла multiple_notes.py
    if var_cmd == "/chekzmt":
        # отображение существующих заметок
        if len(note_list) == 0:
            print("Нет введённых заметок, возврат к панели управления.")
            time.sleep(3)
        else:
            for i in range(len(note_list)):
                print(f"Заметка №{i+1}")
                print(f"ID заметки: {note_list[i]["id"]}")
                print(f"Имя пользователя: {note_list[i]["name"]}")
                for b in range(len(note_list[i]["title"])): #запуск цикла по длинне списка
                    if b == 0:
                        print(f"{note_list[i]["title"][b]}")
                    else:
                        print(f"{"\t"* (b - 1)} {note_list[i]["title"][b]}") # отражение ввода с использованием "TAB"
                # print(f"Заголовк заметки: {note_list[i]["title"]}")
                print(f"Текст заметки: {note_list[i]["content"]}")
                print(f"Статус заметки: {note_list[i]["status"]}")
                print(f"Дата создания заметки: {note_list[i]["created_date"]}")
                print(f"Дедлайн заметки: {note_list[i]["issue_date"]}")
                chek_dl(note_list, i)# функция расчёта дедлайна в файле check_deadline.py
            time.sleep(3)
    if var_cmd == "/delzmt":
        del_note(note_list) # функция удаления в файле delete_note.py
    if var_cmd == "/exit":
        arg = 0
    if var_cmd == "/swapstat":
        swap_status(status_list,note_list) # функция смены статуса в файле update_status.py

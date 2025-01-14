from delete_note import *
from add_titles_loop import title_loop
from _datetime import datetime, date
from update_status import *
list_title = ["Заголовки:"]
status_list = {1:"Новая",
               2:"В работе",
               3:"Отложено",
               4:"Выполнено"}
note_list = []
def add_parametr():
    while True:
        name = input("Введите ваше имя: ")
        if name in "":
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    title_loop(list_title)
    while True:
        content = input("Введите текст заметки: ")
        if content in "":
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    status = status_new(status_list)

    print("Дата создания по умолчанию равна текущему дню. Хоти ввести вручную?")
    cmd_date = input("Введите Y - да/N- нет или оставьте пустым: ")
    if cmd_date == "Y":
        while True:
            try:
                created_date = datetime.strptime(input("Введите дату создания в формате дд-мм-гггг: "),"%d-%m-%Y").strftime("%d-%m-%Y")
            except:
                print("Вы ввели дату в не корректном формате, попробуйте ещё раз.")
            else:
                break
    elif cmd_date in "N" or "":
        created_date = date.today().strftime("%d-%m-%Y")
    while True:
        try:
            issue_date = datetime.strptime(input("Введите дату дедлайна в формате дд-мм-гггг: "), "%d-%m-%Y").strftime("%d-%m-%Y")
        except:
            print("Вы ввели дату в не корректном формате, попробуйте ещё раз.")
        else:
            break
    if len(note_list) == 0:
        id_zmt = 1
    else:
        number = len(note_list) - 1
        id_zmt = note_list[number]["id"]+1
    note_dict = {"id": id_zmt,
                "name": name,
                "title": list_title,
                "content": content,
                "status": status,
                "created_date": created_date,
                "issue_date": issue_date}
    note_list.append(note_dict)




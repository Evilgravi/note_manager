import time

def swap_status(status_list,note_list):
    var_swap = []
    tmp_parm = -1
    print("Выберите заметку для смены статуса")
    time.sleep(1)
    # вывод заметок для выбора
    for i in range(len(note_list)):
        print(f"Заметка №{i + 1}")
        print(f"ID заметки: {note_list[i]["id"]}")
        print(f"Имя пользователя: {note_list[i]["name"]}")
        print(f"Первый заголовок: {note_list[i]["title"][1]}")
        # print(f"Заголовк заметки: {note_list[i]["title"]}")
        print(f"Статус заметки: {note_list[i]["status"]}")
    var_select = input("Введите имя, заголовок или ID заметки для выбора: ")
    for i in range(len(note_list)):
        if var_select == note_list[i]["title"]:
            var_swap.append(i)
        elif var_select == note_list[i]["name"]:
            var_swap.append(i)
        elif var_select == str(note_list[i]["id"]):
            var_swap.append(i)
    if len(var_swap) == 0:
        print("Значение не найдено, попробовать ещё раз?")
        arg_YN = input("Y/N для продолжения можно оставить пустым: ")
        if arg_YN == "N":
            return
    if len(var_swap) == 1:
                print(f"""Выбранная заметка: 
        ID заметки: {note_list[var_swap[0]]["id"]}
        Имя пользователя: {note_list[var_swap[0]]["name"]}
        Первый заголовок: {note_list[var_swap[0]]["title"][1]}
        Статус заметки: {note_list[var_swap[0]]["status"]}""")
                time.sleep(1)
                print("доступные статусы для замены:")
                for i in range(len(status_list)):
                    print(f"{i+1}. {status_list[i+1]}")
                stat_new = input("Введите номер или название статуса: ")
                try:
                    stat_new = int(stat_new)
                    note_list[var_swap[0]]["status"] = status_list[stat_new]
                    print(f"Статус успешно изменён на \"{status_list[stat_new]}\"")
                    time.sleep(1)
                except:
                    for i in range(len(status_list)):
                        if stat_new.lower() in status_list[i].lower():
                            note_list[var_swap[0]]["status"] = status_list[i]
                            print(f"Статус успешно изменён на \"{status_list[i]}\"")
                            time.sleep(1)
                else:
                    return
    if len(var_swap) > 1:
        print(f"Под введёный критерий попапдают {len(var_swap)} заметки")
        for i in range(len(var_swap)):
            print(f"""ID заметки: {note_list[var_swap[i]]["id"]}
                Имя пользователя: {note_list[var_swap[i]]["name"]}
                Первый заголовок: {note_list[var_swap[i]]["title"][1]}
                Статус заметки: {note_list[var_swap[i]]["status"]}""")
        while True:
            try:
                var_select = int(input("Введите ID заметки для выбора нужной: "))
            except:
                print("Для ввода доступны только цифры, попробуйте ещё раз")
            else:
                for i in range(len(note_list)):
                    if var_select == note_list[i]["id"]:
                        tmp_parm = i
                if tmp_parm != -1:
                    print(f"""Выбранная заметка: 
                           ID заметки: {note_list[tmp_parm]["id"]}
                           Имя пользователя: {note_list[tmp_parm]["name"]}
                           Первый заголовок: {note_list[tmp_parm]["title"][1]}
                           Статус заметки: {note_list[tmp_parm]["status"]}""")
                    time.sleep(1)
                    print("доступные статусы для замены:")
                    for i in range(len(status_list)):
                        print(f"{i + 1}. {status_list[i + 1]}")
                    stat_new = input("Введите номер или название статуса: ")
                    try:
                        stat_new = int(stat_new)
                        note_list[tmp_parm]["status"] = status_list[stat_new]
                        print(f"Статус успешно изменён на \"{status_list[stat_new]}\"")
                        time.sleep(1)
                    except:
                        for i in range(len(status_list)):
                            if stat_new.lower() in status_list[i].lower():
                                note_list[tmp_parm]["status"] = status_list[i]
                                print(f"Статус успешно изменён на \"{status_list[i]}\"")
                                time.sleep(1)
                    else:
                        return

def status_new(status_list):
    while True:
        print("доступные статусы для ввода: ")
        for i in range(len(status_list)):
            print(f"{i + 1}. {status_list[i + 1]}")
        stat_tmp= input("Введите номер или название статуса: ")
        if stat_tmp in "":
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    try:
        stat_tmp = int(stat_tmp)
        status = status_list[stat_tmp]
        print(f"Статус успешно установлен на \"{status_list[stat_tmp]}\"")
        time.sleep(1)
        return status
    except:
        for i in range(len(status_list)):
            if stat_tmp.lower() in status_list[i].lower():
                status = status_list[i]
                print(f"Статус успешно установлен на \"{status_list[i]}\"")
                time.sleep(1)
                return status
    else:
        return







# # book_help = """Команды для работы:
# #             /help - вывести список команд
# #             /statchek - узнать статус заметки
# #             /statupdat - изменить статус заметки
# #             /statnew - создание нового статуса
# #             /stathelp - узнать возможные варианты ввода для статуса
# #             /exit - завершить выполнение программы"""
# status_list = {1: "В работе",
#                2: "Отложено",
#                3: "Выполнено"}
# statik_var = 0
# dynamic_var = 0
#
#
# while statik_var == 0:
#     var_cmd = input("Введите команду: ")
#     if var_cmd == "/help":
#
#     elif var_cmd == "/statchek":
#         print("Текущий статус заметки: ", status)
#     elif var_cmd == "/statupdat":
#         print("Возможные варианты ввода:")
#         for i in range(len(status_list)):
#             c = i+1
#             print(c,"=", status_list[c])
#         print("Ввод возможен как цифрой так и значением.")
#         stat_update = input("Введите значение статуса: ")
#         if len(stat_update) <= len(str(max(range(len(status_list))))):
#             stat_update = int(stat_update)
#             if stat_update in range(len(status_list)+1):
#                 status_new = status_list[stat_update]
#                 print(f"Статус заметки '{status}' изменён на '{status_new}'")
#                 status = status_new
#         else:
#             for i in range(len(status_list)):
#                 c = i + 1
#                 if stat_update.lower() in status_list.get(c).lower():
#                         status_new = status_list[c]
#                         print(f"Статус заметки '{status}' изменён на '{status_new}'")
#                         status = status_new
#     elif var_cmd == "/statnew":
#         status_new= input("Введите новый статус: ")
#         if status_new != "":
#             c = max(range(len(status_list))) + 2
#             add = {c: status_new}
#             status_list.update(add)
#             print(f"Новый статус, \"{status_new}\" добавлен в словарь")
#         else:
#             print("Вы ничего не ввели")
#     elif var_cmd == "/stathelp":
#         print("Возможные варианты ввода:")
#         for i in range(len(status_list)):
#             c = i + 1
#             print(c, "=", status_list[c])
#     elif var_cmd == "/exit":
#         break
#     else:
#         print("Вы ввели не корректную команду")
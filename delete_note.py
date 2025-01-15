import time
def del_note(note_list):
    # проверка на наличие заметок
    if len(note_list) == 0:
        print("Нет введённых заметок, возврат к панели управления.")
        time.sleep(3)
    else:
        arg_whi = 1
        # запуск отображения заметок
        while arg_whi == 1:
            print("Список заметок:")
            for i in range(len(note_list)):
                print(f"Заметка №{i+1}")
                print(f"ID заметки: {note_list[i]["id"]}")
                print(f"Имя пользователя: {note_list[i]["name"]}")
                print(f"Заголовок заметки: {note_list[i]["title"]}")
            print("Для более точного удаления используйте ID заметки, это позволит удалить только одну заметку")
            title_del = input("Введите заголовок заметки, имя пользователя или ID для выбора удаления. Для отмены используйте команду /exit: ")
            # выход из цикла удаления
            if title_del == "/exit":
                arg_whi=0
                # запуск поиска и удаления по критериям
            for i in range(len(note_list)):
                try:
                    if int(title_del) == int(note_list[i]["id"]):
                        del note_list[i]
                        arg_whi = 0
                        print(f"Заметка с ID: \"{title_del}\" успешно удалена!")
                        time.sleep(3)
                        break
                except:
                        if title_del.lower() == note_list[i]["title"][1].lower():
                            del note_list[i]
                            arg_whi = 0
                            print(f"Заметка(ки) с заголовком: \"{title_del}\" успешно удалена!")
                            time.sleep(3)
                        elif title_del.lower() == note_list[i]["name"].lower():
                            del note_list[i]
                            arg_whi = 0
                            print(f"Заметка(ки) с именем пользователя: \"{title_del}\" успешно удалена!")
                            time.sleep(3)
                # проработка исключения если значение не найдено
            if arg_whi == 1:
                print("Значение не найдено, попробовать ещё раз?")
                arg_YN = input("Y/N для продолжения можно оставить пустым: ")
                if arg_YN == "N":
                    arg_whi = 0
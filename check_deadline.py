from _datetime import datetime
def chek_dl(note_list,i):
    date_now = datetime.today()
    deadline = datetime.strptime(note_list[i]["issue_date"],"%d-%m-%Y") - date_now
    if deadline.days > 0:
        print(f"До дедлайна задачи осталось {deadline.days} дней\n")
    elif deadline.days == 0:
        print(f"Дедлайн задачи сегодня\n")
    else:
        print(f"Задержка дедлайна задачи на {abs(deadline.days)} дней\n")


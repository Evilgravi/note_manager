from _datetime import datetime

q=1
while q==1:
    try:
        issue_date = datetime.strptime(input("Введите дату дедлайна в формате дд-мм-гггг: "),"%d-%m-%Y")
    except:
        print("Вы ввели дату в не корректном формате, попробуйте ещё раз.")
    else: q=0
date_now = datetime.today()
deadline = issue_date - date_now
if deadline.days > 0:
    print(f"До дедлайна задачи осталось {deadline.days} дней")
elif deadline.days == 0:
    print(f"Дедлайн задачи сегодня")
else:
    print(f"Задержка дедлайна задачи на {abs(deadline.days)} дней")


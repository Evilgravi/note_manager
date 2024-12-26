i=1
number_title=1
list_title = ["Заголовки:"]
parm_duplicate = 0
# объявление вводных переменных

print("для завершения ввода заголовков оставьте поле пустым и нажмите enter или введите 'стоп'.")

while i==1: # запуск цикла с вечным условием
    title = input(f"Введите заголовок заметки {number_title}: ") #получение заголовков от пользователя
    if title.lower() not in ["","стоп","stop"]: # условие для выхода из цикла, если поле пустое или содержит стоп то цикл завершится

        for c in range(len(list_title)): # цикл проверки уникальности
            if list_title[c] == title: # проверка уникальности значения
                parm_duplicate = 1 # счётчик дублей
# после отработки цикла проверки уникальности, сверяем результат
        if parm_duplicate == 0:
            list_title.append(title) # заносим его в список если дубликатов нет
            number_title += 1  # нумерация заголовков не изменяется если ввод не прошел проверку уникальности
        else:
            print("Такой заголовок уже существует, попробуйте ввести другой")
            parm_duplicate = 0
    else:
        break # если поле пустое то прерываем цикл

if len(list_title)>1: # проверка на наличие введённых элементов
    for b in range(len(list_title)): #запуск цикла по длинне списка
        print(f"{"\t"* b} {list_title[b]}") # отражение ввода с использованием "TAB"
else:
    print("Вы ничего не ввели.")

import random
def monty_hall(n):
    choices = ['empty', 'empty', 'prize']

    # проверяем вариант с неизменным выбором
    win_count = 0
    for _ in range(n):
        # в начале каждой попытки случайно перемешаем массив
        random.shuffle(choices)
        result = choices[random.randrange(len(choices))]
        if result == 'prize':
            win_count += 1
    # вероятность выиграть - частота выигранных опытов
    #print(win_count/n)

    # проверяем вариант с изменением выбора
    win_count = 0
    for _ in range(n):
        # в начале каждой попытки случайно перемешаем массив
        random.shuffle(choices)
        # первый выбор
        first_choice = random.randrange(len(choices))
        # ведущий открывает дверь с empty
        for i in range(len(choices)):
            if i != first_choice and choices[i] == 'empty':
                host_choice = i
                break
        # делаем второй выбор, меняя первое решение
        for i in range(len(choices)):
            if i != first_choice and i != host_choice:
                result = choices[i]
        if result == 'prize':
            win_count += 1
    # вероятность выиграть - частота выигранных опытов

    return(win_count/n)

year = {
    "1": "31",
    "2": "28",
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31"
    }

def get_day(piple):
    dete_best_day = []
    for i in range(piple):
        month = random.randint(1,12)
        max_day = int(year.get(str(month)))
        day = random.randint(1,max_day)
        dete_best_day.append([month,day])
    return unic_element(dete_best_day)

#Проверка уникальности элементов
def unic_element(arr_element):
    for i in range(len(arr_element)-1):
        for j in range(i+1, len(arr_element)):
            if arr_element[i] == arr_element[j]:
                return True
    return False

def birthday(n, piple):
    luck = 0
    for i in range(n):
        if get_day(piple):
            luck += 1
    return luck/n

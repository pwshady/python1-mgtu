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
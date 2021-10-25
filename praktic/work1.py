import random

words = ["книга", "месяц", "ручка", "шарик", "олень", "носок", "лот", "ом", "лосось", "электростанция", "стул", "синхрофазатрон"]

life = 5

def test_letters(letters, char):
    for let in range(len(letters)):
        if letters[let] == char:
            return True
    return False

def set_let(word,tec_word,char):
    for i in range(len(word)):
        if word[i] == char:
            if i > 0:
                tec_word = tec_word[0:i] + word[i] + tec_word[i+1:]
            else:
                tec_word =  word[0] + tec_word[i+1:]
    return tec_word

def fortune(life,word):
    tec_word = ""
    letters = ""
    for i in range(len(word)):
        tec_word += "\u25A0"

    while life > 0:
        for i in range(len(tec_word)):
            print(tec_word[i], end=" ")
        print()
        char = input("У Вас " + str(life) + " попыток. Введите букву или слово: ")
        if len(char) == 1:
            if not test_letters(letters, char):
                letters += char
                if set_let(word, tec_word, char) != tec_word:
                    tec_word = set_let(word, tec_word, char)
                    life +=1
            else:
                print("Такую букву уже называли")
        else:
            if char == word:
                return True
        if tec_word == word:
            return True
        life -= 1
    return False

def get_word(words):
    word = random.choice(words)
    return word

while life > 0:
    life = int(input("Введите количество попыток или 0 для завершения"))
    if len(words) > 0:
        word = get_word(words)
        words.remove(word)
        if fortune(life,word):
            print("Поздравляем Вы победитель!!!")
        else:
            print("Увы Вы проиграли (:")
    else:
        print("Ups")
        break

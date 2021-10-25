import os
import re

from typing import Text

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        strings = str(file.readlines())
        strings = strings.lower()
        words = re.findall(r'\w+',strings)
    return set(words)

def save_file(name,words):
    with open(name, 'w', encoding='utf-8') as file:
        file.write("Всего уникальных слов: " + str(len(words)) + "\n")
        file.write("=========================\n")
        for word in words:
            file.write(word+"\n")
    
save_file("count.txt", sorted(read_file("data.txt")))
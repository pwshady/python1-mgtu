import re

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        strings = str(file.readlines())
        raw_data = re.findall(r'\d{3} \w+ \w+ \w+ \w+ \d{2}:\d{2}:\d{2}',strings)
        name = "output" + name[5:]
        output_file = open(name, 'w', encoding='utf-8')
        for raw_line in raw_data:
            line = re.findall('\w+',raw_line)
            ready_line = "[" + line[5] + ":" + line[6] + ":" + line[7] + "] - Поезд № " + line[0] + " " + line[2] + " " + line[3]
            output_file.write(ready_line + "\n")
    return #set(words)

read_file("input-5.txt")
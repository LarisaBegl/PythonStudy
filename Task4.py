"""В соответствии со своим вариантом разработать программу для работы с файлами на языке Python.
 Предварительно создать текстовый файл F1 не менее чем из 10 строк и записать в него информацию
 Скопировать из файла F1 в файл F2 все строки, кроме той строки, в которой больше всего гласных букв.
  Напечатать номер этой строки.
 """

import os
#новый файл
newfile = open("New.txt", "w")

# Определяем список гласных букв
vowels = list("аоуэыеяиюёАОУЭЫЕЯИЮЁ")
max_vowels = 0
number = 0
with open("file4.txt", "r") as file:
    for index,line in enumerate(file):
        number = 0
        for i in line:
            if i in vowels:
                number += 1
        if number > max_vowels:
            max_vowels = number
            ind = index

with open("file4.txt", "r") as f:
    for i, line in enumerate(f):
        if i != ind:
            newfile.write(line)
newfile.close()

print("Файл file4.txt скопирован в {} без {} строки".format(newfile.name,ind))

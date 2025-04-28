import os
str_b = "Тест: \n Замена строки в текстовом файле; \n Изменить строку в списке; \n Записать строку в файл \n"

with open("res.txt", "w") as file:
    file.write(str_b)
    print (str_b)

with open("res.txt", "r") as file:
    read_file = file.readlines()

i = int(input("pos1 = "))
while True:
    if 0 < i < len(read_file):
        break
    else:
        i = int(input("уточните pos1 = "))

j = int(input("pos2 = "))
while True:
    if 0 < j < len(read_file):
        break
    else:
        j = int(input("уточните pos2 = "))

read_file[i], read_file[j] = read_file[j], read_file[i]
del read_file[0]
str_new = "".join(read_file)

with open("res.txt", "w") as file:
    file.write(str_new)

print(str_new)


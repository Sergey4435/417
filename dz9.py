n = int(input("Количество студентов: "))
students = []
good_st = []
res = 0
avera = 0

for i in range(n):
    print(i + 1, "-й студент: ", end="")
    name = input()
    surname = input("Фамилия: ")
    ball = int(input("Балл: "))
    res += ball
    students.append({"Name": name, "Surname": surname, "Ball": ball})

avera = res / n

for j in students:
    if j["Ball"] >= avera:
        good_st.append(j["Name"])

print()
print("Средний бал ", int(round(avera, 0)), ". Студенты с баллом выше среднего: ")
for i in good_st:
    print(i)

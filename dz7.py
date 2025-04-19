a = set(input("Введите 1-ю строку: "))
b = set(input("Введите 2-ю строку: "))
a -= b
print("Искомые буквы: ")
a = tuple(a)
c = sorted(a)
for i in c:
    print( i, end=" ")

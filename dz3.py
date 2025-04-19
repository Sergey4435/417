a = input("Vvedite simbol: ")
b = input("Kol-vo: ")
c = input("Direction(0 ili 1): ")

while type(b) is not int:
    try:
        b = int(b)
    except ValueError:
        print("Chislo ne tceloe")
        b = input("Vvedite tceloe chislo: ")


i = 0
while i < int(b):
    if int(c) == 0:
        print(a, end="")
    else:
        print(a)
    i += 1

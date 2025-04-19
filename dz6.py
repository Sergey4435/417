from math import pi
n = int(input("Выберите фигуру (1-прямоугольник 2-треугольник 3-круг): "))
while True:
    if n in (1, 2, 3):
        break
    else:
        n = int(input("Уточните фигуру: "))


def square(x, y):
    return x * y


def triangle(x, y):
    return x * y / 2


def circle(x):
    return pi * x ** 2


if n == 1:
    s = float(input("введите ширину: "))
    h = float(input("введите длину: "))
    res = round(square(s, h), 2)
elif n == 2:
    s = float(input("введите основание: "))
    h = float(input("введите высоту: "))
    res = round(triangle(s, h), 2)
elif n == 3:
    h = float(input("введите радиус: "))
    res = round(circle(h), 2)
else:
    res = "фигура не определена"


print("Площадь фигуры: ", res)

from math import *


class A():
    k = 0

    @staticmethod
    def area(*args):
        if len(args) == 3:
            if isinstance(args[0], int):
                s = (args[0]+args[1]+args[2])/2
                area = sqrt(s*(s-args[0])*(s-args[1])*(s-args[2]))
                A.k += 1
                print(f"Площадь треугольника по формуле Герона {args}: {area}")
            else:
                A.k += 1
                print(f"Площадь треугольника через основание и высоту {args[1:]}: {(args[1]*args[2])/2}")
        if len(args) == 2:
            area = args[0] * args[1]
            A.k += 1
            print(f"Площадь прямоугольника {args}: {area}")
        if len(args) == 1:
            A.k += 1
            area = args[0]**2
            print(f"Площадь квадрата ({args[0]}): {area}")


A.area(3, 4, 5)
A.area("t", 6, 7)
A.area(7)
A.area(2, 6)
print(f"Количество подсчетов площади: {A.k}")


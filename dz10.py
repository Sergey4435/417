S1 = 0


def area(a, b, c):
    def square(d, f):
        return d * f

    S = 2 * (square(a, b) + square(a, c) + square(b, c))
    return S


def area1(a, b, c):
    def square(d, f):
        return d * f

    S = 0
    global S1
    S1 = 2 * (square(a, b) + square(a, c) + square(b, c))
    return S


def area2(a, b, c):
    def square(d, f):
        nonlocal S1
        S1 = 0
        return d * f

    S1 = 2 * (square(a, b) + square(a, c) + square(b, c))
    return S1


print(area(2, 4, 6))  # локальная
area1(5, 8, 2, )
print(S1)  # глобальная
print(area2(1, 6, 8))  # нелокальгая

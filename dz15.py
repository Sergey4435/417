n = [-2, 3, 8, -11, -4, 6]


def counter(lst):
    res = 0
    if len(lst) == 0:
        return 0
    else:
        if lst[0] < 0:
            res += 1
            return res + counter(lst[1:])
        else:
            return counter(lst[1:])


print(n)
print(f"n = {counter(n)}")

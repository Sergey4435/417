def decorator(func):
    def wrap(*args):
        func(*args)
        print(f"Среднее арифметическое чисел {args} = {sum(args) / len(args)}")

    return wrap


@decorator
def fn(*args):
    print(f"Сумма чисел {args}= {sum(args)}")


fn(2, 3, 3, 4)

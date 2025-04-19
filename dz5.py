import random
n = int(input("Vvedite dlinu spiska: "))
mas = [random.randint(-10,10) for i in range(10)]
print(mas)
res = []
for j in mas:
    if j >= 0 and j not in res:
        res.append(j)
print("Новый список, состоящий из положительных элементов: ", res)
print("Наибольший элемент списка: ", max(res))



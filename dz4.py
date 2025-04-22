a = [int(input("-> ")) for i in range(int(input("n: ")))]
print(a)
s = 0
k = 0
for i in a:
    if i != 0:
        s += i
        k += 1
res = s / k
print("Среднее арифметическое ненудевых элементов: ", res)

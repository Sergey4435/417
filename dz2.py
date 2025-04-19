sums = int(input("Введите сумму копеек:"))
sums = sums % 100
if sums % 10 == 1 and sums != 11:
    print(sums, "копейка")
elif 2 <= sums % 10 <= 4 and sums != 12 and sums != 13 and sums != 14:
    print(sums, "копейки")
else:
    print(sums, "копеек")

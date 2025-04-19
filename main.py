# name = "Игорь"
# age = 28
# print ("меня зовут "+name+". Mне "+str(age), end=" ")
# print ("New line")

# name=input("Name: ")
# print("hello, ", name)

# num = int(input("Введите число:"))
# power = input("Степень:")
# res = num**int(power)
# print(res)

# print()

# print(5-3==2 and 1+3==4)

# age = input("Vash vozrast:")
# if int(age) >= 18:
#     print("dostup +")
# else:
#     print("Dostup -")
#
# a = input("1 storona: ")
# b = input("2 storona: ")
# c = input("3 storona: ")
#
# if a == b == c:
#     print("Ravnostoronniy")
# elif a == b or b == c or a == c:
#     print("ravnobedrennyi")
# else:
#     print("raznostri")

# month = int(input("Vvedite #:"))
# if month == 1 or month == 2 or month == 12:
#     print("Zima")
#     if 3 <=month <= 5:
#         print("vesna")
#     if 6 <= month <8:
#         print("leto")
#     if 9 <= month <= 11:
#         print("osen")
# else:
#     print("ne sushestvuet")

# тернарное выражение

# a, b = 10, 20
# print(a if a<b else b)

# a, b = 20, 20
# print("a == b" if a == b else "a > b" if a > b else "a < b")

# Исключения

# a = 0
# b = "2"
# print(a + int(b))

# try:
#     n = int(input("Введите целое число: "))
#     print(n*2)
# except ValueError:
#     print("xnj-nj yt nfr")
#
# print("KOd nizhe")
#
# try:
#     n = int(input("VVedite delimoe: "))
#     m = int(input("VVedite delitel: "))
#     print(n/m)
# except (ValueError, ZeroDivisionError):
#     print("xnj-nj yt nfr")
# else:
#     print("Vse horosho")
# finally:
#     print("End of programme")
# except ZeroDivisionError:
#     print("delenie na  0")

# n = input("VVedite 1 chislo: ")
# m = input("Vvedite 2 chislo: ")
# try:
#     print(int(n)+int(m))
# except ValueError:
#     print(n + m)

# n = input("VVedite 1 chislo: ")
# m = input("Vvedite 2 chislo: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Цикл while

# i = 0
# while i < 5:
#     print("i = ", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i%2 == 0:
#         print(i, end=" ")
#     i += 1

# n = int(input("Введите количество символов: "))
# print("*"*n)
#
# i=0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1
#
#
# a = int(input("Vvedite nachalo: "))
# b = int(input("Vvedite konetc:  "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print ("Summa: ", res)
#
# n = input("Vvedite chislo")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Chislo ne tceloe")
#         n = input("Vvedite tceloe chislo: ")
# if n % 2 == 0:
#     print("Chetnoe")
# else:
# #     print("Nechetnoe")
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nCykl ended!")

# i = 0
# while True:
#     print(i)
# res = 1
# while True:
#     n = int(input("Vvedite chislo: "))
#     if n == 0:
#         break
#     res *= n
#
# print("Rezultat: ", res)
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Ended")

# i = 1
# while  i < 5:
#     print("Vneshniy: i =", i)
#     j = 1
#     while j < 4:
#         print("\tVnutrennyi: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i,"*", j, "=", i*j, end="\t\t")
#         j +=1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j%2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
#
# a = input("Vvedite simbol: ")
# b = input("Kol-vo: ")
# c = input("Direction(0 ili 1): ")
#
# while type(b) is not int:
#     try:
#         b = int(b)
#     except ValueError:
#         print("Chislo ne tceloe")
#         b = input("Vvedite tceloe chislo: ")
#
# i = 0
# while i < int(b):
#     if int(c) == 0:
#         print(a, end="")
#     else:
#         print(a)
#     i += 1


# for i in "Hello", "World":
#     print(i)
# range(start, stop, step)
# print(range(2, 9))
#
# for i in range(10, 0, -1):
#     print(i, end=" ")

# ch = int(input("Введите целое число: "))
# for i in range(1, ch+1):
#     if ch % i == 0:
#         print(i, end=" ")
#
# for i in range(10, 101):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("Tnd of cykle")
#
# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# w = int(input("Введите w: "))
# h = int(input("Введите h: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# st = [i * 2 for i in "Hello"]
# print(st)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (List)

# num = [14, 16, 18, 20, 22, 24, 26, 28, "Hello", True, 2.8]
# print(num)
# print(type(num))
# print(num[0])
# print(num[-1])
# num[0] = 256
# num[1]+=100
# print(num)
#
# print(len(num))

# s = []
# print(s, type(s))
#
# s2 = list("Hello")
# print(s2, type(s2))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + s2
# print(s3*2)

# n = list(range(10, 2, -2))
# print(n)

# a = [i ** 2 for i in range(5)]
# print(a)

# a = [0]*int(input("Vvedite kol-vo elem: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Vvedite kol-vo elem: ")))]

# lst = [5, 9, 8, 2, 3]

# for i in range(len(lst)):
#     print(lst[i], end=" ")
# print()
#
# for i in lst:
#     print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("Vvedite kol-vo elem: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Summa otrits chisel: ", s)
#
# a = [int(input("-> ")) for i in range(int(input("Vvedite kol-vo elem: ")))]
# print(a)
# s=0
# for i in a:
#     if i <0:
#         s += i
# print("Summa patriots chisel: ", s)
#
# n = list(range(21,41))
# print(n)
# s = 0
# k = 0
# for i in range(len(n)):
#     if n[i] % 2 :
#         s += n[i]
#     else:
#         k += 1
#
# print("Chet: ", k)
# print("Nechet: ", s)
#
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
#
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
#
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1,len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")
#
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# j = a[0]
# for i in a:
#     if i > j:
#         print(i, end=" ")
#     j = i
#
# lst = [3, 7, 4, 6, 2]
# print(lst[1:3])
# print(lst[1:])
# print(lst[:4])
# print(lst[::-1])
# print(lst[3:1:-1])
#
# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[0:1])
# print(lst[6:])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "HelloWorld"
# print(st[1:5])
# print(st[::-1])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[2] = 120
# s[10:11] = [200]
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s=0
# k=0
# for i in a:
#     if i != 0:
#         s += i
#         k +=1
# res = s / k
# print("Среднее арифметическое ненудевых элементов: ", res)

# print(dir(list))

# # Методы списка
# s = [5, 20, 120, 1]
# print(s)
# s.append(99) #добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3]) #добавляет список в конец списка
# print(s)
# s.insert(2, 100)#добавляет элемент в список
# print(s)
#
# lst = []
# n = int(input("Kol-vo elem v spiske: "))
# for i in range(n):
#     x = int(input("Vvedite chislo: "))
#     lst.append(x)
#     lst.insert(0, x)
# print(lst)
#
# a = [5,9,2,1,4,3,2,4]
# b = [4,2,1,7,3,2]
# c = []
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# a = [5,9,2,1,4,3,2,4]
# b = [4,2,1,7,3,2]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#
# print(c)
#
# a = [1,2,3,4,5]
# b = [11,22,33]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# s = [5,20,120,200,120]
# print(s)
# s[1:3] = []
# del s[1:3]
# s.remove(120) #удаляет первый элемент из списка
# num = 5
# if num in s:
#     s.remove(num)
# s.pop() #удаляет последний элемент
# s.pop(1) #удаляет по заданному индексу
# ind = 9
# try:
#     num = s.pop(ind)
#     print(num)
# except IndexError:
#     print(ind, "-такого индекса не существует")
# s.clear()
# print(s)
# print("Vvedite elem spiska")
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# print("Vvedite index: ")
# k = int(input("K = "))
# try:
#     a.pop(k)
# except:
#     print(k, "-такого индекса не существует")
# print(a)
#
# s = [5,20,120,200,120]
# print(s)
#
# num = s.count(20)
# print(num)
#
# ind = s.index(200) #Вернет индекс на заданное значение
# print(ind)
#
# a = [1,2,3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
#
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# b.append(200)
# print("a =", a)
# print("b =", b)

# b = [51, 32, 3, 200]
# print(b)
# # b.reverse()
# b.sort(reverse=True)
# print(b)
#
# s = ["VITALII", "Sergey", "Alex", "Anna"]
# print(s)
# s1 = sorted(s, reverse=False)
# print(s1)

# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(0, 9))
# print(random.randrange(2, 10, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# import random
#
# mas = [random.randint(20, 40) for i in range(10)]
# print(mas)
#
# lst = [33, 36, 22, 36, 40, 34, 38, 34, 34, 34]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# import random
# import time

# lst = [random.randint(0,100) for i in range(10)]
# print(lst)
# max_1 = max(lst)
# print("MAX znachenie: ", max_1)
# lst.remove(max_1)
# lst.insert(0, max_1)
# print(lst)

# lst = [random.randint(0,100) for i in range(10)]
# print(lst)
# min_1 = min(lst)
# print("MIN znachenie: ", min_1)
# ind = lst.index(min_1)
# print("INDEX: ", ind)
# del lst[0: ind]
# print(lst)

# import random
#
# n = int(input("Vvedite razmer 1 spiska: "))
# m = int(input("Vvedite razmer 2 spiska: "))
#
# s1 = [random.randint(0, 10) for i in range(n)]
# print(s1)
# s2 = [random.randint(0, 10) for i in range(m)]
# print(s2)
# s3 = []
# 1 zadacha
# s3 = s1 + s2
# print(s3)

# 2 zadacha
# for i in range(len(s1)):
#         if s1[i] not in s3:
#             s3.append(s1[i])
# for i in range(len(s2)):
#     if s2[i] not in s3:
#         s3.append(s2[i])
# print(s3)

# 3 zadacha
# for i in range(len(s1)):
#     if s1[i] in s2 and s1[i] not in s3:
#             s3.append(s1[i])
# print(s3)
# 4 zadacha
# s3 = [min(s1), min(s2), max(s1), max(s2)]
# print(s3)
#
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# #
# # st = ["Hello", "World"]
# # print(st[1][4])
#
# print("Variant 1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print("Variant 2")
# for i in m:
#     # print(i)
#     for j in i:
#         print(j, end="\t\t")
#     print()
# import random
# n = int(input("Vvedite dlinu spiska: "))
# mas = [random.randint(-10,10) for i in range(10)]
# print(mas)
# res = []
# for j in mas:
#     if j >= 0 and j not in res:
#         res.append(j)
# print("Новый список, состоящий из положительных элементов:", res)
# print("Наибольший элемент списка", max(res))

# Modules

# import math
#
# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# import math as m
#
# num1 = m.sqrt(2)
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import *
#
# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import pi
#
# radius = int(input("Vvedite radius: "))
# print("Dlina okruzhnosti: ", round(2 * pi * radius, 2))
#
# import time
# import locale
#
# print(time.time())
# print(time.ctime(542752621))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y."))
# locale.setlocale(locale.LC_ALL, "ru_RU")
# print(time.strftime("Сегодня: %d %B %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(542752621)))
#
# num = 1_000_000.0
# print(num)
#
# pause = 1.5
# print("Running")
# time.sleep(pause)
# print(pause,"sec")

# start = time.time()
# time.sleep(5)
# finish = time.time() - start
# print(finish)

# function


# def hello(name, age):
#     print("Hello", name, "I", age)
#
#
# hello("Irina", 20)
# hello(18, "Ivan")
# def get_sum(a, b):
#     print("Summa chisel:", end="")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# # get_sum(12, 7)
# print(res)

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def test(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(10, 5)
# num1 = 10
# num2 = 5
# if test(num1, num2):
#     print(num1, ">", num2)
# else:
#     print(num1, "<", num2)

#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#     has_special = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_number = True
#         if "!" or "@" or "%":
#             has_special = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number and has_special:
#         return True
#     return False

#
# p = input("Vvedite: ")
# if check_password(p):
#     print("Nadezhnyi")
# else:
#     print("Nenado")

#
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, d=2, c=3))
# print(get_sum(1, 5, d=2, c=3))

#
# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(12, "Ira")
# display_info(age=23, name="Ira")
# display_info("Ira", age=23, name="Ira")
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
# lt1.append(4)
# print(lt1, id(lt1))
# lt1.pop(1)
# print(lt1, id(lt1))

# s = "Hello"
# print(s, id(s))
# s = s + "!"
# print(s, id(s))
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

#
# def test(lst):
#     lst.append(4)
#
#
# x = [1, 2, 3]
# print(test(x))
# print(x)
#
#
# def test1(n):
#     n = 5
#
# x1 = 3
# print(test1(x1))
# print(x1)

# Кортежи
#
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50

# a = ()
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))

# a = (1, 2, 3, 4, 5, 6)
# print(a, type(a))
# print(a[2])
# print(a[1:4])

#
# s = tuple(int(input("-> ")) for i in range(5))
# print(s)

# from random import randint
#
# s = [randint(50,100) for i in range(5)]
# print(s)
#
# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# if a in t3:
#     print(t3.index("a"))
#
# for i in t3:
#     print(i, end=" ")
#
#
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first+1)
#             return tpl[first:second+1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))

#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5,0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))
#
#
# point = (20, 14)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координате 0, 0")
#     case (x, 0):
#         print("Точка находится в", x, 0)
#     case (0,y):
#         print(0, y)
#     case (x, y):
#         print(x, y)
#     case _:
#         print("None")

#
# t = (10, "Python", (1, 2, 3), ["hello"])
# print(t)
# t[4][0] = "new"
# print(t)
# t[4].append("hi")
# print(t)

#   Распаковка кортежа
#
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)


# t = (1,2,3)
# del t
# print(t)

# t = (1, 2, 3, 4, 5)
# print(t, type(t))
# lst = list(t)
# print(lst, type(lst))
# lst.append(6)
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
#
# countries = (
#     ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
#     ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
# )
# print(countries, end="\n\n")
#
# for county in countries:
#     county_name, county_population, cities = county
#     print("\nCountry: ", county_name, county_population)
#     for city in cities:
#         city_name, city_population = city
# #         print(city_name, city_population)
#
#
# s = input("Введите по порядку: ")
# tpl = tuple(s)
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if not tpl[i] in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Summ", lst[i], "=", tpl.count(lst[i]))


# Множество (set)

# s = {"one", "two", "three", "one"}
# # print(s)
# for i in s:
#     print(i)

# a = {}
# print(a, type(a))
#
# b = set("Hello")
# print(b, type(b))
# s = list(b)
# print(s)

# s = {input("-> ") for x in range(10)}
# print(s)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if 'a' in i])
# # print(tuple(i for i in lst if 'a' in i))
# # print({i for i in lst if 'a' in i})
# print(['A'+i[1:] if i[0] == 'a' else 'B'+i[1:] for i in lst if i[1]=='c'])

# s = {"one", "two", "three"}
# s.add("four")
# print(s)
# s.remove("four")
# print(s)
#
# el = "two"
# if el in s:
#     s.remove(el)
#
# print(s)
# s.discard("five")
# print(s)

# el = s.pop()
# print(s)
# print(el)

# s.clear()
# print(s)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# c = a.union(b)
# c = a | b
# a |= b
# print(a)
#
# c = a & b
# a &= b
# print(c)
# c = a - b
# a -= b
# print(c)
# print(a)


# s1 = "Hello"
# s2 = "How are you"
#
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
#
# print(a >= b)
# print(a <= b)


#  Словарь (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(lst, type(lst))
# print(d, type(d))
# print(lst[1])
# print(d["two"])
# d["two"] = 200
#
#
# d = {}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))
#
#
# def func(one, two):
#     return one, two
#
#
# print(func(two=2, one=1))

# lst = [["one", 1], ["two", 2], ["three", 3]]
#
# print(dict(lst))

# d = {0: "text", "one": 1, (1, 2): "cortage", "list": [5, 6, 7] }
# d = {0: "text", True: 1, (1, 2): "cortage", "list": [5, 6, 7], 1: 10, False: 0}
# print(d)

# d = {i*2: i**2 for i in range(7)}
# print(d)
# from random import randint
#
#
# d = {randint(1,10): input("->") for i in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# # print("one" in d)
# # print(2 in d)
# try:
# #     print(d["two"])
# # except KeyError:
# #     print("No collectiomn")
# print(d)

# for i in d:
#     print(i, d[i])

# d = {}
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}
# print(d)
# q = int(input("Which elem: "))
# del d[q]
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# print(len(d))
#
# goods = {
#     "1": ["Core-i3-4300", 9, 4500],
#     "2": ["Core-i3-4570K", 3, 8500],
#     "3": ["AMD FX-6300", 4, 3700],
#     "4": ["PENTIUM G3220", 5, 2100],
#     "5": ["Core-i5-3450", 6, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], "-", goods[i][1], "in po", goods[i][2], sep=" ")
#
# while True:
#     n = input("#: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Summ: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Number")
#         else:
#             print("Incorrect")
#     else:
#         break
#
#     for i in goods:
#         print(i, ") ", goods[i][0], "-", goods[i][1], "in po", goods[i][2], sep=" ")

# # print(dir(dict))
# d = {"one": 1, "two": 2, "three": 3}
#
# # print(list(d.keys()))
# # print(d.values())
# # print(list(d.items()))
#
# for i in d:
#     print(i, end=" ")
# print()
# for i in d.keys():
#     print(i, end=" ")
# print()
# for i in d.values():
#     print(i, end=" ")
# print()
# for i in d.items():
#     print(i, end=" ")
# print()
# for i, j in d.items():
#     print(i, ":", j)
#
# d = {"one": 1, "two": 2, "three": 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d2["two"] = 200
# print("D =", d)
# print("D2 =", d2)
# d["four"] = 4
# print("D =", d)
# print("D2 =", d2)

# d = {"one": 1, "two": 2, "three": 3}

# value = d.get("three1", "No")
# value = d.get("three1", False)
# value = d.pop("two", "No")
# item = d.popitem()
# print(item)
# d.clear()

# item = d.setdefault("four", 4)
# print(item)

# d2 = {"four": 4, "five": 5}
# print(d2)
# d3 = d | d2
# print(d3)
#
# d.update(d2)
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "NewYork"}
#
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
# d["location"] = d.pop("city")
#
# print(d)
# print(new_d)
#
# s = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#         },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(s)
#
# for x in s:
#     print(x)
#     for y in s[x]:
#         print(y, ":", s[x][y])
# print()
# for x, y in s.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j)


# d = {"one": 1, "two": 2, "three": 3, "four": 4}
# print({key: value for key, value in d.items()})
# print({value: key for key, value in d.items()})
# print({key: value for key, value in d.items() if value <= 2})

# d = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(list(d))

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# #  zip()
#
# a = ["December", "January", "February"]
# b = [12, 1, 2]
#
# print(dict(zip(b, a)))
# print(list(zip(a, b)))
#
# month = [('December', 12), ('January', 1), ('February', 2)]
# a, b = zip(*month)
# print(a)
# print(b)


# one = {"name": "Irina", "surname": "Petrova", "job": "Consulant"}
# two = {"name": "Igor", "surname": "Vetrov", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, v1)
#     print(k2, v2)
# print(sorted(one.items()))
#
# letters = ['b', 'c', 'a', 'd']
# numbers = [3, 4, 1, 2]
#
# lst = list(zip(numbers, letters))
# print(lst)
# lst.sort()
# print(lst)
# print(dict(lst))
# print({v: k for k, v in lst})

# one = {"one": 1, "two": 2}
# two = {"three": 3, "four": 4}
#
# print({**one, **two})
#
# a = ["January", "February", "March"]
# i = 1
# for value in a:
#     print(i, ")", value)
#     i+=1
# print()
# for i, value in enumerate(a, 1):
#     print(i, ")", value)
#
# one = {"one": 1, "two": 2}
#
# for i, (k, v) in enumerate(one.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

#
# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7))
# print(func())
#
# def summ(*params):
#     res = 0
#     for i in params:
#         res+=i
#     return res
#
#
# print(summ(1,2,3,4,5,6,))


# def search(*args):
#     average = sum(args) / len(args)
#     print(average)
#
#     res = []
#     for num in args:
#         if num < average:
#             res.append(num)
#     return res
#
#
# print(search(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(search(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, *args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, ))

# def print_scors(student, *scores):
#     print("student Name: ", student, end=". Score: ")
#     for score in scores:
#         print(score, end=". ")
#     print()
#
#
# print_scors("Irina", 100, 95, 88, 92, 99)
# print_scors("Igor", 96, 20, 33, 36)
# print_scors("Nikita")

#
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def info(**data):
#     for k, v in data.items():
#         print(k, ": ", v, sep="")
#     print("\n")
#
#
#
# info(name="Irina", surname="Vertova", age=22, phone="22-33-44")
# info(name="Igor", sage=25, phone="22-33-44", email="igor@mail.ru")


# def func(a, b, *args, m=100, **kwargs):
#     print(args[0])
#     return a, args, m, kwargs
#
#
# print(func(1, 2, 3, 4, 5, 6, c=22, d=54, e=79, m=200))

# # области видимости (scope)
#
# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Same"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# bye()
# hi()
# bye()

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# # [5, 7, 9]
#
# new_list = list(map(lambda x, y: x + y, l1, l2))
# print(new_list)

# t = ("abcd", "abc", "asdfg", "asd", "dfg")
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# # t2 = tuple(map(lambda s: len(s) == 3, t))
#
# print(t2)

# b = [44, 54, 66, 43, 78, 89]
# res = list(filter(lambda s: s > sum(b)/len(b), b))
# print(res)


# Декораторы

# def hello():
#     return "Hello, i am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, i am super_func")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, i am func 'hello'"
#
#
# test = hello
# print(type(test))
# print(test())

# def my_decorator(func):
#     def inner():
#         print("Код до")
#         func()
#         print("Код после")
#     return inner
#
#
# def func_test():
#     print("Hello, i am func_test")


# test =  my_decorator(func_test)
# test()
#
# def my_decorator(func):     # декорирующая функция
#      def inner():
#          print("Код до")
#          func()
#          print("Код после")
#      return inner
#
#
# @my_decorator     # декоратор
# def func_test():                         # декорируемая функция
#      print("Hello, i am func_test")
#
#
# func_test()
#
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap


#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())
#
#
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Incer", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# @cnt
# def world():
#     print("world")
#
#
# hello()
# hello()
# world()
# hello()
# world()

#
# def outer(fn):
#     def wrap(arg1, arg2):
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")

#
# def outer(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         fn(*args, **kwargs)
#         print("kwargs", kwargs)
#
#     return wrap
#
#
# @outer
# def print_students(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_students("Борис", "Елизавета", "Игорь", study="Java")
# print_students("vladimir", "Sergey", "Marry")

#
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма: ", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
# def multiply(arg):
#     def outer(fn):
#         def inner(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return inner
#
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
#
# def typed(*args, **kwargs):
#     def wraper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Uncorrect")
#
#             for k in kwargs:
#                 if type(f_kwargs[k] is not kwargs[k]):
#                     raise TypeError("Uncor")
#
#             return fn(*f_args, **f_kwargs)
# 
#         return wrap
#
#     return wraper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, str)
# def typed_fn3(x, y, z="hello"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5, ))
# print(typed_fn2("hello", "world", "hello", ))
# print(typed_fn3("hh", "ee", "hello"))
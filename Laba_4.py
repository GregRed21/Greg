# # 1) Задание 1: Создайте модуль с функцией, которая принимает
# # на вход два числа и возвращает их сумму. Используйте эту функцию в основной программе.
# import modul_func
# a = int(input('Enter the first num: \n'))
# b = int(input('Enter the second num: \n'))
# q = modul_func.func_sum(a,b)
# print(f'The result of the sum: {q}')
# # Задание 2: Создайте пакет, который будет содержать модуль с функцией
# # для вычисления факториала числа и модуль с функцией
# # для нахождения наибольшего общего делителя двух чисел.
# # Используйте эти функции в основной программе.
# import Paccket
# a = int(input('Enter the first num: \n'))
# b = int(input('Enter the second num: \n'))
# c = int(input('Enter the third num: \n'))
# q = Paccket.Fuctorial.fuctorial(a)
# print(f'Factorial = {q}')
# w = Paccket.NOD.nod(b, c)
# print(f'Наибольший общий делитель чисел {b} и {c} = {w}')
# # 3) Создайте модуль с функцией для генерации случайного числа от 1 до 10.
# # Используйте эту функцию в основной программе
# # для генерации случайного числа и вывода его на экран.
# import modul_random
# a = int(input('Enter the first num: \n'))
# b = int(input('Enter the second num: \n'))
# print(modul_random.get_random(a, b))
# # 4) Cоздайте пакет, который будет содержать модуль с функцией для проверки,
# # является ли число простым, и модуль с функцией для нахождения всех делителей числа.
# # Используйте эти функции
# # в основной программе для проверки нескольких чисел на простоту и вывода их делителей.
# import Packet_4
# a = int(input('Enter the first num: \n'))
# b = int(input('Enter the second num: \n'))
# c = int(input('Enter the third num: \n'))
# print(Packet_4.simple_num(a))
# print(Packet_4.delitel(a))
# print(Packet_4.simple_num(b))
# print(Packet_4.delitel(b))
# print(Packet_4.simple_num(c))
# print(Packet_4.delitel(c))

# # 5) Создайте модуль с функцией для перевода градусов Цельсия в градусы Фаренгейта и наоборот.
# # Используйте эту функцию в основной программе для перевода нескольких температурных значений.
# import Modul_Gradus
# a = int(input('Введите градусы Цельсия: \n'))
# b = int(input('Введите градусы Фаренгейта: \n'))
# c = int(input('Введите градусы Цельсия: \n'))
# d = int(input('Введите градусы Фаренгейта: \n'))
# print(Modul_Gradus.gradus(a, b))
# print(Modul_Gradus.gradus(c, d))

# # 6) Задание 6: Напишите программу, которая генерирует случайное число от 1 до 100
# # с помощью модуля random и запрашивает у пользователя его предположение.
# # Если предположение больше сгенерированного числа,
# # программа должна вывести "Меньше", если меньше - "Больше", если равно - "Вы угадали!".
# from random import randint
# q = int(input('Введите и угадайте число: \n'))
# a = randint(1,100)
# if q == a:
#     print(f'Вы угадали, ваше число {q} совпало со сгенерированным числом {a}')
# elif q>a:
#     print(f'Ваше число {q} больше сгенерированного числа {a}')
# else:
#     print(f'Ваше число {q} меньше сгенерированного числа {a}')

# # 7) Задание 7: Напишите программу, которая генерирует случайный пароль из 8 символов
# # (буквы и цифры) с помощью модуля random и выводит его на экран.
# from random import randint
# import random
# from string import ascii_letters
# a = [randint(1,9) for x in range(4)]
# q = ''
# u = 0
# for y in a:
#     q+=str(a[u])
#     u+=1
# alphabet = [random.choice(ascii_letters) for i in range(4)]
# w = (''.join(alphabet))
# print(q+w)

# # 8) Напишите программу, которая генерирует случайную последовательность из 10 букв английского алфавита
# # с помощью модуля random и выводит ее на экран.
# import random
# from string import ascii_letters
# print(''.join([random.choice(ascii_letters) for i in range(10)]))

# # 9) Напишите программу, которая генерирует случайную последовательность из 5 чисел от 1 до 50
# # с помощью модуля random и выводит ее на экран.
# # Затем программа должна запрашивать у пользователя пять чисел
# # и выводить на экран количество угаданных чисел.
# from random import randint
# a = [randint(1,50) for x in range(5)]
# q = int(input('Введите первое число: \n'))
# w = int(input('Введите второе число: \n'))
# e = int(input('Введите третье число: \n'))
# r = int(input('Введите четвертое число: \n'))
# t = int(input('Введите пятое число: \n'))
# y = []
# y.append(q)
# y.append(w)
# y.append(e)
# y.append(r)
# y.append(t)
# print(y)
# print(a)
# count=0
# for i in a:
#     for u in y:
#         if i==u:
#             count+=1
# if 1==count:
#     print(f'Вы угадали всего {count} число')
# elif 2<=count<=4:
#     print(f'Вы угадали всего {count} числа')
# elif count==5:
#     print(f'Вы угадали все числа')
# else:
#     print(f'Вы ничего не угадали')

# # 10) Напишите программу, которая генерирует случайную последовательность
# # из 20 чисел от 1 до 10 с помощью модуля random
# # и выводит на экран количество повторяющихся чисел.
# from random import randint
# a = [randint(1,10) for x in range(20)]
# print(a)
# count=[]
# for i in a:
#     for y in a:
#         if i==y:
#             count.append(i)
# set_count=set(count)
# count_true=len(set_count)
# print(f'Количество повторяющихся чисел: {count_true}')
# print(f'Количество повторяющихся чисел: {len(set(a))}')

# # 11) Создайте функцию, которая принимает на вход число и возвращает
# # его квадратный корень с помощью модуля math.
# # Используйте эту функцию в основной программе для вычисления корня из нескольких чисел.
# import math
# a = int(input('Введите первое число: \n'))
# def sqrt(a):
#     return math.sqrt(a)
# print(sqrt(a))

# # 12) Создайте функцию, которая принимает на вход два числа и возвращает их сумму квадратов
# # с помощью модуля math.
# # Используйте эту функцию в основной программе для вычисления суммы квадратов нескольких чисел.
# import math
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# def sum_sqrt(a,b):
#     return math.sqrt(a)+math.sqrt(b)
# print(sum_sqrt(a,b))

# # 13) Создайте функцию, которая принимает на вход число и возвращает
# # его факториал с помощью модуля math.
# # Используйте эту функцию в основной программе для вычисления факториала нескольких чисел.
# import math
# a = int(input('Введите первое число: \n'))
# def factorial(a):
#     return math.factorial(a)
# print(factorial(a))

# # 14) Создайте функцию, которая принимает на вход два числа и возвращает их
# # наибольший общий делитель с помощью модуля math.
# # Используйте эту функцию в основной программе для вычисления НОД нескольких пар чисел.
# import math
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# def NOD(a,b):
#     return math.gcd(a,b)
# print(NOD(a,b))

# # 15) Создайте функцию, которая принимает на вход число и возвращает его синус с помощью модуля math.
# # Используйте эту функцию в основной программе для вычисления синуса нескольких углов в градусах.
# import math
# a = int(input('Введите угол в градусах: \n'))
# def sinus(a):
#     a = math.radians(a)
#     return math.sin(a)
# print(sinus(a))

# # 16) Задание 16: Создайте график функции y = x^2 с помощью модуля Matplotlib.
# # Настройте оси координат и подпишите график.
#
# import matplotlib.pyplot as plt
#
# a = int(input('Введите значение: \n'))
# y = [q for q in range(1, a)]
# x = [w**2 for w in y]
# print(y, x)
# plt.plot(x, y)
# plt.xlabel('Ось х') #Подпись для оси х
# plt.ylabel('Ось y') #Подпись для оси y
# plt.title('График функции') #Название
# plt.show()

# # 17) Создайте столбчатую диаграмму, отображающую количество продаж по месяцам в году.
# # Используйте модуль Matplotlib для создания диаграммы и pandas для загрузки данных.
# import matplotlib.pyplot as plt
# import pandas as pd
# from random import randint
# x=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
# y = [randint(100, 500) for q in range(13)]
# month = {}
# for i in range(len(x)):
#     month[x[i]] = y[i]
# month_xy = pd.Series(month)
# plt.title('Количество продаж по месяцам')
# plt.plot(month_xy)
# plt.show()

# # 18) Создайте круговую диаграмму, отображающую соотношение продаж разных товаров в магазине.
# # Используйте модуль Matplotlib для создания диаграммы и pandas для загрузки данных.
# import matplotlib.pyplot as plt
# import pandas as pd
# from random import randint
# x=["Молоко", "Печенье", "Йогурт", "Творог", "Курица"]
# y = [randint(100, 500) for q in range(6)]
# tovary = {}
# for i in range(len(x)):
#     tovary[x[i]] = y[i]
# tovary_xy = pd.Series(tovary)
# plt.title('Соотношение продаж разных товаров')
# plt.pie(tovary_xy, labels=tovary_xy.index,autopct='%1.1f%%')
# plt.show()

# # 19) Создайте scatter plot, отображающий зависимость роста и веса людей.
# # Используйте модуль Matplotlib для создания графика и pandas для загрузки данных.
# import matplotlib.pyplot as plt
# import pandas as pd
# from random import randint
# x=[randint(160, 210) for q in range(7)]
# y = [randint(60, 120) for w in range(7)]
# bubble_sizes = [randint(30, 300) for e in range(7)]
# x.sort()
# y.sort()
# rost_wes = {}
# for i in range(len(x)):
#     rost_wes[x[i]] = y[i]
# rost_wes_xy = pd.Series(rost_wes)
# print(rost_wes_xy)
# plt.title('Зависимость роста и веса')
# plt.xlabel("Рост")
# plt.ylabel("Вес")
# plt.scatter(rost_wes_xy.index, rost_wes_xy, s=bubble_sizes, alpha=0.7, edgecolors='b', linewidths=3)
# plt.show()

# # 20) Загрузите данные из файла Excel с помощью pandas и выведите первые 5 строк таблицы.
# import pandas as pd
#
# ef = pd.read_excel('Kexcel.xlsx')
# print(ef.head(5))
# print(ef['Протяженность, км'])

# # 21) Задание 21: Отобразите статистическую информацию о таблице, используя метод describe().
# import pandas as pd
#
# ef = pd.read_excel('Kexcel.xlsx')
#
# print(ef.describe())

# 22) Отфильтруйте таблицу, оставив только строки, у которых значение в столбце "Возраст" больше 30.
#
# import pandas as pd
#
# ef = pd.read_excel('Kexcel.xlsx')
#
# print(ef['Возраст'])
#
# for i in ef['Возраст']:
#     if i>30:
#         print(i)

# # 23) Отсортируйте таблицу по значению в столбце "Зарплата" по убыванию.
# import pandas as pd
#
# ef = pd.read_excel('Kexcel.xlsx')
# print(ef)
# print(ef.sort_values('Зарплата', ascending=False))

# # 24) Создайте новый столбец "Индекс массы тела" на основе значений в столбцах "Рост" и "Вес".
# import pandas as pd
# from xlsxwriter import Workbook
# from openpyxl import Workbook
# ef = pd.read_excel('Kexcel.xlsx')
# rost=[]
# wes=[]
# for i in ef['Рост']:
#     rost.append(i)
# for i in ef['Вес']:
#     wes.append(i)
# print(wes)
# print(rost)
# index_mass=[i/(y**2) for i,y in zip(rost,wes)]
# print(index_mass)
# df=pd.DataFrame({'Индекс массы тела':index_mass})
# x = [ef, df]
# ef = pd.concat(x, axis = 1)
# writer=pd.ExcelWriter('Kexcel.xlsx', engine='xlsxwriter' )
# ef.to_excel(writer, sheet_name='List1')
# writer.close()
#
# # index_masss=[rost[i]/(wes[i]**2) for i in range(0, len(rost))]
# # print(index_masss)
# # excel_header = ['Индекс массы тела']
# # data=[index_mass]
# # df=pd.DataFrame(data, columns=excel_header)
# # writer=pd.ExcelWriter('Kexcel.xlsx', engine='openpyxl')
# # df.to_excel(writer, sheet_name='List2')
# # writer.close()

# 25) Создайте гистограмму,
# отображающую распределение оценок студентов по математике.
# Используйте модуль Matplotlib для создания гистограммы и pandas для загрузки данных.
# import pandas as pd
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# from random import randint
# x=["Гриша", "Женя", "Миша", "Саша", "Маша", "Петя", "Федя"]
# y = [randint(0, 10) for q in range(8)]
# Ocenki_matan = {}
# for i in range(len(x)):
#     Ocenki_matan[x[i]] = y[i]
# print(Ocenki_matan)
# df = pd.DataFrame(Ocenki_matan, index=['Баллы'])
# print(df)
# hist = df.hist()
# plt.title('Распределение оценок по математике')
# plt.xlabel('Студенты')
# plt.ylabel('Оценки')
# plt.show()
#
# # n_bins=len(df)
# # fig, axs = plt.subplot(1,2)
# # axs[0].hist(df['Студенты'], bins=n_bins)
# # axs[0].set_title('sepal length')
# # axs[1].hist(df['Баллы'], bins=n_bins)
# # axs[1].set_title('petal length')
# # plt.show()
# df.plot.hist()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('Студенты.xlsx')
print(df.head())
fig,ax=plt.subplot()
df.hist(df['Баллы'])
plt.show()
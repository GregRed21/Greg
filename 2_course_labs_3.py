# # Задание 1: Напишите программу, которая выводит на экран 
# # все числа от 1 до 10 с помощью цикла while
# i=0
# while i<10:
#     i+=1
#     print(i)
# # 2) Напишите программу, которая запрашивает у пользователя число и выводит
# # на экран все числа от 1 до введенного числа с помощью цикла while.
# q = int(input('Введите число: \n'))
# i = 1
# while i<(q+1):
#     print(i)
#     i+=1
# # 3) все четные числа от 1 до введенного числа с помощью цикла while.
# q = int(input('Введите число: \n'))
# i = 1
# while i<(q+1):
#     if i % 2 == 0:
#         print(i)
#     i+=1
# # 4) сумму всех чисел от 1 до введенного числа с помощью цикла while.
# q = int(input('Введите число: \n'))
# i = 1
# w = []
# while i<(q+1):
#     w.append(i)
#     i+=1
# print(w)
# print(sum(w))
# # 5) его факториал с помощью цикла while.
# q = int(input('Введите число: \n'))
# i = 1
# w = 1
# while i<(q+1):
#     w*=i
#     i+=1
#     print(w)
# # 6)  Напишите программу, которая выводит на экран 
# # таблицу умножения от 1 до 10 с 
# # помощью двойного цикла.
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i*j:4}', end=' ')
#     print()
# # 7) выводит на экран таблицу умножения от 1 до 
# #введенного числа с помощью двойного цикла
# a = int(input('Введите число: \n'))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print(f'{i*j:4}', end=' ')
#     print()
# # 8)Создайте двумерный массив размером 3 на 4 
# # и заполните его случайными числами от 1 
# # до 10. Найдите сумму элементов массива 
# from random import randint
# n = int(input('Введите число строк: \n'))
# m = int(input('Введите число столбцов: \n'))
# massiv = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         massiv[i][j]=randint(1,10)
# for i in range(n):
#     for j in range(m):
#         print(massiv[i][j], end=' ')
#     print()
# print('Сумма элементов массива:')
# s=0
# for i in range(n):
#     for j in range(m):
#         s+=massiv[i][j]
# print(s)
# # 9)Создайте двумерный массив размером 5 на 5 
# # и заполните его случайными числами от 0 
# # до 9. Найдите максимальный элемент в каждой строке
# # и выведите результат в виде списка
# from random import randint
# n = int(input('Введите число строк: \n'))
# m = int(input('Введите число столбцов: \n'))
# massiv = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         massiv[i][j]=randint(0,9)
# for i in range(n):
#     for j in range(m):
#         print(massiv[i][j], end=' ')
#     print()

# t = []
# r=0
# max_elem = massiv[0][0]
# while r<n:
#     for j in range(m):
#         if massiv[i][j]>max_elem:
#             max_elem = massiv[i][j]
#         r+=1

# s_max = [(i,j) for i in range(n) for j in range(m) if massiv[i][j] == max_elem]
# line, column = s_max[0]
# print('Максимальный элемент: ', max_elem)
# print('Строка:', line, 'Столбец:', column)
# print('Максимальные элементы в сроках:')
# t.append(massiv)
# u=[]
# for y in t[0]:
#     max_max=max(y)
#     u.append(max_max)
# print(u)

# # 10) Создайте двумерный массив размером 6 на 6 и заполните его случайными числами от 
# # 1 до 100. Отсортируйте каждую строку по возрастанию и выведите результат в виде таблицы.
# from random import randint
# n = int(input('Введите число строк: \n'))
# m = int(input('Введите число столбцов: \n'))
# q=[]
# massiv = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         massiv[i][j]=randint(1,100)
# for i in range(n):
#     massiv[i].sort()
# for i in range(n):
#     print(massiv[i])



# # 11)  Создайте двумерный массив размером 7 на 7 и заполните его случайными числами от 
# # -10 до 10. Найдите сумму элементов массива, находящихся на главной диагонали.
# from random import randint
# n = int(input('Введите число строк: \n'))
# m = int(input('Введите число столбцов: \n'))
# q=[]
# massiv = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         massiv[i][j]=randint(-10,10)
# for i in range(n):
#     for j in range(m):
#         print(massiv[i][j], end=' ')
#     print()
# for i in range(n):
#     for j in range(m):
#         if i==j:
#             q.append(massiv[i][j])
# print(q)
# print(sum(q))


# # 12) Создайте двумерный массив размером 8 на 8 и заполните его случайными числами от 
# # 1 до 100. Найдите максимальный элемент в каждом столбце и выведите результат в виде списка.
# from random import randint
# n = int(input('Введите число строк: \n'))
# m = int(input('Введите число столбцов: \n'))
# massiv = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         massiv[i][j]=randint(1,100)
# for i in range(n):
#     for j in range(m):
#         print(massiv[i][j], end=' ')
#     print()

# t = []
# r=0
# max_elem = massiv[0][0]
# while r<n:
#     for j in range(m):
#         if massiv[i][j]>max_elem:
#             max_elem = massiv[i][j]
#         r+=1


# s_max = [(i,j) for i in range(n) for j in range(m) if massiv[i][j] == max_elem]
# line, column = s_max[0]
# print('Максимальный элемент: ', max_elem)
# print('Строка:', line, 'Столбец:', column)
# print('Максимальные элементы в столбцах:')
# t.append(massiv)
# u=[]
# for y in t[0]:
#     max_max=max(y)
#     u.append(max_max)
# print(u)

# # 13)
# cities=('Moscow', 'Serpuhov', 'Himki')
# print('Кортеж из трех городов:', cities)

# # 14)Задание 14: Напишите программу, которая создает кортеж из пяти элементов 
# # (имена студентов) и 
# # выводит на экран только первый и последний элементы.

# name_stud = ('Гриша','Никита','Женя','Маша','Света')
# print(name_stud[0])
# print(name_stud[-1])

# # Задание 15: Напишите программу, которая создает кортеж из десяти элементов (числа) и выводит 
# # на экран только четные числа.

# num=(1,2,3,4,5,6,7,8,9,10)
# for i in num:
#     if i % 2 == 0:
#         print(i)


# # Задание 16: Напишите программу, которая создает кортеж из пяти элементов (фамилии людей) и 
# # запрашивает у пользователя номер элемента, который нужно удалить из кортежа. После удаления 
# # элемента программа должна вывести оставшиеся элементы кортежа на экран.

# surnames = ('Ильин', "Дованков", "Добрый", "Сдобнов", "Гришин")

# q = int(input('Введите номер элемента, который нужно удалить (от 1 до 5): \n'))

# if 1<=q<=5:
#     q-=1
#     surnames=list(surnames)
#     del surnames[q]
#     new_surnames=tuple(surnames)
#     print('Оставшиеся элементы: ', new_surnames)
# else:
#     print('Введите другую цифру')


# # Задание 17: Напишите программу, которая создает два 
# # кортежа из пяти элементов каждый (числа) 
# # и выводит на экран только те элементы, которые есть в обоих кортежах.

# t_1=(1,2,3,4,5)
# t_2=(3,4,5,6,7)

# set1=set(t_1)
# set2=set(t_2)

# inter=set1.intersection(set2)

# print('Элементы, которые есть в обоих кортежах:')
# for e in inter:
#     print(e)
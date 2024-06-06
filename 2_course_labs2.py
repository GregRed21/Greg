# #1) Пользователь вводит 2 числа, вычислить sqrt(x-sqrt9(y))
# import math
# x = int(input('Введите первое число: \n'))
# y = int(input('Введите второе число: \n'))
# print(math.sqrt(x-math.sqrt(y)))
# # 2) Дано число. Если оно больше 3, то увеличить число на 10, иначе уменьшить на 10.
# x = int(input('Введите первое число: \n'))
# if x > 3:
#     print(x+10)
# else:
#     print(x-10)
# # 3) Дано число. Если оно меньше 7, то вывести Yes, если больше 10, то вывести No, если равно 9, то вывести Error.
# x = int(input('Введите первое число: \n'))
# if x < 7:
#     print('Yes')
# elif x > 10:
#     print('No')
# elif x == 8:
#     print('Try again')
# else:
#     print('Error')
# # 4) Пользователь вводит номер месяца, вывести название месяца.
# a = int(input("Введите номер месяца: \n"))
# def month(a):
#     b = ['январь', "февараль", "март", "апрель", "май", 
#          "июнь", "июль", "август", "сентябрь", "октябрь", 
#          "ноябрь", "декабрь"]
#     print(b[a-1])
# month(a)
# # 5) Дано два числа. Вывести наибольшее из них
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# if a>b:
#     print(f'Число {a} больше числа {b}')
# elif b>a:
#     print(f'Число {b} больше числа {a}')
# else:
#     print('Введите разные числа')
# # 6) Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# if len(range(a, b))>=100:
#     print('Yes')
# else:
#     print('No')
# # 7) Даны два числа. Если первое число больше второго, то вывести 
# # yes, иначе поменять значения этих переменных и вывести их на экран
# import random
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# if a>b:
#     print('Yes')
# elif b>a:
#     c = a*random.randint(1, 9)
#     v = b*random.randint(1, 9)
#     print(c, v)
# else:
#     print('Введите разные числа')
# # 8)  Дано число. Если оно от -10 до 10 не включительно, то 
# # увеличить его на 5, иначе уменьшить на 10.
# a = int(input('Введите первое число: \n'))
# if -10<a<10:
#     a+=5
#     print(a)
# else:
#     a-=10
#     print(a)
# # 9)  Дано число. Если оно более 100 или менее -100, то занулить, иначе увеличить его на 1.
# a = int(input('Введите первое число: \n'))
# if a<-100 or a>100:
#     a=0
#     print(a)
# else:
#     a+=1
#     print(a)
# # 10) Дано число. Если оно от 2 до 5 включительно, то увеличить 
# # его на 10. Если оно от 7 до 40, то уменьшить на 100. Если оно 
# # не более 0 или более 3000, то увеличить в 3 раза (то есть 
# # умножить на 3). Иначе занулить это число.
# a = int(input('Введите первое число: \n'))
# if 2<=a<=5:
#     a+=10
#     print(a)
# elif 7<=a<=40:
#     a-=100
#     print(a)
# elif a<0 or a>3000:
#     a*=3
#     print(a)
# else:
#     a = 0
#     print(a)
# # 11) Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)
# a = int(input("Введите номер месяца: \n"))
# def month_and_yeartime(a):
#     b = ['январь', "февараль", "март", "апрель", "май", 
#          "июнь", "июль", "август", "сентябрь", "октябрь", 
#          "ноябрь", "декабрь"]
#     print(b[a-1].capitalize())
#     if 1<=a<3 or a==12:
#         print('Зима')
#     elif 3<=a<=5:
#         print('Весна')
#     elif 6<=a<=8:
#         print('Лето')
#     else:
#         print('Осень')

# month_and_yeartime(a)
# # 12) Пользователь вводит три числа - длины сторон треугольника. 
# # Найти площадь треугольника. Сделать проверку на существование 
# # треугольника (например, 1, 2, 3 - такого треугольника не существует).
# a = int(input('Введите первое число: \n'))
# b = int(input('Введите второе число: \n'))
# c = int(input('Введите третье число: \n'))
# def triangle(a, b, c):
#     while True:
#         if (a+b>c and b+c>a and a+c>b):
#             break
#         else:
#             print('Треугольника с такими сторонами не существует')
#             break
#     p = a+b+c
#     p_2 = p/2
#     s = (p_2*((p_2-a)*(p_2-b)*(p_2-c)))**0.5
#     return s
# if triangle(a,b,c)!=0.0 and triangle(a,b,c)!=None:
#     print(f'Площадь треугольника: {triangle(a,b,c)}')
# else:
#     print('Введите другие значения')
# # 13) Даны два прямоугольника, стороны которых параллельны 
# # или перпендикулярны осям координат. Известны координаты 
# # левого нижнего угла каждого из них и длины их сторон. Один из 
# # прямоугольников назовем первым, другой — вторым.
# # а) Определить, принадлежат ли все точки первого 
# # прямоугольника второму.
# # б) Определить, принадлежат ли все точки одного из 
# # прямоугольников другому.
# # в) Определить, пересекаются ли эти прямоугольники
# class Rectangle(object):
#     def __init__(self, x, y, w, h):
#         self.x1 = x
#         self.x2 = x + w
#         self.y1 = y
#         self.y2 = y + h

#     def is_involved(self, other):
#         if all([other.x1 <= self.x1, 
#                 other.y1 <= self.y1, 
#                 other.x2 >= self.x2,
#                 other.y2 >= self.y2]):
#             return True
#         return False

#     def is_intersected(self, other):
#         if any([all([other.x1 <= self.x1 <= other.x2, other.y1 <= self.y1 <= other.y2]),
#                 all([other.x1 <= self.x2 <= other.x2, other.y1 <= self.y1 <= other.y2]),
#                 all([other.x1 <= self.x1 <= other.x2, other.y1 <= self.y2 <= other.y2]),
#                 all([other.x1 <= self.x2 <= other.x2, other.y1 <= self.y2 <= other.y2])]):
#             return True
#         return False

# print("Rectangle 1:")
# rect1 = Rectangle(int(input("x = ")), int(input("y = ")), int(input("width = ")), int(input("height = ")))
# print()
# print("Rectangle 2:")
# rect2 = Rectangle(int(input("x = ")), int(input("y = ")), int(input("width = ")), int(input("height = ")))

# print()
# print('а) Принадлежат ли все точки первого прямоугольника второму:')
# print(rect2.is_involved(rect1))
# print('б) Принадлежат ли все точки одного из прямоугольников другому:')
# print(rect2.is_involved(rect1) or rect1.is_involved(rect2))
# print('в)* Пересекаются ли эти прямоугольники:')
# print(rect2.is_intersected(rect1) or rect1.is_intersected(rect2))
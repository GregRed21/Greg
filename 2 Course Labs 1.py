# #1 Вывести на экран текст
# print('1) Silence is golden')
#2 Вывести на экран текущее название дня недели, месяца, и свое имя
# print('2)')
# import datetime
# current_time = datetime.datetime.now()
# print('Year: ', current_time.year)
# print('Month: ', current_time.month)
# print('Day: ', current_time.day)
# print('Hour: ', current_time.hour)
# print('Minute: ', current_time.minute)
# print('Year: ', current_time.year)
# print('Mine name is\nmine name is\nmine name is\nchk chk Slim Shady')
# #3Вывести нули
# q,w,e,r,t = '0','00','000','0000','00000'
# print(f'3)\n{q}\n{w}\n{e}\n{r}\n{t}\n')
# #4Вывести прямугольник из А 5*8
# print('4)')
# qw = "AAAAA"
# qe = 0
# while qe<8:
#     print(qw)
#     qe+=1
# #5Вывести W
# qr = '*     *     *'
# qt = ' *   * *   *' 
# qy = '  * *   * *'
# qu = '   *     *' 
# print('5)')
# print(qr)
# print(qt)
# print(qy)
# print(qu)
# #6Вычислить
# print('6)', '1+2-4=',1+2-4)
# #7 Вычислить
# print('7)', '1/2+1/4=',1/2+1/4)
# #8Вычислить
# print('8)')
# a = 2
# b = 3
# print(((a+4*b)*(a-3*b))+a**2)
# #9Вычислить
# print('9)')
# x = -2
# print(x+x**5)
# print(-x+x**5)
# #10Вычислить
# print('10)')
# wq = 1.7
# eq = 3
# print(((wq+1)**2)+3*(wq+1))
# print(((eq+1)**2)+3*(eq+1))
# #11 Пользователь вводит букву Анг алф. нужно чтобы ряд продолжился 
# print('11)')
# from string import ascii_uppercase
# startletter = ord(input('Введите букву английского алфавита нижнего регистра:')) 
# if startletter < 97:
#     print("Введите только буквы английского алфавита нижнего регистра")
# elif startletter>123:
#     print('Вводите только английские буквы')

# for qq in range(ord('a'), ord('z')):
#     if startletter == qq:
#         print(chr(qq))
#         print(chr(qq+1))
#         print(chr(qq+2))
#         print(chr(qq+3))
#     elif startletter == ord('x'):
#         print('x')
#         print('y')
#         print('z')
#         print('a')
#         break
#     elif startletter == ord('y'):
#         print('y')
#         print('z')
#         print('a')
#         print('b')
#         break
#     elif startletter == ord('z'):
#         print('z')
#         print('a')
#         print('b')
#         print('c')
#         break
# #12 Вывести анг алф по 5 букв в строке
# print('12)')
# for i in range(ord('a'), ord('z')+1):
#   if (i-2) % 5 == 0:
#     print('')
#   print(chr(i), end="")
# print('12.1)')
# from string import ascii_lowercase
# alphabet = [chr(i) for i in range(97,123)]
# q = 5 
# w = [ascii_lowercase[e:e+q] for e in range(0,len(alphabet),q)]
# print(w)
# #13 Вывести квадрат 7 на 7 из случайных значений
# print('13)')
# from random import randint
# from string import ascii_letters

# r, t = ascii_letters, ''

# for q in range(1, 8):
#    for w in range(1, 8):
#        t += r[randint(0, len(r)-1)]
#    print(t)
#    t = ''
# #14 Пользователь вводит положительное число. зашифровать
# print('14)')
# from string import ascii_lowercase
# import random

# num = input('Введите число: ')

# print(''.join(ascii_lowercase[int(x)] + ascii_lowercase[random.randint(0, 26)] for x in str(num)))

# #15 Сгенерировать строку 
# from string import ascii_lowercase
# import random
# print('15)')
# print(''.join([random.choice(ascii_lowercase) for x in range(6)]) + '!!')

# #16 Сгенерировать пароль 
# print('16)')
# import random
# from string import ascii_uppercase, ascii_letters
# from itertools import zip_longest

# str_len = random.randint(8, 8)
# str_to_randomness = ''
# requires_vals = ['_', random.choice(ascii_uppercase), random.choice(ascii_uppercase)]
# nums = []

# if str_len <= 8:
#     rnd_nums = str_len - 3
#     requires_vals.insert(0, random.choice(range(10)))
#     nums = random.choices(population=list(range(10)), k=rnd_nums - 1)
# else:
#     nums = random.choices(population=list(range(10)), k=5)

# for i in range(8, str_len):
#     requires_vals.append(random.choice(ascii_letters))

# random.shuffle(requires_vals)
# for n, r in zip_longest(nums, requires_vals):
#     n = n if n != None else ''
#     r = r if r != None else ''
#     str_to_randomness += str(r) + str(n)

# print(str_to_randomness)
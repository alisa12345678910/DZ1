#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

#n = int(input("Введите число дня недели от 1 до 7: "))
#if n < 1 or n > 7:
#    print('Введено неверное число')
#elif n > 5:
#    print('Да, это выходной!')
#else:
#    print('Да, это будний день')

#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#для всех значений предикат

for x in range(2):
        for y in range(2):
            for z in range(2):
                print((not (x or y or z) == (not (x) and not (y) and not (z))))
                print(x, y, z)

#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
#номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

#x = int(input('Введите число x≠0:'))
#y = int(input('Введите число y≠0:'))


#if x == 0 and y == 0:
#    print('Вы не поняли условия задачи, попробуйте снова;)')
#elif x > 0 and y > 0:
#    print(
#        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
#elif x < 0 and y > 0:
#    print(
#        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
#elif x < 0 and y < 0:
#    print(
#        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
#elif x > 0 and y < 0:
#    print(
#        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')

#4. Напишите программу, которая по заданному номеру четверти показывает диапазон 
#возможных координат точек в этой четверти (x и y).

#n = int(input('Введите номер четверти, в которой бы хотели узнать диапозон возможных координат: '))

#if n == 1:
#    print('В первой четверти - x > 0; y > 0')
#elif n == 2:
#    print('Во второй четверти - x < 0; y > 0')
#elif n == 3:
#    print('В третьей четверти - x < 0; y < 0')
#elif n == 4:
#    print('В четвертой четверти - x > 0; y < 0')
#else:
#    print('Такой четверти нет :(')

#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
#между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

#ax = float(input('Введите координаты точки A по оси x:'))
#ay = float(input('Введите координаты точки A по оси y:'))
#bx = float(input('Введите координаты точки B по оси x:'))
#by = float(input('Введите координаты точки B по оси y:'))

#import math
#distans = math.sqrt((ax-bx)**2+(ay-by)**2)
#print(f'Растояние между точкой A и точкой B = {round(distans, 3)}' )

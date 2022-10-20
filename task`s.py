# 22.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(list), 2):
    sum += list[i]
print(sum)

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2, 3, 5, 9, 3]
mult = 0
a = -1
i = 0
print(list, end=' => ')
while i < (len(list)/2):
    mult = list[i] * list[a]
    i += 1
    a -= 1
    print(mult, end=', ')

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
count = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(count):
    number = float(input())
    some_list.append(number)
min = 0
max = 1
for el in some_list:
    if '.' in str(el):
        dr = str(el).split('.')[1]
        if float('0.' + dr) > max:
            mas = float('0.' + dr)
        elif float('0.' + dr) > min:
            min = float('0.' + dr)
print(max - min)

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import random
a = random.randint(0, 100000)
print(a)
one_zero = ''
while a > 0:

    one_zero = str(a % 2) + one_zero
    a = a//2

print(one_zero)



# ЗадачаФибанача

k = int(input())
some_list = [0] * (k*2+1)
some_list[k+1] = 1
for ind in range(k + 2, k*2+1):
    some_list[ind] = some_list[ind - 1] + some_list[ind - 2]
for ind in range(k, -1, -1):
    some_list[ind] = some_list[ind + 2] - some_list[ind + 1]
print(some_list)
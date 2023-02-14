# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите число N элементов: ")))
a = []
for i in range(n):
    num = int(input("Введите num "))
    a.append(num)
print(a)

m = (int(input("Введите число M элементов: ")))
b = []
for i in range(m):
    num = int(input("Введите num "))
    b.append(num)
print(b)
res = a + b
print('слияние двух списков: ', res)

checked_nums_list = []
for i in res:
    if res.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print(i)













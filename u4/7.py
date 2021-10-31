print('Введите количество чисел в массиве: ')
n = int(input())
print('Вводите через пробел:')
a = [x for x in map(int, input().split())]
print('1. Среднее арифметическое:')
print('| ', round(sum(a)/n))

print('2. Сумма:')
print('| ', sum(a))

print('3. Минимальное и максимальное с индексами:')
for i in range(n):
    if (a[i] == max(a)):
        mx_i = i
    if (a[i] == min(a)):
        mn_i = i
print('| ', max(a), '(', mx_i, ')', min(a), '(', mn_i, ')')

print('4. Произведение всех чисел, находящихся между индексами максимального и минимального:')
pr = 1
if (mn_i < mx_i):
    for i in range(mn_i + 1, mx_i):
        pr = pr*a[i]
elif (mn_i > mx_i):
    for i in range(mx_i + 1, mn_i):
        pr = pr*a[i]
elif (mn_i == mx_i):
    pr = 0

print('| ', pr)

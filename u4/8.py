a = [170, 181, 174, 180, 169]
print('Вводите: ')
new = {}
while True:
    n = input()
    if (n.isdigit() == 1):
        a.append(int(n))
        a.sort()
        new[n] = a.index(int(n))
    elif (n == 'все построены'):
        print(a, '\n')
        print('Новые люди', new)
        break
    else:
        print('Подозрительно')

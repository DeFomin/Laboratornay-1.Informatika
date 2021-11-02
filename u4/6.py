print('Вводите через пробел:')
a = []
count = 0
prov = '0123456789'
while True:
    n = input()
    if (n.isdigit() == 1):
        a.append(n)
        count += 1
    else:
        break
print(count, a)

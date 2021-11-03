print('Вводите: ')
a = []
count = 0

while True:
    n = input()

    if (str(n).lstrip('-').replace('.', '', 1).isdigit() == 1):
        a.append(n)
        count += 1
    else:
        print(count, a)
        break

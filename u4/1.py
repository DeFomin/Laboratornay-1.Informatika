print('Введите ваше имя: ')
first_name = str(input())
print('Введите вашу фамилию: ')
second_name = str(input())

print('У вас есть отчество? (да/нет)')
answer = str(input())
a = ['да', 'нет', 'Да', 'Нет']
if ((answer == 'да') or (answer == 'Да')) and (answer in a):
    print('Введите ваше отчество: ') # Если есть
    third_name = str(input())
    name = second_name + ' ' + first_name[0] + '. ' + third_name[0] + '. '
    print('Ваше имя: ', name)
elif ((answer == 'нет') or (answer == 'Нет')) and (answer in a):
    name = second_name + ' ' + first_name[0] + '. '
    print('Ваше имя: ', name)
else:
    print('Введено неверно')

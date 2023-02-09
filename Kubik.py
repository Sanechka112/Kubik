import random
cube = [1, 2, 3, 4, 5, 6]
com = input('Введите команду: ')
while com != '0':
    rand_numb = random.randint(0, len(cube) - 1)
    if com == 'Бросить кубик':
        print(cube[rand_numb])
    else:
        print('Неизвестная команда!')
    com = input('Введите команду: ')
print('Завершение программы...')
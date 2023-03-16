print('нажмите enter для старта программы или введите "выход" без кавычек для завершения работы программы')
year = input()
while True:
    year = input('Введите порядковый номер месяца или "выход"')
    if year == 'выход':
        break
    else:
        year = int(year)
    
        if year == 12 or year == 1 or year == 2:
            print('Зима')
        elif year == 3 or year == 4 or year == 5:
            print('Весна')
        elif year == 6 or year == 7 or year == 8:
            print('Лето')
        elif year == 9 or year == 10 or year == 11:
            print ('Осень')
        else:
            print('Вы ввели некорректные данные')
print('Программа завершена')
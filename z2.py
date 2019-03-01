def stroka (stroka1, stroka2):
    if type(stroka1) and type(stroka2) is str:
        if stroka1==stroka2:#проверка на одинаковые значения
            print(1)
        if stroka2=="learn":#проверка на learn
            print(3)
        if len(stroka1)>len(stroka2):#берем значения и сравниваем между собой
            print(2)
    else:#проверка на остальное, она не срабатывает, потому что input всегда str
        print(0)        
stroka ((input('Введите строку один')), (input('Введите строку два'))) #пользователь вводит строку 1 и строку 2
stroka ((input('Введите строку один')), (input('Введите строку два'))) #пользователь вводит строку 1 и строку 2
stroka ((input('Введите строку один')), (input('Введите строку два'))) #пользователь вводит строку 1 и строку 2
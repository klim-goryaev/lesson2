def stroka (stroka1, stroka2):
    if isinstance(stroka1,str) and isinstance(stroka2,str):
        if stroka1!=stroka2 and stroka2=="learn":#проверка на learn
            print(3)
            return    
        if len(stroka1)>len(stroka2):#берем значения и сравниваем между собой
            print(2)
        if stroka1==stroka2:#проверка на одинаковые значения
            print(1)
    else:#проверка на остальное, она не срабатывает, потому что input всегда str
        print(0)        
stroka ((input('Введите строку один: ')), (input('Введите строку два: '))) #пользователь вводит строку 1 и строку 2
stroka ((input('Введите строку один: ')), (input('Введите строку два: '))) #пользователь вводит строку 1 и строку 2
stroka ((input('Введите строку один: ')), (input('Введите строку два: '))) #пользователь вводит строку 1 и строку 2
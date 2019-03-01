def stroka (stroka1, stroka2):
    if type(stroka1) is str:
        if type(stroka2) is str:
            if stroka1==stroka2:#проверка на одинаковые значения
                print(1)
            if stroka2=="learn":#проверка на learn
                print(3)
            if len(stroka1)>len(stroka2):#берем значения и сравниваем между собой
                print(2)
            
    #else stroka1 == stroka2:#если строки одинаковые, то возвращаем 1
     #           print("1")
    #elif stroka1 != stroka2: #если строки разные и первая длиннее, вернуть 2
     #   print("2")
    #elif stroka1 != stroka2: #если строки разные и вторая строка 'learn', возвращает 3
      #  print("3") 
stroka ((input('Введите строку один')), (input('Введите строку два'))) #пользователь вводит строку 1 и строку 2
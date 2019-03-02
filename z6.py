def get_summ(num_one, num_two):
    try :
        num_one_int = int(num_one)
        num_two_int = int(num_two)
        print(num_one_int+num_two_int)
    except ValueError :
        print("Не работает!")
get_summ ((input('Введите строку один: ')), (input('Введите строку два: '))) #пользователь вводит строку 1 и строку 2
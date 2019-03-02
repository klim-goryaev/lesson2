try:
    while True:
        user_say = input('Скажи что-нибудь: ')
        if user_say == 'Пока':
            print('Ну пока')
        else:
            print('Сам ты {}'.format(user_say))
except KeyboardInterrupt:
    print('Except')
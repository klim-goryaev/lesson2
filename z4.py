#словарь вопросов ответов
qa = [
    {'question':"Как дела", 'answer': "Хорошо!"}, 
    {'question':"Куда пойдешь?", 'answer':"На курсы"},
    {'question':"Что делаешь?", 'answer':"Программирую"}, 
    ]
for quest in qa:
    while True:
        user_say = input()
        if user_say == (quest["question"]):
            print (quest["answer"])
        else:
            print ('Нет ответа на {}'.format(user_say))
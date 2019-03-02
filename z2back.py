#словарь вопросов ответов
qa = [
    {'question':"Как дела", 'answer': "Хорошо!"}, 
    {'question':"Куда пойдешь?", 'answer':"На курсы"},
    {'question':"Что делаешь?", 'answer':"Программирую"}, 
    ]
for quest in qa:
    a=(quest["question"])
    b=(quest["answer"])

while True:
    user_say = input()
    if user_say == (a):
        print (b)
        break
    else:
        print ('Нет ответа на {}'.format(user_say))

#проблема 1 - почему то ищет всегда по последнему вопросу
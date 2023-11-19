def english():
    count = 0
    points = 0

    questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
    answers = ["is", "am", "in"]

    user_input = input("Привет! Предлагаю проверить свои знания английского! Набери 'ready', чтобы начать!\n")
    if user_input.lower() == "ready":

        for question in questions:
            print(question)
            attempt = 3
            while True:

                user_input = input('Введите правильный ответ:\n')
                if user_input == answers[questions.index(question)]:
                    print('Верно')
                    count += 1
                    break
                else:
                    attempt -= 1

                if attempt == 0:
                    break
                print(f'Осталось попыток: {attempt}, попробуйте еще раз!')

            points += 10 * attempt

        print(f'Вот и все! Вы ответили на {count} вопросов из {len(questions)} верно, вы набрали {points} баллов.')
    else:
        print('Кажется, вы не хотите играть. Очень жаль')


english()
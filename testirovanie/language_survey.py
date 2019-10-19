from survey import AnonymousServey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = 'What language did you first learn to speak?'
my_survey = AnonymousServey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("'q' to quit")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Вывод результатов опроса.
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()

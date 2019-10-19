import unittest
from survey import AnonymousServey


class TestAnonymSurvey(unittest.TestCase):
    """" Тесты для класса AnonymousSurvey """
    def setUp(self):
        """" Создание опроса и набора ответов для всех тестовых методов """
        frage = 'What language did you first learn to speak?'
        self.my_survey = AnonymousServey(frage)
        self.responses = ['eng', 'de', 'sp']

    def test_store_single_response(self):
        """" Проверяет, что один ответ сохранен правильно """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """" Проверяет, что три ответа были сохранены правильно """
        for a in self.responses:
            self.my_survey.store_response(a)
        for ant in self.responses:
            self.assertIn(ant, self.my_survey.responses)
            

# unittest.main()
if __name__ == 'main':
    unittest.main()

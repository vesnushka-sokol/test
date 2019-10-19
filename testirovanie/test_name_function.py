import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Тесты для 'name_function.py' """
    def test_first_last_name(self):
        """" Имена вида 'Janis Jop' работают правильно? """
        form_name = get_formatted_name('janis', 'jop')
        self.assertEqual(form_name, 'Janis Jop')

    def test_first_last_middle_name(self):
        """ Работают ли такие имена, как 'Wolfgang Amadeus Mozart'? """
        form_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(form_name, 'Wolfgang Amadeus Mozart')


# unittest.main()
if __name__ == 'main':
    unittest.main()

import unittest
from city_functions import get_city_functions


class LandTest(unittest.TestCase):
    def test_city_country(self):
        full_n = get_city_functions('Chile', 'Santiago')
        self.assertEqual(full_n, 'Santiago, Chile')

    def test_city_country_ohne_population(self):
        full_n = get_city_functions('Chile', 'Santiago')
        self.assertEqual(full_n, 'Santiago, Chile')

    def test_city_country_population(self):
        full_n = get_city_functions('Chile', 'Santiago', 5000000)
        self.assertEqual(full_n, 'Santiago, Chile - population 5000000')


unittest.main()

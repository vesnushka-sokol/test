import unittest
from angestellter import Angestellter


class TestAngestellter(unittest.TestCase):
    def setUp(self):
        vorname = 'Alex'
        name = 'Sokol'
        gehalt = 4500
        self.angest = Angestellter(vorname, name, gehalt)

    def test_give_default_raise(self):
        self.assertEqual(self.angest.gehalt, 4500)

    def test_give_custom_raise(self):
        self.assertEqual(self.angest.give_raise(), 9500)


if __name__ == 'main':
    unittest.main()

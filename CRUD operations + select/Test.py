import unittest
from type import *
from owner import *
from shelf import *
from document import *


class Shelf(unittest.TestCase):
    SHELVES_1 = '1'
    SHELVES_2 = '2'
    SHELVES_3 = '4'
    SHELVES_4 = '5'
    SHELVES_5 = 'jjj'
    SHELVES_6 = 6

    EXPECTED_1 = ['1', '2']
    EXPECTED_2 = ['1']
    EXPECTED_3 = None

    def test_select1(self):
        self.assertEqual(select_shelf(self.SHELVES_1, self.SHELVES_2), self.EXPECTED_1)

    def test_select2(self):
        self.assertEqual(select_shelf(self.SHELVES_1, self.SHELVES_3), self.EXPECTED_2)

    def test_select3(self):
        self.assertEqual(select_shelf(self.SHELVES_3, self.SHELVES_4), self.EXPECTED_3)

    def test_select4(self):
        self.assertEqual(select_shelf(self.SHELVES_5), self.EXPECTED_3)

    def test_select5(self):
        self.assertEqual(select_shelf(self.SHELVES_6), self.EXPECTED_3)


    def test_create(self):
        self.assertEqual()

class Document(unittest.TestCase):
    pass







if __name__ == '__main__':
    unittest.main()

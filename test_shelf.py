import unittest
from shelf import *


class Shelf(unittest.TestCase):
    def test_select1(self):
        INPUT_1 = '2207 876234'
        EXPECTED_1 = '1'

        INPUT_2 = '11-2'
        EXPECTED_2 = '1'

        INPUT_3 = '10006'
        EXPECTED_3 = '2'

        self.assertEqual(get_shelf_by_doc_number(INPUT_1), EXPECTED_1)
        self.assertEqual(get_shelf_by_doc_number(INPUT_2), EXPECTED_2)
        self.assertEqual(get_shelf_by_doc_number(INPUT_3), EXPECTED_3)
        self.assertEqual(get_shelf_by_doc_number('INPUT_3'), None)

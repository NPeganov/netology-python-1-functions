import unittest
import builtins
from unittest.mock import patch
from functions import *
from main import *
import containers


class MyTestCase(unittest.TestCase):
    EXPECTED_RESULT_TEST1 = 'This command doesn\'t exist \nPrint \'lof\' to see the list of commands'
    INPUT_TEST1 = 'xdfh'

    EXPECTED_RESULT_TEST2 = """The list of commands: 
q - to finish the program
p - to show who owns the document
s - to show on which shelf the document is held
l - to show full information of the document
ads - to add a new shelf
ds - to delete a shelf
ad - to add a new doc
d - to delete a document
m - to move the document from one shelf to another
lof - to show full list of commands"""
    INPUT_TEST2 = 'lof'

    EXPECTED_RESULT_TEST3 = 'The program stopped'
    INPUT_TEST3 = 'Q'

    EXPECTED_RESULT_TEST4 = 'The shelf was successfully added. Current list of shelves: 1, 2, 3, 4 '
    INPUT_TEST4 = '4'
    INPUT_FOR_UPPER_FUNC_TEST4 = factory(command='ads')

    EXPECTED_RESULT_TEST5 = 'The program stopped'
    INPUT_TEST5 = 'Q'

    EXPECTED_RESULT_TEST6 = 'The program stopped'
    INPUT_TEST6 = 'Q'

    EXPECTED_RESULT_TEST7 = 'The program stopped'
    INPUT_TEST7 = 'Q'

    EXPECTED_RESULT_TEST8 = 'The program stopped'
    INPUT_TEST8 = 'Q'

    EXPECTED_RESULT_TEST9 = 'The program stopped'
    INPUT_TEST9 = 'Q'

    EXPECTED_RESULT_TEST10 = 'The program stopped'
    INPUT_TEST10 = 'Q'

    def test1(self):

        self.assertEqual(factory(self.INPUT_TEST1), self.EXPECTED_RESULT_TEST1)

    def test2(self):
        self.assertEqual(factory(self.INPUT_TEST2), self.EXPECTED_RESULT_TEST2)

    def test3(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)    # !!!

    def test4(self):
        assert input() == '4'
        @patch 'builtins.input', side_effect='4'
        with patch('builtins.input', side_effect='4'):
            stacks = containers.get_input_stacks()
        self.assertEqual(stacks, self.EXPECTED_RESULT_TEST3)
        self.assertEqual(create_shelf(new_num=self.INPUT_TEST4), self.EXPECTED_RESULT_TEST3)
        with patch("builtins.input", return_value="4"):
            self.assertEqual(create_shelf.get_input(), self.EXPECTED_RESULT_TEST3)

    def test5(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)

    def test6(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)

    def test7(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)

    def test8(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)

    def test9(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)

    def test10(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)


if __name__ == '__main__':
    unittest.main()

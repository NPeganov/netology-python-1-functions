import unittest
from unittest.mock import MagicMock
from functions import *
from main import factory, user_interaction


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

    def test1(self):
        self.assertEqual(factory(self.INPUT_TEST1), self.EXPECTED_RESULT_TEST1)  # add assertion here

    def test2(self):
        self.assertEqual(factory(self.INPUT_TEST2), self.EXPECTED_RESULT_TEST2)  # add assertion here

    def test3(self):
        self.assertEqual(user_interaction(), self.EXPECTED_RESULT_TEST3)  # add assertion here


if __name__ == '__main__':
    unittest.main()

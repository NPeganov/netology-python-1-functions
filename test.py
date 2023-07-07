import unittest
import builtins
from unittest.mock import patch
from functions import *
from main import *
import containers


class MyTestCase(unittest.TestCase):
    EXPECTED_RESULT_TEST1 = 'The program stopped'
    INPUT_TEST1 = 'Q'

    def test1(self):
        self.assertEqual(factory(self.INPUT_TEST1), self.EXPECTED_RESULT_TEST1)


if __name__ == '__main__':
    unittest.main()

import unittest
from task import *

EXPECTED_RESULT_TEST1 = """The list of commands: 
q - to finish the program
p - to show who owns the document
s - to show on which shelf the document is held
l - to show full information of the document
ads - to add a new shelf
ds - to delete a shelf
ad - to add a new doc
d - to delete a document
m - to move the document from one shelf to another
lof - to show full list of commands
"""

_ = '10006'
_ = 'Аристарх Павлов'

_ = '568'
_ = 'Document owner is not found'

_ = """№: 2207 876234, type: passport, owner: Василий Гупкин, storage shelf: 1 
№: 11-2, type: invoice, owner: Геннадий Покемонов, storage shelf: 1 
№: 10006, type: insurance, owner: Аристарх Павлов, storage shelf: 2 
"""

_ =

class MyTestCase(unittest.TestCase):
    EXPECTED_RESULT_TEST1 = """The list of commands: 
    q - to finish the program
    p - to show who owns the document
    s - to show on which shelf the document is held
    l - to show full information of the document
    ads - to add a new shelf
    ds - to delete a shelf
    ad - to add a new doc
    d - to delete a document
    m - to move the document from one shelf to another
    lof - to show full list of commands
    """
    def test_something(self):
        self.assertEqual(show_list_of_commands(), self.EXPECTED_RESULT_TEST1)  # add assertion here


if __name__ == '__main__':
    unittest.main()

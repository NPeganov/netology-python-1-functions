import unittest
from documents import select_documents, DocKeys


class Select(unittest.TestCase):
    def test_select1(self):
        INPUT = dict()
        EXPECTED = [
            ('1', {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}),
            ('1', {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}),
            ('2', {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'})
        ]
        self.assertEqual(select_documents(INPUT), EXPECTED)

    def test_select2(self):
        INPUT = {DocKeys.SHELF: '1'}
        EXPECTED = [
            ('1', {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}),
            ('1', {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'})
        ]
        self.assertEqual(select_documents(INPUT), EXPECTED)

    def test_select3(self):
        INPUT = {DocKeys.SHELF: '2'}
        EXPECTED = [
            ('2', {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'})
        ]
        self.assertEqual(select_documents(INPUT), EXPECTED)

    def test_select4(self):
        INPUT = {DocKeys.TYPE: 'insurance',
                 DocKeys.NUMBER: '10006'}
        EXPECTED = [
            ('2', {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'})
        ]
        self.assertEqual(select_documents(INPUT), EXPECTED)

    def test_select5(self):
        INPUT = {DocKeys.TYPE: 'insurance',
                 DocKeys.NUMBER: '10006',
                 DocKeys.OWNER: 'Vasya'}
        self.assertEqual(select_documents(INPUT), [])

import unittest
from documents import read_documents, update_document, delete_document, DocKeys
from globals import *


class DocCrud(unittest.TestCase):
    def test_read1(self):
        INPUT = dict()
        EXPECTED = [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин', DocKeys.SHELF: '1'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов', DocKeys.SHELF: '1'},
            {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов', DocKeys.SHELF: '2'}
        ]
        self.assertEqual(EXPECTED, read_documents(INPUT))

    def test_read2(self):
        INPUT = {DocKeys.SHELF: '1'}
        EXPECTED = [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин', DocKeys.SHELF: '1'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов', DocKeys.SHELF: '1'}
        ]
        self.assertEqual(EXPECTED, read_documents(INPUT))

    def test_update1(self):
        NEW_VALUES = {DocKeys.SHELF: '3', DocKeys.OWNER: 'Vasya', DocKeys.NUMBER: '22'}
        EXPECTED = {'type': 'passport', 'number': '22', 'name': 'Vasya', DocKeys.SHELF: '3'}
        self.assertEqual(EXPECTED, update_document('2207 876234', NEW_VALUES))


    def test_update2(self):
        NEW_VALUES = {DocKeys.SHELF: '6', DocKeys.OWNER: 'Vasya', DocKeys.NUMBER: '22'}
        EXPECTED = None
        self.assertEqual(EXPECTED, update_document('2207 876234', NEW_VALUES))


    def test_delete1(self):
        WHERE = {DocKeys.SHELF: '1'}
        EXPECTED = ['2207 876234', '11-2']
        result = delete_document(WHERE)
        self.assertTrue(EXPECTED[0] in result)
        self.assertTrue(EXPECTED[1] in result)
        self.assertEqual([{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}], documents)
        self.assertEqual({'1': [], '2': ['10006'], '3': []}, directories)

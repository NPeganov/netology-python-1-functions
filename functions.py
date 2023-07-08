from constants import K_NUMBER, K_NAME
from shelf_doc_input_handler import *
from global_variables import *


def read_doc_by_number(doc_num):
    a = None
    for document in documents:
        if document[K_NUMBER] == doc_num:
            a = document
    if a is None:
        return None
    else:
        return a


def get_doc_owner():
    doc_num = input_handler_doc('Enter number of the document: \n')
    if read_doc_by_number(doc_num) is not None:
        document = read_doc_by_number(doc_num)
        if document is str:
            print('Document\'s owner was not found ')
        else:
            owner = document[K_NAME]
            return owner


def get_shelf_num():
    doc_num = input_handler_doc('Enter number of the document: \n')
    shelf = None
    for key_shelf_num, values in directories.items():
        if doc_num in values:
            shelf = key_shelf_num
            return shelf
    if shelf is None:
        print('Document is not found ')


def read_shelf_list():
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key}, '

    print(f'Current list of shelves: {shelves} ')


def update_doc():
    doc_num = input_handler_doc('Enter number of a document to move it: \n')
    shelf = input_handler_shelf('Enter number of the shelf where to move: \n')
    a = None
    if doc_num in directories[shelf]:
        print(f'The document is already on shelf {shelf}. ')
    else:
        for d in directories.values():
            if doc_num in d:
                d.remove(doc_num)
                a = d
        if a is None:
            print('The document wasn\'t found on the shelf. ')
        else:
            directories[shelf].append(doc_num)
            print('The document was successfully moved! ')


def delete_shelf():
    shelf_num = input_handler_shelf('Enter number of the shelf to delete: \n')
    if directories[shelf_num] != list():
        print('There are documents on the shelf, remove them before removing the shelf \
        (print "d" to remove a document). ')
    else:
        del directories[shelf_num]
        print('The shelf was deleted. ')


def delete_doc():
    doc_num = input_handler_doc('Enter number of a document to delete it: \n')
    for document in documents:
        if document[K_NUMBER] == doc_num:
            documents.remove(document)
        for d in directories.values():
            if doc_num in d:
                d.remove(doc_num)

        print('The document is successfully deleted! ')

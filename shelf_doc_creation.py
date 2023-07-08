from constants import K_NUMBER, K_TYPE, K_NAME, QUIT_COM, LIST_OF_COMS_COM
from shelf_doc_input_handler import input_handler_shelf
from global_variables import *
from list_doc_info import list_commands
from functions import read_doc_by_number
from integer_input import input_integer


def create_doc():
    num = input_handler_num()
    document = read_doc_by_number(num)
    if document is not None:
        while existence(num, document.values(), 'document'):
            num = input_handler_num()
    doc_type = input('Enter the type of the document: \n')
    owner_name = input_handler_owner()
    shelf = input_handler_shelf('Enter the number of a shelf to place the document: \n')
    if shelf is not None:
        document = dict()
        document[K_TYPE] = doc_type
        document[K_NUMBER] = num
        document[K_NAME] = owner_name
        documents.append(document)
        directories[shelf].append(num)
        print('The document was successfully added! ')


def input_handler_num():
    num = input('Enter the number of a new document: \n')
    while not input_integer(num):
        if num in QUIT_COM:
            quit('The program stopped.')
        elif num in LIST_OF_COMS_COM:
            list_commands()
            break
        print('The number of document must be digital. ')
        num = input('Enter the number of a new document: \n')
    return num


def input_handler_owner():
    owner_name = input('Enter the name of the document\'s owner: \n')
    owner_name = owner_name.split(' ')
    for word in range(len(owner_name)):
        owner_name[word] = owner_name[word].capitalize()
    owner_name = ' '.join(owner_name)
    return owner_name


def create_shelf():
    new_num = input_handler_shelf(True, 'Enter number of the new shelf: \n')
    if not existence(new_num, directories, 'shelf'):
        directories[new_num] = []
        print(f'The shelf was successfully added. ')


def existence(var, storage, name):
    if var in storage:
        print(f'The {name} already exists ')
        existence_indicator = True
    else:
        existence_indicator = False
    return existence_indicator

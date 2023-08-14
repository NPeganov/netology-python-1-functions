from constants import QUIT_COM, LIST_OF_COMS_COM
from global_variables import *
from list_doc_info import list_commands
from number_input import is_number


def input_handler_shelf(should_exist, text=''):
    shelf = input(text)
    if should_exist:
        shelf = input_initialization(shelf, 'shelf', directories, text, '"ads"')
    else:
        shelf = input_initialization(shelf, 'shelf', directories, text, '"ads"')
    return shelf


def input_handler_doc(text=''):
    doc = input(text)
    document = []
    numbers = []
    for value in directories.values():
        document.append(value)
    for num in document:
        numbers.extend(num)
        doc = input_initialization(doc, 'document', numbers, text, '"ad"')
    return doc


def input_initialization(obj, name, storage, text, command):
    while obj not in storage:
        if obj in QUIT_COM:
            quit('The program stopped.')
        elif obj in LIST_OF_COMS_COM:
            list_commands()
            break
        else:
            print(f'The {name} doesn\'t exist. To add a {name} type {command} ')
            obj = input(text)
    return obj

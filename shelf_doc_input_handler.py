from constants import QUIT_COM, LIST_OF_COMS_COM
from variables import *
from main import main_loop


def input_handler_shelf(text=''):
    shelf = input(text)
    while shelf not in directories:
        if shelf in QUIT_COM:
            main_loop(command='q')
        elif shelf in LIST_OF_COMS_COM:
            main_loop(command='lof')
            break
        else:
            print('The shelf doesn\'t exist. To add a shelf type \'ads\' ')
            shelf = input(text)
    return shelf


def input_handler_doc(text=''):
    doc = input(text)
    document = []
    numbers = []
    for value in directories.values():
        document.append(value)
    for num in document:
        numbers.extend(num)
    while doc not in numbers:
        if doc in QUIT_COM:
            main_loop(command='q')
        elif doc in LIST_OF_COMS_COM:
            main_loop(command='lof')
        else:
            print('The document doesn\'t exist. To add a document type \'ads\' ')
            doc = input(text)

    return doc

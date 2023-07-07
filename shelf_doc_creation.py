from constants import K_NUMBER, K_TYPE, K_NAME
from variables import directories, documents
from shelf_doc_input_handler import input_handler_shelf


def create_doc():
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
    while not num.isdigit():
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
    new_num = input_handler_shelf('Enter number of the new shelf: \n')
    if new_num in directories:
        print('The shelf already exists ')
    else:
        directories[new_num] = []
        print(f'The shelf was successfully added. ')

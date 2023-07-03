from constants import *
from functions import *


def factory(command):
    if command in PERSON_COM:
        doc_num = input('Enter number of the document: \n')
        return get_doc_owner(doc_num)
    elif command in SHELF_COM:
        doc_num = input('Enter number of the document: \n')
        return read_shelf(doc_num)
    elif command in LIST_COM:
        return list_doc_info()
    elif command in ADD_SHELF_COM:
        new_shelf_num = input('Enter number of the new shelf: \n')
        return create_shelf(new_shelf_num)
    elif command in DELETE_SHELF_COM:
        to_be_deleted_shelf_num = input('Enter number of the shelf to delete: \n')
        return delete_shelf(to_be_deleted_shelf_num) + list_doc_info()
    elif command in ADD_DOCUMENT_COM:
        _num = input('Enter the number of a new document: \n')
        _type = input('Enter the type of the document: \n')
        _owner = input('Enter the name of the document\'s owner: \n')
        _shelf = input('Enter the number of a shelf to place the document: \n')
        return create_doc(_num, _type, _owner, _shelf) + list_doc_info()
    elif command in DELETE_COM:
        doc_to_be_deleted = input('Enter number of a document to delete it: \n')
        return delete_doc(doc_to_be_deleted) + list_doc_info()
    elif command in MOVE_COM:
        doc_to_move = input('Enter number of a document to move it: \n')
        _shelf = input('Enter number of the shelf where to move: \n')
        return update_doc(doc_to_move, _shelf) + list_doc_info()
    elif command in LIST_OF_COMS_COM:
        return list_commands()
    else:
        return 'This command doesn\'t exist. \nPrint \'lof\' to see the list of commands.'


def user_interaction():
    command = None
    while command not in QUIT_COM:
        command = input('Enter the command, please: \n').lower()
        if command in QUIT_COM:
            print('The program stopped.')
        else:
            print(factory(command))


if __name__ == '__main__':
    print(list_commands())
    user_interaction()

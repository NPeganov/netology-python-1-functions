from constants import *
from functions import *


def factory():
    command = input('Enter the command, please: \n').lower()
    if command in PERSON:
        doc_num = input('Enter number of the document: \n')
        return read_doc_owner(doc_num)
    elif command in SHELF:
        doc_num = input('Enter number of the document: \n')
        return read_shelf(doc_num)
    elif command in FULL_DOC_INFO:
        return read_doc_info()
    elif command in ADD_SHELF:
        new_shelf_num = input('Enter number of the new shelf: \n')
        return create_shelf(new_shelf_num)
    elif command in DELETE_SHELF:
        to_be_deleted_shelf_num = input('Enter number of the shelf to delete: \n')
        return delete_shelf(to_be_deleted_shelf_num) + read_doc_info()
    elif command in ADD_DOCUMENT:
        _num = input('Enter the number of a new document: \n')
        _type = input('Enter the type of the document \n')
        _owner = input('Enter the name of the document\'s owner \n')
        _shelf = input('Enter the number of a shelf to place the document \n')
        return create_doc(_num, _type, _owner, _shelf) + read_doc_info()
    elif command in DELETE:
        doc_to_be_deleted = input('Enter number of a document to delete it: \n')
        return delete_doc(doc_to_be_deleted) + read_doc_info()
    elif command in MOVE:
        doc_to_move = input('Enter number of a document to move it: \n')
        _shelf = input('Enter number of the shelf where to move: \n')
        return update_doc(doc_to_move, _shelf) + read_doc_info()
    elif command in LIST_OF_COMS:
        return read_commands_list()
    else:
        return 'This command doesn\'t exist \nPrint \'lof\' to see the list of commands'


def user_interaction():
    command = None
    while command not in QUIT:
        if command in QUIT:  # Tf is going on here
            print('The program stopped')
        else:
            print(factory())


if __name__ == '__main__':
    print(read_commands_list())
    user_interaction()

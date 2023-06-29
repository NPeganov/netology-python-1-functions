from constants import *


def user_interaction():
    command = None
    while command not in QUIT:
        command = input('Enter the command, please: \n').lower()
        if command in PERSON:
            doc_num = input('Enter number of the document: \n')
            print(show_doc_owner(doc_num))
        elif command in SHELF:
            doc_num = input('Enter number of the document: \n')
            print(show_shelf_of_doc(doc_num))
        elif command in FULL_DOC_INFO:
            print(show_full_doc_info())
        elif command in ADD_SHELF:
            new_shelf_num = input('Enter number of the new shelf: \n')
            print(add_new_shelf(new_shelf_num))
        elif command in DELETE_SHELF:
            to_be_deleted_shelf_num = input('Enter number of the shelf to delete: \n')
            print(delete_a_shelf(to_be_deleted_shelf_num), clod)
            print(show_full_doc_info())
        elif command in ADD_DOC:
            _num = input('Enter the number of a new document: \n')
            _type = input('Enter the type of the document \n')
            _owner = input('Enter the name of the document\'s owner \n')
            _shelf = input('Enter the number of a shelf to place the document \n')
            print(add_new_doc(_num, _type, _owner, _shelf), clod)
            print(show_full_doc_info())
        elif command in DELETE:
            doc_to_be_deleted = input('Enter number of a document to delete it: \n')
            print(delete_doc(doc_to_be_deleted), clod)
            print(show_full_doc_info())
        elif command in MOVE:
            doc_to_move = input('Enter number of a document to move it: \n')
            _shelf = input('Enter number of the shelf where to move: \n')
            print(move_doc(doc_to_move, _shelf), clod)
            print(show_full_doc_info())
        elif command in LIST_OF_COMS:
            print(show_list_of_commands())
        elif command in QUIT:
            print('The program stopped')
        else:
            print('This command doesn\'t exist \nPrint \'lof\' to see the list of commands')


if __name__ == '__main__':
    print(show_list_of_commands())
    user_interaction()
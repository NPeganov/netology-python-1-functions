from constants import *
from functions import *
from shelf_doc_creation import create_doc, create_shelf
from list_doc_info import list_commands, list_doc_info


def main_loop():
    command = None
    while command not in QUIT_COM:
        command = input('Enter the command, please: \n').lower()
        if command in PERSON_COM:
            result = get_doc_owner()
            if result is not None:
                print(result)
            else:
                get_doc_owner()
        elif command in SHELF_COM:
            result = get_shelf_num()
            if result is not None:
                print(result)
            else:
                get_shelf_num()
        elif command in LIST_COM:
            list_doc_info()
        elif command in ADD_SHELF_COM:
            create_shelf()
            read_shelf_list()
        elif command in DELETE_SHELF_COM:
            delete_shelf()
            list_doc_info()
        elif command in ADD_DOCUMENT_COM:
            create_doc()
            list_doc_info()
        elif command in DELETE_COM:
            delete_doc()
            list_doc_info()
        elif command in MOVE_COM:
            update_doc()
            list_doc_info()
        elif command in LIST_OF_COMS_COM:
            list_commands()
        elif command in QUIT_COM:
            print('The program stopped.')
        else:
            print('This command doesn\'t exist. \nPrint \'lof\' to see the list of commands. \n')


if __name__ == '__main__':
    list_commands()
    main_loop()

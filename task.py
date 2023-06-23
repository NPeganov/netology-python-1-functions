documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def show_list_of_commands():
    commands = {'q': 'to finish the program',
                'p': 'to show who owns the document',
                's': 'to show on which shelf the document is held',
                'l': 'to show full information of the document',
                'ads': 'to add a new shelf',
                'ds': 'to delete a shelf',
                'ad': 'to add a new doc',
                'd': 'to delete a document',
                'm': 'to move the document from one shelf to another',
                'lof': 'to show full list of commands'}

    the_list_of_coms = str()
    for key, value in commands.items():
        the_list_of_coms += f'\n{key} - {value}'
    return f'The list of commands: {the_list_of_coms}'


def show_doc_owner(documents, doc_num):
    owner = None
    for document in documents:
        if document['number'] == doc_num:
            owner = document['name']
            return owner
    if owner is None:
        return 'Document owner is not found'


def show_shelf_of_doc(directories, doc_num):
    shelf = None
    for key, values in directories.items():
        if doc_num in values:
            shelf = key
            return shelf
    if shelf is None:
        return 'Document is not found'


def show_full_doc_info(documents, directories):
    result = ''
    for document in documents:
        for key, values in directories.items():
            if document['number'] in values:
                result += f'№: {document["number"]}, type: {document["type"]}, owner: {document["name"]}' \
                          f', storage shelf: {key} \n'
    return result


def current_list_of_shelves(directories):
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key}, '
    return f'Current list of shelves: {shelves}'


def add_new_shelf(directories, new_num):
    for _ in directories:
        if new_num == _:
            return 'The shelf already exists'
    directories[new_num] = []
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key} '
    return f'The shelf was successfully added. {current_list_of_shelves(directories)}', directories


def delete_a_shelf(directors, shelf_num):
    if shelf_num not in directories:
        return 'The shelf doesn\'t exist'
    if directors[shelf_num] != list():
        return 'There are documents on the shelf, remove them before removing the shelf (print d to remove a document).'
    del directories[shelf_num]
    return 'The shelf was deleted.', directories


def add_new_doc(directories, documents):
    num = input('Enter the number of a new document: \n')
    type = input('Enter the type of the document \n')
    owner = input('Enter the name of the document\'s owner \n').capitalize()
    shelf = input('Enter the number of a shelf to place the document \n')
    if shelf not in directories:
        return 'The shelf doesn\'t exist. To add a shelf print \'ads\''
    document = dict()
    document['type'] = type
    document['number'] = num
    document['name'] = owner
    documents.append(document)
    directories[shelf].append(num)
    return 'The document was successfully added!', directories, documents


def delete_doc(directories, documents, doc):
    a = None
    for document in reversed(range(len(documents))):
        if documents[document]['number'] == doc:
            del documents[document]
            a = document
    if a is None:
        return 'The document doesn\'t exist'
    for d in directories.values():
        if doc in d:
            d.remove(doc)

    result = ('The document is successfully deleted!', directories, documents)

    return result


def move_doc(doc, shelf, directories):
    a = None
    for d in directories.values():
        if doc in d:
            d.remove(doc)
            a = d
    if a is None:
        return 'The document wasn\'t found on the shelf'
    directories[shelf].append(doc)
    return 'The document was successfully moved!', directories


def user_interaction(documents, directories):
    command = None
    doc_owner = 'p'
    finish = 'q'
    on_which_shelf = 's'
    full_doc_info = 'l'
    new_shelf = 'ads'
    delete_shelf = 'ds'
    doc_to_be_added = 'ad'
    d = 'd'
    m = 'm'
    list_of_coms = 'lof'
    clod = '\nCurrent list of document: \n'

    while command != finish:
        command = input('Enter the command, please: \n').lower()
        if command == doc_owner:
            doc_num = input('Enter number of the document: \n')
            print(show_doc_owner(documents, doc_num))
        elif command == on_which_shelf:
            doc_num = input('Enter number of the document: \n')
            print(show_shelf_of_doc(directories, doc_num))
        elif command == full_doc_info:
            print(show_full_doc_info(documents, directories))
        elif command == new_shelf:
            new_shelf_num = input('Enter number of the new shelf: \n')
            print(add_new_shelf(directories, new_shelf_num)[0])
            directories = add_new_shelf(directories, new_shelf_num)[1]
        elif command == delete_shelf:
            to_be_deleted_shelf_num = input('Enter number of the shelf to delete: \n')
            print(delete_a_shelf(directories, to_be_deleted_shelf_num)[0], clod)
            directories = delete_a_shelf(directories, to_be_deleted_shelf_num)[1]
            print(show_full_doc_info(documents, directories))
        elif command == doc_to_be_added:
            print(add_new_doc(directories, documents)[0], clod)
            directories, documents = add_new_doc(directories, documents)[1], add_new_doc(directories, documents)[2]
            print(show_full_doc_info(documents, directories))
        elif command == d:
            doc_to_be_deleted = input('Enter number of a document to delete it: \n')
            print(delete_doc(directories, documents, doc_to_be_deleted)[0], clod)
            directories, documents = delete_doc(directories, documents, doc_to_be_deleted)[1], delete_doc(directories,
                                                                                        documents, doc_to_be_deleted)[2]
            print(show_full_doc_info(documents, directories))
        elif command == m:
            doc_to_move = input('Enter number of a document to move it: \n')
            shelf = input('Enter number of the shelf where to move: \n')
            print(move_doc(doc_to_move, shelf, directories)[0])
            directories = move_doc(doc_to_move, shelf, directories)[1]
            print(show_full_doc_info(documents, directories))
        elif command == list_of_coms:
            print(show_list_of_commands())
        elif command == finish:
            print('The program stopped')
        else:
            print('This command doesn\'t exist \nPrint \'lof\' to see the list of commands')


if __name__ == '__main__':
    show_list_of_commands()
    user_interaction(documents, directories)

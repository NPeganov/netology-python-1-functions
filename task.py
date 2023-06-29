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
                'ad': 'to add a new doc',  # !
                'd': 'to delete a document',  # !
                'm': 'to move the document from one shelf to another',
                'lof': 'to show full list of commands'}

    the_list_of_coms = str()
    for key, value in commands.items():
        the_list_of_coms += f'\n{key} - {value}'
    return f'The list of commands: {the_list_of_coms}'


def show_doc_owner(doc_num):
    owner = None
    for document in documents:
        if document['number'] == doc_num:
            owner = document['name']
            return owner
    if owner is None:
        return 'Document owner is not found'


def show_shelf_of_doc(doc_num):
    shelf = None
    for key, values in directories.items():
        if doc_num in values:
            shelf = key
            return shelf
    if shelf is None:
        return 'Document is not found'


def show_full_doc_info():
    result = ''
    for document in documents:
        for key, values in directories.items():
            if document['number'] in values:
                result += f'№: {document["number"]}, type: {document["type"]}, owner: {document["name"]}' \
                          f', storage shelf: {key} \n'
    return result


def current_list_of_shelves():
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key}, '

    a = f'Current list of shelves: {shelves}' #!
    return f'Current list of shelves: {shelves}'


def add_new_shelf(new_num):
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
    return f'The shelf was successfully added. {current_list_of_shelves()}'


def delete_a_shelf(shelf_num):
    if shelf_num not in directories:
        return 'The shelf doesn\'t exist'
    if directories[shelf_num] != list():
        return 'There are documents on the shelf, remove them before removing the shelf' \
               ' (print "d" to remove a document).'
    del directories[shelf_num]
    return 'The shelf was deleted.'


def add_new_doc(num, type, owner, shelf):
    if shelf not in directories:
        return 'The shelf doesn\'t exist. To add a shelf print \'ads\''
    owner = owner.split(' ')
    for word in range(len(owner)):
        owner[word] = owner[word].capitalize()
    owner = ' '.join(owner)
    document = dict()
    document['type'] = type
    document['number'] = num
    document['name'] = owner
    documents.append(document)
    directories[shelf].append(num)
    return 'The document was successfully added!'


def delete_doc(doc):
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

    return 'The document is successfully deleted!'


def move_doc(doc, shelf):
    a = None
    for d in directories.values():
        if doc in d:
            d.remove(doc)
            a = d
    if a is None:
        return 'The document wasn\'t found on the shelf'
    directories[shelf].append(doc)
    return 'The document was successfully moved!'


def user_interaction():
    command = None
    person = 'p'
    quit = 'q'
    shelf = 's'
    full_doc_info = 'l'
    add_shelf = 'ads'
    delete_shelf = 'ds'
    add_doc = 'ad'
    document = 'd'
    move = 'm'
    list_of_coms = 'lof'
    clod = '\nCurrent list of document:'

    while command != quit:
        command = input('Enter the command, please: \n').lower()
        if command == person:
            doc_num = input('Enter number of the document: \n')
            print(show_doc_owner(doc_num))
        elif command == shelf:
            doc_num = input('Enter number of the document: \n')
            print(show_shelf_of_doc(doc_num))
        elif command == full_doc_info:
            print(show_full_doc_info())
        elif command == add_shelf:
            new_shelf_num = input('Enter number of the new shelf: \n')
            print(add_new_shelf(new_shelf_num))
        elif command == delete_shelf:
            to_be_deleted_shelf_num = input('Enter number of the shelf to delete: \n')
            print(delete_a_shelf(to_be_deleted_shelf_num), clod)
            print(show_full_doc_info())
        elif command == add_doc:
            _num = input('Enter the number of a new document: \n')
            _type = input('Enter the type of the document \n')
            _owner = input('Enter the name of the document\'s owner \n')
            _shelf = input('Enter the number of a shelf to place the document \n')
            print(add_new_doc(_num, _type, _owner, _shelf), clod)
            print(show_full_doc_info())
        elif command == document:
            doc_to_be_deleted = input('Enter number of a document to delete it: \n')
            print(delete_doc(doc_to_be_deleted), clod)
            print(show_full_doc_info())
        elif command == move:
            doc_to_move = input('Enter number of a document to move it: \n')
            _shelf = input('Enter number of the shelf where to move: \n')
            print(move_doc(doc_to_move, _shelf), clod)
            print(show_full_doc_info())
        elif command == list_of_coms:
            print(show_list_of_commands())
        elif command == quit:
            print('The program stopped')
        else:
            print('This command doesn\'t exist \nPrint \'lof\' to see the list of commands')


if __name__ == '__main__':
    show_list_of_commands()
    user_interaction()

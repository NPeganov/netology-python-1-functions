from constants import COMMANDS, K_NUMBER, K_TYPE, K_NAME


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


def create_shelf(new_num):
    if new_num in directories:
        return 'The shelf already exists '
    directories[new_num] = []
    return f'The shelf was successfully added. {read_shelf_list()} '


def create_doc(num, type, owner, shelf):
    if shelf not in directories:
        return 'The shelf doesn\'t exist. To add a shelf type \'ads\' '
    owner = owner.split(' ')
    for word in range(len(owner)):
        owner[word] = owner[word].capitalize()
    owner = ' '.join(owner)
    document = dict()
    document[K_TYPE] = type
    document[K_NUMBER] = num
    document[K_NAME] = owner
    documents.append(document)
    directories[shelf].append(num)
    return 'The document was successfully added! '


def read_doc_by_number(doc_num):
    a = None
    for document in documents:
        if document[K_NUMBER] == doc_num:
            a = document
    if a is None:
        return 'Document was not found '
    else:
        return a


def get_doc_owner(doc_num):
    document = read_doc_by_number(doc_num)
    if document is str:
        return 'Document\'s owner was not found '
    owner = document[K_NAME]
    return owner


def read_shelf(doc_num):
    shelf = None
    for key_shelf_num, values in directories.items():
        if doc_num in values:
            shelf = key_shelf_num
            return shelf
    if shelf is None:
        return 'Document is not found '


def list_doc_info():
    result = ''
    for document in documents:
        for key, values in directories.items():
            if document[K_NUMBER] in values:
                result += f'№: {document[K_NUMBER]}, type: {document[K_TYPE]}, owner: {document[K_NAME]}' \
                          f', storage shelf: {key} \n'
    return f'Current list of document: \n{result} '


def read_shelf_list():
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key}, '

    return f'Current list of shelves: {shelves} '


def list_commands():
    list_of_coms = str()
    for key, value in COMMANDS.items():
        list_of_coms += f'\n{key} - {value}'
    return f'The list of commands: {list_of_coms}'


def update_doc(doc_num, shelf):
    a = None
    if doc_num in directories[shelf]:
        return f'The document is already on shelf {shelf}. '
    for d in directories.values():
        if doc_num in d:
            d.remove(doc_num)
            a = d
    if a is None:
        return 'The document wasn\'t found on the shelf. '
    directories[shelf].append(doc_num)
    return 'The document was successfully moved!. '


def delete_shelf(shelf_num):
    if shelf_num not in directories:
        return 'The shelf doesn\'t exist'
    if directories[shelf_num] != list():
        return 'There are documents on the shelf, remove them before removing the shelf' \
               ' (print "d" to remove a document). '
    del directories[shelf_num]
    return 'The shelf was deleted. '


def delete_doc(doc_num):
    a = None
    for document in documents:
        if document[K_NUMBER] == doc_num:
            documents.remove(document)
            a = doc_num
    if a is None:
        return 'The document doesn\'t exist '
    for d in directories.values():
        if doc_num in d:
            d.remove(doc_num)

    return 'The document is successfully deleted! '

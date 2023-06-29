import logging
from constants import COMMANDS, NUMBER, TYPE, NAME


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
    return f'The shelf was successfully added. {read_shelf_list()}'


def create_doc(num, type, owner, shelf):
    if shelf not in directories:
        return 'The shelf doesn\'t exist. To add a shelf print \'ads\''
    owner = owner.split(' ')
    for word in range(len(owner)):
        owner[word] = owner[word].capitalize()
    owner = ' '.join(owner)
    document = dict()
    document[TYPE] = type
    document[NUMBER] = num
    document[NAME] = owner
    documents.append(document)
    directories[shelf].append(num)
    return 'The document was successfully added!'


def read_doc_owner(doc_num):
    owner = None
    for document in documents:
        if document['number'] == doc_num:
            owner = document['name']
            return owner
    if owner is None:
        return 'Document owner is not found'


def read_shelf(doc_num):
    shelf = None
    for key, values in directories.items():
        if doc_num in values:
            shelf = key
            return shelf
    if shelf is None:
        return 'Document is not found'


def read_doc_info():
    result = ''
    for document in documents:
        for key, values in directories.items():
            if document['number'] in values:
                result += f'№: {document["number"]}, type: {document["type"]}, owner: {document["name"]}' \
                          f', storage shelf: {key} \n'
    return f'Current list of document: \n{result}'


def read_shelf_list():
    shelves = ''
    last_key = list(directories.keys())[-1]
    for key in directories:
        if key == last_key:
            shelves += f'{key}'
        else:
            shelves += f'{key}, '

    a = f'Current list of shelves: {shelves}' #!
    return f'Current list of shelves: {shelves}'


def read_commands_list():
    the_list_of_coms = str()
    for key, value in COMMANDS.items():
        the_list_of_coms += f'\n{key} - {value}'
    return f'The list of commands: {the_list_of_coms}'


def update_doc(doc, shelf):
    a = None
    for d in directories.values():
        if doc in d:
            d.remove(doc)
            a = d
    if a is None:
        return 'The document wasn\'t found on the shelf'
    directories[shelf].append(doc)
    return 'The document was successfully moved!'


def delete_shelf(shelf_num):
    if shelf_num not in directories:
        return 'The shelf doesn\'t exist'
    if directories[shelf_num] != list():
        return 'There are documents on the shelf, remove them before removing the shelf' \
               ' (print "d" to remove a document).'
    del directories[shelf_num]
    return 'The shelf was deleted.'


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

from variables import *
from constants import *


def list_commands():
    list_of_coms = str()
    for key, value in COMMANDS.items():
        list_of_coms += f'\n{key} - {value}'

    print(f'The list of commands: {list_of_coms}')


def list_doc_info():
    result = ''
    for document in documents:
        for key, values in directories.items():
            if document[K_NUMBER] in values:
                result += f'№: {document[K_NUMBER]}, type: {document[K_TYPE]}, owner: {document[K_NAME]}, \
storage shelf: {key} \n'

    print(f'Current list of document: \n{result} ')
